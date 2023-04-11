from django.urls import path
from .views import home_screen_view, personal_schedule_view

urlpatterns = [
    path("", home_screen_view, name="home"),
    path("personal-schedule/", personal_schedule_view, name="personal_schedule")
]
