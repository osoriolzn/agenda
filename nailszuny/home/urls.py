from django.urls import path
from .views import index, agenda

urlpatterns = [
    path('', index, name='home'),
    path('agenda/', agenda, name='agenda')
]