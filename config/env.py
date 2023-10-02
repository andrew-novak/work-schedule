import environ
import sys

env = environ.Env()
is_runserver = "runserver" in sys.argv

env_vars = {}
if not is_runserver:
    env_vars = {
        "IS_PRODUCTION": env.bool("WORK_SCHEDULE_IS_PRODUCTION"),
        "HOST": env.str("WORK_SCHEDULE_HOST"),
        "DJANGO_SECRET_KEY": env.str("WORK_SCHEDULE_DJANGO_SECRET_KEY"),
        "DB_NAME": env.str("WORK_SCHEDULE_DB_NAME"),
        "DB_USER": env.str("WORK_SCHEDULE_DB_USER"),
        "DB_PASSWORD": env.str("WORK_SCHEDULE_DB_PASSWORD"),
        "STATIC_ROOT": env.str("WORK_SCHEDULE_STATIC_ROOT"),

        # Optional:

        # Use a path without a trailing slash, e.g. "/apps/app1"
        "SUBLOCATION": env.str("WORK_SCHEDULE_SUBLOCATION"),
        # Demo user
        # setting them will a 'Login as demo user' button appear on the login screen,
        # use credentials for a staff user but not a superuser
        "DEMO_USER_USERNAME": env.str("WORK_SCHEDULE_DEMO_USER_USERNAME"),
        "DEMO_USER_PASSWORD": env.str("WORK_SCHEDULE_DEMO_USER_PASSWORD")
    }