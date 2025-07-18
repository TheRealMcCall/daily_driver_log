from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'logger/home.html')


def dashboard(request):
    return render(request, 'logger/dashboard.html')


def new_trip(request):
    return render(request, 'logger/new_trip.html')


def day_summary(request):
    return render(request, 'logger/day_summary.html')
