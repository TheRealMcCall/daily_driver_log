from django.shortcuts import render, get_object_or_404, redirect
from .models import DayLog, Trip, UserSettings
from .forms import TripForm, DayLogForm, UserSettingsForm
from datetime import date
from django.contrib import messages
from django.utils.timezone import now


# To render the home page
def home(request):
    return render(request, 'logger/home.html')


# Displays all the daylogs for logged in user on the dashboard view
def dashboard(request):

    today = date.today()
    today_log = DayLog.objects.filter(
        user=request.user, start_date=today
        ).first()

    return render(request, 'logger/dashboard.html', {
        'today_log': today_log,
        'today': today,
    })


# View to create or edit a daylog.
def daylog_form(request, daylog_id=None):
    if daylog_id:
        log = get_object_or_404(DayLog, id=daylog_id, user=request.user)
    else:
        log = None

    if request.method == 'POST':
        form = DayLogForm(request.POST, instance=log)
        if form.is_valid():
            # Links DayLog to the current user before saving
            daylog = form.save(commit=False)
            daylog.user = request.user
            daylog.save()
            messages.success(request, "Today's log created!")
            return redirect('dashboard')
    else:
        form = DayLogForm(instance=log)

    return render(request, 'logger/daylog_form.html', {
        'form': form,
    })


def create_today_log(request):
    today = now().date()
    daylog, created = DayLog.objects.get_or_create(
        user=request.user, start_date=today
        )

    if created:
        messages.success(request, "Today's log was created.")
    else:
        messages.info(request, "Today's log already exists.")

    return redirect('dashboard')


# View to delete a day log
def delete_daylog(request, daylog_id):
    log = get_object_or_404(DayLog, id=daylog_id, user=request.user)
    log.delete()
    return redirect('dashboard')


# View to delete a specific trip
def delete_trip(request, daylog_id, trip_id):
    daylog = get_object_or_404(DayLog, id=daylog_id, user=request.user)
    trip = get_object_or_404(Trip, id=trip_id, day_log=daylog)
    trip.delete()
    return redirect('day_summary', daylog_id=daylog.id)


def daylog_history(request):
    user_daylogs = (
        DayLog.objects
        .filter(user=request.user)
        .order_by('-start_date')
    )
    return render(request, 'logger/daylog_history.html', {
        'daylogs': user_daylogs,
    })


# View for creating and editing a trip
def trip_form(request, daylog_id, trip_id=None):
    daylog = get_object_or_404(DayLog, id=daylog_id, user=request.user)

    # If editing, below gets the specific trip.
    if trip_id:
        trip = get_object_or_404(Trip, id=trip_id, day_log=daylog)
    else:
        trip = None

    if request.method == 'POST':
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            # Link the trip to the daylog before saving.
            trip = form.save(commit=False)
            trip.day_log = daylog
            trip.save()
            return redirect('day_summary', daylog_id=daylog.id)
    else:
        form = TripForm(instance=trip)

    return render(request, 'logger/trip_form.html', {
        'form': form,
        'daylog': daylog,
        'trip': trip,
    })


# View to show a summary of a specific DayLog and its related trips
def day_summary(request, daylog_id):

    daylog = get_object_or_404(DayLog, id=daylog_id, user=request.user)

    return render(request, 'logger/day_summary.html', {
        'daylog': daylog,
        'trips': daylog.trips.all(),
    })


def settings_view(request):
    settings, created = UserSettings.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        if 'reset' in request.POST:
            settings.max_daily_minutes = 600
            settings.max_trip_minutes = 330
            settings.save()
            messages.success(request, "Settings reset to default.")
            return redirect('settings')

        form = UserSettingsForm(request.POST, instance=settings)
        if form.is_valid():
            form.save()
            messages.success(request, "Settings updated successfully.")
            return redirect('dashboard')
    else:
        form = UserSettingsForm(instance=settings)

    return render(request, 'logger/settings.html', {'form': form})
