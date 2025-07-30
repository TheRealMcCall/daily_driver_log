from django.contrib import admin
from django.urls import path, include
from logger import views as logger_views

handler404 = logger_views.custom_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('logger.urls')),
    path('accounts/', include('allauth.urls')),
]
