from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('homePage', homePage, name='EventHomePage'),
    path('testid/<int:id>',tesid,name="Test"),
    path('StaticList', renderList, name="StaticList"),
    path('listEvent', renderListEvent, name="List"),
    path('addevent/', add_event, name="add_event"),
    path('eventslistView/', ListEventView.as_view(), name='list_event_view'),
    path('eventDetails/<int:pk>', DetailEventView.as_view(), name= 'event_datails'),
    path('createform/', create_event, name='create_form'),
    path('eventsCreateView/', CreateEvent.as_view(), name='create_event_form'),
    path('eventsUpdateView/<int:pk>', UpdateEvent.as_view(), name= 'update_event_form'),
    #doit etre sous le nom pk
    
]
