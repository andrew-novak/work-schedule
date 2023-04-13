from django.shortcuts import render
from collections import defaultdict
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
import datetime

def home_screen_view(request):
    return redirect("personal_schedule")

def personal_schedule_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    today = datetime.date.today()
    this_week_monday = today - datetime.timedelta(days=today.weekday())

    shifts = request.user.shift_set.values()
    one_week_shifts = {}
    
    for index in range(7):
        day = this_week_monday + datetime.timedelta(days=index)
        week_day_name = day.strftime('%A')
        one_week_shifts[week_day_name] = shifts.filter(date = day)
    
    context = { "shifts": one_week_shifts.items() }
    return render(request, "screens/personal_schedule.html", context)