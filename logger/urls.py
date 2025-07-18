from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('trip/new/<int:daylog_id>/', views.trip_form, name='trip_form'),
    path('trip/edit/<int:daylog_id>/<int:trip_id>/', views.trip_form, name='edit_trip'),
    path('summary/day/<int:daylog_id>/', views.day_summary, name='day_summary'),
    path('daylog/new/', views.create_daylog, name='create_daylog'),
]
