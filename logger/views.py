from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'logger/home.html')


def dashboard(request):
    return render(request, 'logger/dashboard.html')
