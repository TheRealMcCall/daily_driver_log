from django import forms
from .models import Trip


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['trip_start_time', 'trip_finish_time', 'is_overnight']
        widgets = {
            'trip_start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'trip_finish_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'is_overnight': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
