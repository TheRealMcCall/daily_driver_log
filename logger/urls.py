"""
Urls for the logger app.
"""

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('dashboard/', views.dashboard, name='dashboard'),

    path(
        'trip/new/<int:daylog_id>/',
        views.trip_form,
        name='trip_form'
    ),
    path(
        'trip/edit/<int:daylog_id>/<int:trip_id>/',
        views.trip_form,
        name='edit_trip'
    ),
    path(
        'trip/delete/<int:daylog_id>/<int:trip_id>/',
        views.delete_trip,
        name='delete_trip'
    ),
    path(
        'summary/day/<int:daylog_id>/',
        views.day_summary,
        name='day_summary'
    ),
    path(
        'daylog/new/',
        views.daylog_form,
        name='create_daylog'
    ),
    path(
        'daylog/edit/<int:daylog_id>/',
        views.daylog_form,
        name='edit_daylog'
    ),
    path(
        'daylog/delete/<int:daylog_id>/',
        views.delete_daylog,
        name='delete_daylog'
    ),
    path(
        'daylog/create-today/',
        views.create_today_log,
        name='create_today_log'
    ),
    path(
        'history/',
        views.daylog_history,
        name='daylog_history'
    ),
    path(
        'settings/',
        views.settings_view,
        name='settings'
    ),
    path(
        'accounts/',
        include('allauth.urls')
    ),
]
