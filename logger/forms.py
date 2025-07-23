from django import forms
from .models import Trip, DayLog
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
