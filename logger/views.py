from django.shortcuts import render, get_object_or_404, redirect
from .models import DayLog, Trip, UserSettings
from .forms import TripForm, DayLogForm, UserSettingsForm
from datetime import date
from django.contrib import messages
from django.utils.timezone import now
from django.core.serializers.json import DjangoJSONEncoder
import json


def home(request):
    """
    Render the home page.
    """
    return render(request, 'logger/home.html')


def dashboard(request):
    """
    Display the dashboard with today's DayLog and user settings.
    """
    today = date.today()
    today_log = DayLog.objects.filter(
        user=request.user,
        start_date=today
    ).first()

    user_settings = UserSettings.objects.filter(
        user=request.user
    ).first()

    return render(request, 'logger/dashboard.html', {
        'today_log': today_log,
        'today': today,
        'user_settings': user_settings,
    })


def daylog_form(request, daylog_id=None):
    """
    View to create or edit a DayLog.
    """
    if daylog_id:
        log = get_object_or_404(
            DayLog,
            id=daylog_id,
            user=request.user
        )
    else:
        log = None

    if request.method == 'POST':
        form = DayLogForm(request.POST, instance=log)
        if form.is_valid():
            daylog = form.save(commit=False)
            daylog.user = request.user
            daylog.save()
            messages.success(request, "Today's log created!")
            return redirect('dashboard')
    else:
        form = DayLogForm(instance=log)

    existing_dates = (
        DayLog.objects
        .filter(user=request.user)
        .exclude(pk=log.pk if log else None)
        .values_list('start_date', flat=True)
    )

    existing_dates_json = json.dumps(
        list(existing_dates),
        cls=DjangoJSONEncoder
    )

    return render(request, 'logger/daylog_form.html', {
        'form': form,
        'existing_dates_json': existing_dates_json,
    })


def create_today_log(request):
    """
    Create a DayLog for today if one does not already exist.
    """
    today = now().date()
    daylog, created = DayLog.objects.get_or_create(
        user=request.user,
        start_date=today
    )

    if created:
        messages.success(request, "Today's log was created.")
    else:
        messages.info(request, "Today's log already exists.")

    return redirect('dashboard')


def delete_daylog(request, daylog_id):
    """
    Delete a specific DayLog by ID.
    """
    log = get_object_or_404(
        DayLog,
        id=daylog_id,
        user=request.user
    )
    log.delete()
    return redirect('dashboard')


def delete_trip(request, daylog_id, trip_id):
    """
    Delete a specific Trip within a DayLog.
    """
    daylog = get_object_or_404(
        DayLog,
        id=daylog_id,
        user=request.user
    )
    trip = get_object_or_404(
        Trip,
        id=trip_id,
        day_log=daylog
    )
    trip.delete()
    return redirect('day_summary', daylog_id=daylog.id)


def daylog_history(request):
    """
    Display the user's full history of DayLogs.
    """
    user_daylogs = DayLog.objects.filter(
        user=request.user
    ).order_by('-start_date')

    return render(request, 'logger/daylog_history.html', {
        'daylogs': user_daylogs,
    })


def trip_form(request, daylog_id, trip_id=None):
    """
    Create or edit a Trip for a given DayLog.
    """
    daylog = get_object_or_404(
        DayLog,
        id=daylog_id,
        user=request.user
    )

    if trip_id:
        trip = get_object_or_404(
            Trip,
            id=trip_id,
            day_log=daylog
        )
    else:
        trip = None

    if request.method == 'POST':
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.day_log = daylog
            trip.save()
            return redirect('day_summary', daylog_id=daylog.id)
    else:
        form = TripForm(instance=trip)

    existing_trips = (
        daylog.trips.exclude(id=trip_id)
        .values("trip_start_time", "trip_finish_time")
    )

    existing_trips_json = json.dumps(
        list(existing_trips),
        cls=DjangoJSONEncoder
    )

    return render(request, 'logger/trip_form.html', {
        'form': form,
        'daylog': daylog,
        'trip': trip,
        'existing_trips_json': existing_trips_json,
    })


def day_summary(request, daylog_id):
    """
    Display a summary of a DayLog and its associated Trips.
    """
    daylog = get_object_or_404(
        DayLog,
        id=daylog_id,
        user=request.user
    )

    user_settings = getattr(request.user, 'usersettings', None)

    return render(request, 'logger/day_summary.html', {
        'daylog': daylog,
        'trips': daylog.trips.order_by('trip_start_time'),
        'user_settings': user_settings,
    })


def settings_view(request):
    """
    View to display and update user driving limit settings.
    """
    settings, created = UserSettings.objects.get_or_create(
        user=request.user
    )

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

    return render(request, 'logger/settings.html', {
        'form': form
    })


def custom_404(request, exception):
    """
    Custom view to render the 404 error page.
    """
    return render(request, '404.html', status=404)
