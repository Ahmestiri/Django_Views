from django.urls import path
from . import views

urlpatterns = [
    # Auth Routes
    path("login/", views.login_index, name="login"),
    path("logout/", views.logout_index, name="logout"),
    path("register/", views.register_index, name="register"),
    # User Routes
    path("user/view/<str:pk>/", views.user_index, name="user_index"),
    path("user/edit/<str:pk>/", views.user_edit, name="user_edit"),
    # Message Routes
    path("message/delete/<str:pk>/", views.message_delete, name="message_delete"),
    # Room Routes
    path("", views.home_index, name="home_index"),
    path("room/view/<str:pk>/", views.room_view, name="room_view"),
    path("room/add", views.room_add, name="room_add"),
    path("room/edit/<str:pk>/", views.room_edit, name="room_edit"),
    path("room/delete/<str:pk>/", views.room_delete, name="room_delete"),
]
