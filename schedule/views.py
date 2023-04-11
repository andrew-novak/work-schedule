from django.shortcuts import render
from collections import defaultdict
import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def home_screen_view(request):
    return render(request, "screens/personal_schedule.html")

def personal_schedule_view(request):
    shifts = {
        "Monday": [
            {"role": "Programming", "start": "8:00", "end": "16:00"}
        ],
        "Tuesday": [
            {"role": "Programming", "start": "10:00", "end": "14:00"}
        ],
    }
    context = { "shifts": shifts.items() }
    return render(request, "screens/personal_schedule.html", context)