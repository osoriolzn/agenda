from django.urls import path
from .views import index, show_calendar, agenda

urlpatterns = [
    path('', index, name='home'),
    path('agenda/', agenda, name='agenda'),
    path('calendario/', show_calendar, name='calendar')
]