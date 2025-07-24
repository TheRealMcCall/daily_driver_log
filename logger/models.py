"""
Models for tracking daily driver logs, trips, and user-specific settings.
"""

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver


class DayLog(models.Model):
    """
    Model representing a single day's log of driving for a user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()

    def total_minutes_driven(self):
        """
        Return the total minutes driven across all trips in this DayLog.
        """
        return sum(trip.trip_duration() for trip in self.trips.all())

    def total_hours_and_minutes(self):
        """
        Return the total driving time in (hours, minutes) tuple.
        """
        total_minutes = self.total_minutes_driven()
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return hours, minutes

    def over_daily_limit(self):
        """
        Check if the user has exceeded their max daily driving time.
        """
        user_settings = getattr(self.user, 'usersettings', None)
        max_minutes = (
            user_settings.max_daily_minutes if user_settings else 600
        )
        return self.total_minutes_driven() > max_minutes

    def minutes_remaining(self, max_daily_minutes=600):
        """
        Return the number of driving minutes remaining for the day.
        """
        remaining = max_daily_minutes - self.total_minutes_driven()
        return max(0, remaining)

    def hours_and_minutes_remaining(self, max_daily_minutes=600):
        """
        Return remaining time in (hours, minutes) tuple.
        """
        remaining = self.minutes_remaining(max_daily_minutes)
        hours = remaining // 60
        minutes = remaining % 60
        return hours, minutes

    def __str__(self):
        """
        Return a string representation of the DayLog for admin display.
        """
        return (
            f" Created by User {self.user.username}"
            f" Day Log's Date = {self.start_date}"
            f" Total Minutes Driven = {self.total_minutes_driven()}"
            f" Daily Limit Exceeded = {self.over_daily_limit()}"
        )

    def save(self, *args, **kwargs):
        """
        Validate date constraints and uniqueness before saving.
        """
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


class Trip(models.Model):
    """
    Model representing an individual trip within a DayLog.
    """
    day_log = models.ForeignKey(
        DayLog,
        on_delete=models.CASCADE,
        related_name='trips'
    )
    trip_start_time = models.TimeField()
    trip_finish_time = models.TimeField()
    is_overnight = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        """
        Validate time range and prevent overlaps before saving.
        """
        trip_start_time = datetime.combine(
            self.day_log.start_date,
            self.trip_start_time
        )
        trip_end_time = datetime.combine(
            self.day_log.start_date,
            self.trip_finish_time
        )

        if self.is_overnight:
            if trip_end_time <= trip_start_time:
                trip_end_time += timedelta(days=1)
        else:
            if trip_end_time <= trip_start_time:
                raise ValidationError(
                    "Finish time must be after start time."
                )

        check_end_time = trip_end_time

        for other_trip in self.day_log.trips.exclude(pk=self.pk):
            other_start = datetime.combine(
                self.day_log.start_date,
                other_trip.trip_start_time
            )
            other_end = datetime.combine(
                self.day_log.start_date,
                other_trip.trip_finish_time
            )

            if other_trip.is_overnight and other_end <= other_start:
                other_end += timedelta(days=1)
            if self.is_overnight and trip_end_time <= trip_start_time:
                trip_end_time += timedelta(days=1)

            if trip_start_time < other_end and check_end_time > other_start:
                raise ValidationError(
                    "This trip overlaps with another trip."
                )

        super().save(*args, **kwargs)

    def trip_duration(self):
        """
        Return trip duration in minutes.
        """
        trip_start_time = datetime.combine(
            self.day_log.start_date,
            self.trip_start_time
        )
        trip_end_time = datetime.combine(
            self.day_log.start_date,
            self.trip_finish_time
        )

        if self.is_overnight:
            trip_end_time += timedelta(days=1)

        trip_duration = trip_end_time - trip_start_time
        return int(trip_duration.total_seconds() // 60)

    def total_hours_and_minutes(self):
        """
        Return trip duration as (hours, minutes).
        """
        total_minutes = self.trip_duration()
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return hours, minutes

    def over_trip_limit(self):
        """
        Check if the trip duration exceeds the user's trip limit.
        """
        user_settings = getattr(self.day_log.user, 'usersettings', None)
        max_minutes = (
            user_settings.max_trip_minutes if user_settings else 330
        )
        return self.trip_duration() > max_minutes

    def __str__(self):
        """
        Return a string representation of the trip for admin display.
        """
        return (
            f"User {self.day_log.user.username}"
            f" Date {self.day_log.start_date},"
            f" Start time: {self.trip_start_time},"
            f" Finish time: {self.trip_finish_time},"
            f" Duration: {self.trip_duration()} minutes"
            f" Trip limit exceeded = {self.over_trip_limit()}"
        )


class UserSettings(models.Model):
    """
    Model storing user-specific driving limits.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    max_daily_minutes = models.PositiveIntegerField(default=600)
    max_trip_minutes = models.PositiveIntegerField(default=330)

    def __str__(self):
        return f"{self.user.username}'s settings"

    @property
    def daily_hours(self):
        return self.max_daily_minutes // 60

    @property
    def daily_minutes_only(self):
        return self.max_daily_minutes % 60

    @property
    def trip_hours(self):
        return self.max_trip_minutes // 60

    @property
    def trip_minutes_only(self):
        return self.max_trip_minutes % 60


@receiver(post_save, sender=User)
def create_user_settings(sender, instance, created, **kwargs):
    """
    Automatically create UserSettings when a new user is registered.
    """
    if created:
        UserSettings.objects.create(user=instance)
