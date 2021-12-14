from os import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.top, name="top"),
    path("<str:room_name>/",views.room, name="room"),
    path("api/make", views.make, name="make"),
]
