from django.shortcuts import render, get_object_or_404, redirect
from .models import DayLog, Trip
from .forms import TripForm, DayLogForm

# Create your views here.


def home(request):
    return render(request, 'logger/home.html')


def dashboard(request):

    user_daylogs = DayLog.objects.filter(user=request.user).order_by('-start_date')

    return render(request, 'logger/dashboard.html', {
        'daylogs': user_daylogs,
    })


def create_daylog(request):
    if request.method == 'POST':
        form = DayLogForm(request.POST)
        if form.is_valid():
            daylog = form.save(commit=False)
            daylog.user = request.user
            daylog.save()
            return redirect('dashboard')
    else:
        form = DayLogForm()

    return render(request, 'logger/create_daylog.html', {'form': form})


def delete_trip(request, daylog_id, trip_id):
    daylog = get_object_or_404(DayLog, id=daylog_id, user=request.user)
    trip = get_object_or_404(Trip, id=trip_id, day_log=daylog)
    trip.delete()
    return redirect('day_summary', daylog_id=daylog.id)


def trip_form(request, daylog_id, trip_id=None):
    daylog = get_object_or_404(DayLog, id=daylog_id, user=request.user)

    if trip_id:
        trip = get_object_or_404(Trip, id=trip_id, day_log=daylog)
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

    return render(request, 'logger/trip_form.html', {
        'form': form,
        'daylog': daylog,
        'trip': trip,
    })


def day_summary(request, daylog_id):

    daylog = get_object_or_404(DayLog, id=daylog_id, user=request.user)

    return render(request, 'logger/day_summary.html', {
        'daylog': daylog,
        'trips': daylog.trips.all(),
        'total_minutes': daylog.total_minutes_driven(),
        'over_limit': daylog.over_daily_limit()
    })
