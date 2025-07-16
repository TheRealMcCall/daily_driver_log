from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# Model for DayLog
class DayLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()


# adjusts how DayLog objects are shown in admin
def __str__(self):
    return f"{self.user.username} - {self.start_date}"


# Model for individual trips
class Trip(models.Model):
    day_log = models.ForeignKey(DayLog, on_delete=models.CASCADE, related_name='trips')
    start_time = models.TimeField()
    finish_time = models.TimeField()
    is_overnight = models.BooleanField(default=False)
