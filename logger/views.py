from django.shortcuts import render, get_object_or_404, redirect
from .models import DayLog, Trip
from .forms import TripForm, DayLogForm


# To render the home page
def home(request):
    return render(request, 'logger/home.html')


# Displays all the daylogs for logged in user on the dashboard view
def dashboard(request):

    user_daylogs = (
         DayLog.objects
         .filter(user=request.user)
         .order_by('-start_date')
    )

    return render(request, 'logger/dashboard.html', {
        'daylogs': user_daylogs,
    })


# View to display and process the form for creating a new DayLog
def create_daylog(request):

    if request.method == 'POST':
        form = DayLogForm(request.POST)
        if form.is_valid():
            # Links DayLog to the current user before saving
            daylog = form.save(commit=False)
            daylog.user = request.user
            daylog.save()
            return redirect('dashboard')
    else:
        form = DayLogForm()

    return render(request, 'logger/create_daylog.html', {'form': form})


# View to delete a specific trip
def delete_trip(request, daylog_id, trip_id):
    daylog = get_object_or_404(DayLog, id=daylog_id, user=request.user)
    trip = get_object_or_404(Trip, id=trip_id, day_log=daylog)
    trip.delete()
    return redirect('day_summary', daylog_id=daylog.id)


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
        'total_minutes': daylog.total_minutes_driven(),
        'over_limit': daylog.over_daily_limit()
    })
