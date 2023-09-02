from django.shortcuts import render
from collections import defaultdict
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from datetime import date, datetime, timedelta

from schedule.models import Shift

def home_screen_view(request):
    return redirect("personal_schedule")

def personal_schedule_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    # based on today
    today = date.today()
    this_week_monday = today - timedelta(days=today.weekday())
    this_week_sunday = this_week_monday + timedelta(days=6)

    # based on the passed value or today (if no value passed)
    monday = this_week_monday
    query_monday = request.GET.get('monday')
    if query_monday:
        # TODO: check if it is Monday in correct format
        monday = datetime.strptime(query_monday, '%d-%m-%Y').date()
    sunday = monday + timedelta(days=6)
    previous_monday = monday - timedelta(days=7)
    next_monday = monday + timedelta(days=7)

    week_string = f"{monday.strftime('%B %d')} - {sunday.strftime('%B %d, %Y')}"

    #shifts = request.user.shift_set.values()
    one_week_shifts = Shift.objects.filter(user=request.user, date__range=[monday, sunday])

    shifts_by_weekday = {}
    for index in range(7):
        day = monday + timedelta(days=index)
        week_day_name = day.strftime('%A')
        shifts_by_weekday[week_day_name] = one_week_shifts.filter(date = day)
    
    formatted_previous_monday = previous_monday.strftime("%d-%m-%Y")
    formatted_next_monday = next_monday.strftime("%d-%m-%Y")

    context = {
        "week_string": week_string,
        "previous_monday": formatted_previous_monday,
        "next_monday": formatted_next_monday,
        "shifts": shifts_by_weekday.items(),
    }
    return render(request, "screens/personal_schedule.html", context)

def team_schedule_view(request):
    '''
    if not request.user.is_authenticated:
        return redirect("login")
    
    today = date.today()
    this_week_monday = today - timedelta(days=today.weekday())
    this_week_sunday = this_week_monday + timedelta(days=6)

    first_monday = request.GET.get('first_monday', this_week_monday)

    #shifts = request.user.shift_set.values()
    one_week_shifts = Shift.objects.filter(user=request.user, date__range=[this_week_monday, this_week_sunday])
    
    one_week_shifts = {}
    for index in range(7):
        day = this_week_monday + timedelta(days=index)
        week_day_name = day.strftime('%A')
        one_week_shifts[week_day_name] = one_week_shifts.filter(date = day)
    
    context = { "shifts": one_week_shifts.items() }
    return render(request, "screens/personal_schedule.html", context)
    '''
    return render(request, "screens/team_schedule.html")
