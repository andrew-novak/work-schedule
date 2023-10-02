from django.shortcuts import render
from collections import defaultdict
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from datetime import date, datetime, timedelta
import environ
from django.contrib.auth.views import LoginView

from config.env import env_vars
from schedule.models import Shift

'''
DEMO_USER_USERNAME = env_vars.get("DEMO_USER_USERNAME")
DEMO_USER_PASSWORD = env_vars.get("DEMO_USER_PASSWORD")
is_demo_user = DEMO_USER_USERNAME is not None and DEMO_USER_PASSWORD is not None
'''
DEMO_USER_USERNAME = env_vars.get("b")
DEMO_USER_PASSWORD = env_vars.get("b")
is_demo_user = True

class login_view(LoginView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_demo_login_available'] = is_demo_user
        return context
    
    def handle_demo_user_login(self):
        print(not is_demo_user)
    
        if not is_demo_user:
            form = self.get_form()
            form.errors.clear()
            form.add_error(None, "Demo login is disabled")
            return self.form_invalid(form)
        
        # Demo user
        user = authenticate(
            self.request,
            username=DEMO_USER_USERNAME,
            password=DEMO_USER_PASSWORD
        )

        # Successful authentication
        if user is not None:
            login(self.request, user)
            return redirect(self.get_success_url())   
        # Handle authentication failure
        else:
            form = self.get_form()
            form.errors.clear()
            form.add_error(None, "Invalid demo user credentials configured on server")
            return self.form_invalid(form)

    def post(self, request, *args, **kwargs):
        if 'demo-login-button' in self.request.POST:
            return self.handle_demo_user_login()
        # Handle default
        return super().post(request, *args, **kwargs)

def login_demo_user_view(request):
    if not is_demo_user:
        return render(request, 'login.html', {'error_message': 'Demo login is disabled'})

    # Demo user
 
    user = authenticate(request, username=DEMO_USER_USERNAME, password=DEMO_USER_PASSWORD)

    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        # Handle authentication failure
        return render(request, 'login.html', {'error_message': 'Invalid demo user credentials'})

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

    week_string = f"{monday.strftime('%d %b')} - {sunday.strftime('%d %b, %Y')}"

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

    week_string = f"{monday.strftime('%d %b')} - {sunday.strftime('%d %b, %Y')}"

    one_week_shifts = Shift.objects.filter(date__range=[monday, sunday])

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
    return render(request, "screens/team_schedule.html", context)
