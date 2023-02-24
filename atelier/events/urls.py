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
    path('eventDetails/<int:pk>', DetailEventView.as_view(), name= 'event_details')
    #doit etre sous le nom pk
    
]
