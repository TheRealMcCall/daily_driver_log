"""
Admin configuration for DayLog and Trip models.
"""

from django.contrib import admin
from .models import DayLog, Trip

admin.site.register(DayLog)
admin.site.register(Trip)
