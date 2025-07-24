from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


# Model for DayLog
class DayLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()

# To sum up the total minutes driven across trips for the day.
    def total_minutes_driven(self):
        return sum(trip.trip_duration() for trip in self.trips.all()
                   )

# Convert total minutes into hours and minutes
    def total_hours_and_minutes(self):
        total_minutes = self.total_minutes_driven()
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return hours, minutes

# Sets daily limit allowed and returns true or false if limit is exceeded.
    def over_daily_limit(self):
        user_settings = getattr(self.user, 'usersettings', None)
        max_minutes = user_settings.max_daily_minutes if user_settings else 600
        return self.total_minutes_driven() > max_minutes

# Adjusts how DayLogs are shown in admin.
    def __str__(self):
        return (
            f" Created by User {self.user.username}"
            f" Day Log's Date = {self.start_date}"
            f" Total Minutes Driven = {self.total_minutes_driven()}"
            f" Daily Limit Exceeded = {self.over_daily_limit()}"
        )

    def minutes_remaining(self, max_daily_minutes=600):
        remaining = max_daily_minutes - self.total_minutes_driven()
        return max(0, remaining)

    def hours_and_minutes_remaining(self, max_daily_minutes=600):
        remaining = self.minutes_remaining(max_daily_minutes)
        hours = remaining // 60
        minutes = remaining % 60
        return hours, minutes

    def save(self, *args, **kwargs):
        today = datetime.now().date()

        if self.start_date < today - timedelta(days=2):
            raise ValidationError(
                "You can only create logs from the last 2 days."
                )

        if self.start_date > today:
            raise ValidationError("You cannot create logs for future dates.")

        existing = DayLog.objects.filter(
            user=self.user,
            start_date=self.start_date
        ).exclude(pk=self.pk)

        if existing.exists():
            raise ValidationError("A DayLog for this date already exists.")

        super().save(*args, **kwargs)


# Model for individual trips
class Trip(models.Model):
    day_log = models.ForeignKey(
        DayLog,
        on_delete=models.CASCADE,
        related_name='trips'
    )
    trip_start_time = models.TimeField()
    trip_finish_time = models.TimeField()
    is_overnight = models.BooleanField(default=False)

# Validates that the fields are correct before saving
    def save(self, *args, **kwargs):
        trip_start_time = datetime.combine(
            self.day_log.start_date, self.trip_start_time
            )
        trip_end_time = datetime.combine(
            self.day_log.start_date, self.trip_finish_time
            )

        if self.is_overnight:
            if trip_end_time <= trip_start_time:
                trip_end_time += timedelta(days=1)
        else:
            if trip_end_time <= trip_start_time:
                raise ValidationError(
                    "Finish time must be after start time.")

        check_end_time = trip_end_time

        for other_trip in self.day_log.trips.exclude(pk=self.pk):
            other_start = datetime.combine(
                self.day_log.start_date, other_trip.trip_start_time
                )
            other_end = datetime.combine(
                self.day_log.start_date, other_trip.trip_finish_time
                )

            if other_trip.is_overnight and other_end <= other_start:
                other_end += timedelta(days=1)
            if self.is_overnight and trip_end_time <= trip_start_time:
                trip_end_time += timedelta(days=1)

            if trip_start_time < other_end and check_end_time > other_start:
                raise ValidationError("This trip overlaps with another trip.")

        super().save(*args, **kwargs)

# Calculates the individual trip duration.
    def trip_duration(self):
        trip_start_time = datetime.combine(
            self.day_log.start_date, self.trip_start_time
            )
        trip_end_time = datetime.combine(
            self.day_log.start_date, self.trip_finish_time
            )

        if self.is_overnight:
            trip_end_time += timedelta(days=1)

        trip_duration = trip_end_time - trip_start_time
        return int(trip_duration.total_seconds() // 60)

# Convert total minutes into hours and minutes
    def total_hours_and_minutes(self):
        total_minutes = self.trip_duration()
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return hours, minutes

# Sets trip limit allowed and returns true or false if limit is exceeded.
    def over_trip_limit(self):
        user_settings = getattr(self.day_log.user, 'usersettings', None)
        max_minutes = user_settings.max_trip_minutes if user_settings else 330
        return self.trip_duration() > max_minutes

# adjusts how trips are shown in admin
    def __str__(self):
        return (
            f"User {self.day_log.user.username}"
            f" Date {self.day_log.start_date},"
            f" Start time: {self.trip_start_time},"
            f" Finish time: {self.trip_finish_time},"
            f" Duration: {self.trip_duration()} minutes"
            f" Trip limit exceeded = {self.over_trip_limit()}"
        )


class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    max_daily_minutes = models.PositiveIntegerField(default=600)
    max_trip_minutes = models.PositiveIntegerField(default=330)

    def __str__(self):
        return f"{self.user.username}'s settings"


@receiver(post_save, sender=User)
def create_user_settings(sender, instance, created, **kwargs):
    if created:
        UserSettings.objects.create(user=instance)
