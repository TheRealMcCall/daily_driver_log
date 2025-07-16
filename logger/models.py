from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
# Create your models here.


# Model for DayLog
class DayLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()

# To sum up the total minutes driven across trips for the day.
    def total_minutes_driven(self):
        return sum(trip.trip_duration() for trip in self.trips.all()
                   )

# Sets daily limit allowed and returns true or false if limit is exceeded.
    def over_daily_limit(self, max_daily_minutes=600):
        return self.total_minutes_driven() > max_daily_minutes

# Adjusts how DayLogs are shown in admin.
    def __str__(self):
        return (
            f" Created by User {self.user.username}"
            f" Day Log's Date = {self.start_date}"
            f" Total Minutes Driven = {self.total_minutes_driven()}"
            f" Daily Limit Exceeded = {self.over_daily_limit()}"
        )


# Model for individual trips
class Trip(models.Model):
    day_log = models.ForeignKey(DayLog, on_delete=models.CASCADE, related_name='trips')
    trip_start_time = models.TimeField()
    trip_finish_time = models.TimeField()
    is_overnight = models.BooleanField(default=False)

# Validates that the fields are correct before saving
    def save(self, *args, **kwargs):
        trip_start_time = datetime.combine(self.day_log.start_date, self.trip_start_time)
        trip_end_time = datetime.combine(self.day_log.start_date, self.trip_finish_time)
        if self.is_overnight:
            if trip_end_time <= trip_start_time:
                trip_end_time += timedelta(days=1)
        else:
            if trip_end_time <= trip_start_time:
                raise ValidationError("Finish time must be after start time for non-overnight trips.")
        super().save(*args, **kwargs)

# Calculates the individual trip duration.
    def trip_duration(self):
        trip_start_time = datetime.combine(self.day_log.start_date, self.trip_start_time)
        trip_end_time = datetime.combine(self.day_log.start_date, self.trip_finish_time)
        if self.is_overnight:
            trip_end_time += timedelta(days=1)

        trip_duration = trip_end_time - trip_start_time
        return int(trip_duration.total_seconds() // 60)

# Sets trip limit allowed and returns true or false if limit is exceeded.
    def over_trip_limit(self, max_trip_minutes=330):
        return self.trip_duration() > max_trip_minutes

# adjusts how trips are shown in admin
    def __str__(self):
        return (
            f" A Trip by User {self.day_log.user.username} on Date {self.day_log.start_date}, "
            f"Start time: {self.trip_start_time}, Finish time: {self.trip_finish_time},"
            f"Duration: {self.trip_duration()} minutes"
            f" Trip limit exceeded = {self.over_trip_limit()}"
        )
