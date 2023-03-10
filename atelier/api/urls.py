from django.urls import path
from .views import *

urlpatterns = [
    path('get/', getEvent, name='getEvent'),
    path('add/', addEvent, name='addEvent'),
    path('delete/<int:id>/', addEvent, name='deleteEvent'),
    path('update/<int:id>/', addEvent, name='updateEvent'),
    
    
]
