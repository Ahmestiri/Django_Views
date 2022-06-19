from django.urls import path
from . import views

urlpatterns = [
    # Home Routes
    path("", views.home_index, name="home_index"),
    # Room Routes
    path("room/<str:pk>/", views.room_view, name="room_view"),
    path("room/", views.room_add, name="room_add"),
]
