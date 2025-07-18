from django.shortcuts import render, get_object_or_404
from .models import DayLog

# Create your views here.


def home(request):
    return render(request, 'logger/home.html')


def dashboard(request):
    return render(request, 'logger/dashboard.html')


def new_trip(request):
    return render(request, 'logger/new_trip.html')


def day_summary(request, daylog_id):

    daylog = get_object_or_404(DayLog, id=daylog_id, user=request.user)

    return render(request, 'logger/day_summary.html', {
        'daylog': daylog,
        'trips': daylog.trips.all(),
        'total_minutes': daylog.total_minutes_driven(),
        'over_limit': daylog.over_daily_limit()
    })
