from django.urls import path, include
from .import views

urlpatterns = [
    # Homepage
    path('', views.home, name="home"),

    # Dashboard: lists user's day logs
    path('dashboard/', views.dashboard, name='dashboard'),

    # Create a New trip linked to a specific DayLog
    path('trip/new/<int:daylog_id>/', views.trip_form, name='trip_form'),

    # Edit an existing trip
    path('trip/edit/<int:daylog_id>/<int:trip_id>/', views.trip_form, name='edit_trip'),

    # Delete a trip
    path('trip/delete/<int:daylog_id>/<int:trip_id>/', views.delete_trip, name='delete_trip'),

    # Day Summary: list all trips and summary for specific a specific day
    path('summary/day/<int:daylog_id>/', views.day_summary, name='day_summary'),

    # Create a new day log
    path('daylog/new/', views.create_daylog, name='create_daylog'),

    # For Django user authentication
    path('accounts/', include('allauth.urls'))
]
