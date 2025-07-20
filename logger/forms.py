from django import forms
from .models import Trip, DayLog


# Form to create or update a trip.
class TripForm(forms.ModelForm):
    class Meta:
        # Links this form to the Trip model.
        model = Trip
        fields = ['trip_start_time', 'trip_finish_time', 'is_overnight']
        widgets = {
            'trip_start_time': forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'}
                 ),
            'trip_finish_time': forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'}
                 ),
            'is_overnight': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}
                ),
        }


# Form to create a Daylog.
class DayLogForm(forms.ModelForm):
    class Meta:
        # Links this form to the DayLog model.
        model = DayLog
        fields = ['start_date']
        widgets = {
            'start_date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}),
        }
