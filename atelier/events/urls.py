from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('homePage', homePage, name='EventHomePage'),
    path('testid/<int:id>',tesid,name="Test"),
    path('StaticList', renderList, name="StaticList")
]