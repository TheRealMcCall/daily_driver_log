from django.shortcuts import render, get_object_or_404, redirect
from .models import DayLog
from .forms import TripForm

# Create your views here.


def home(request):
    return render(request, 'logger/home.html')


def dashboard(request):

    user_daylogs = DayLog.objects.filter(user=request.user).order_by('-start_date')

    return render(request, 'logger/dashboard.html', {
        'daylogs': user_daylogs,
    })


def new_trip(request, daylog_id):
    daylog = get_object_or_404(DayLog, id=daylog_id, user=request.user)

    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.day_log = daylog
            trip.save()
            return redirect('day_summary', daylog_id=daylog.id)
    else:
        form = TripForm()

    return render(request, 'logger/new_trip.html', {
        'form': form,
        'daylog': daylog,
    })


def day_summary(request, daylog_id):

    daylog = get_object_or_404(DayLog, id=daylog_id, user=request.user)

    return render(request, 'logger/day_summary.html', {
        'daylog': daylog,
        'trips': daylog.trips.all(),
        'total_minutes': daylog.total_minutes_driven(),
        'over_limit': daylog.over_daily_limit()
    })
