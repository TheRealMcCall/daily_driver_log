from django import forms
from .models import Trip, DayLog, UserSettings
from allauth.account.forms import SignupForm


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


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(
        max_length=30, label='First Name', required=True
     )
    last_name = forms.CharField(
        max_length=30, label='Last Name', required=True
        )

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class UserSettingsForm(forms.ModelForm):
    max_daily_hours = forms.IntegerField(min_value=0, label="Max Daily Hours")
    max_daily_minutes_only = forms.IntegerField(min_value=0, max_value=59, label="Max Daily Minutes")

    max_trip_hours = forms.IntegerField(min_value=0, label="Max Trip Hours")
    max_trip_minutes_only = forms.IntegerField(min_value=0, max_value=59, label="Max Trip Minutes")

    class Meta:
        model = UserSettings
        fields = []

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        initial = kwargs.setdefault('initial', {})

        if instance:
            initial['max_daily_hours'] = instance.max_daily_minutes // 60
            initial['max_daily_minutes_only'] = instance.max_daily_minutes % 60
            initial['max_trip_hours'] = instance.max_trip_minutes // 60
            initial['max_trip_minutes_only'] = instance.max_trip_minutes % 60

        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.max_daily_minutes = (
            self.cleaned_data['max_daily_hours'] * 60 +
            self.cleaned_data['max_daily_minutes_only']
        )
        instance.max_trip_minutes = (
            self.cleaned_data['max_trip_hours'] * 60 +
            self.cleaned_data['max_trip_minutes_only']
        )
        if commit:
            instance.save()
        return instance
