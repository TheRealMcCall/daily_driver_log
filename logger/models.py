from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class DayLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()

class Trip(models.Model):
    day_log = models.ForeignKey(DayLog, on_delete=models.CASCADE, related_name ='trips')
    start_time = models.TimeField()
    finish_time = models.TimeField()
    is_overnight = models.BooleanField(default=False)
