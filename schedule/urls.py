from django.urls import path
from .views import home_screen_view, personal_schedule_view
from django.urls import path, include

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', home_screen_view, name="home"),
    path('personal_schedule/', personal_schedule_view, name='personal_schedule')
]
