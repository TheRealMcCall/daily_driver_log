from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('trip/new/', views.new_trip, name='new_trip'),
    path('summary/day/', views.day_summary, name='day_summary')
]
