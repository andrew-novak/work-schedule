from django.urls import path
from .views import login_view, home_screen_view, personal_schedule_view, team_schedule_view
from django.urls import path, include

urlpatterns = [
    path('login/', login_view.as_view() , name="login"),
    path('', include('django.contrib.auth.urls')),
    path('', home_screen_view, name="home"),
    path('personal_schedule/', personal_schedule_view, name='personal_schedule'),
    path('team_schedule/', team_schedule_view, name='team_schedule'),
]
