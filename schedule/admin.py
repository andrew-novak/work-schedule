from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Shift

#admin.site.unregister(Group)

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    pass

#admin.site.register(Shift, ShiftAdmin)