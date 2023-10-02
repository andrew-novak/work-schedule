from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Shift

# Right now the header text is hardocded anyway,
# but may use this value in future.
admin.site.site_header = 'Work Schedule - Manager Panel'

#admin.site.unregister(Group)

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ("date", "user", "start", "end")
    
    def has_module_permission(self, request):
        return True

    def has_add_permission(self, request):
        return True
    
    def has_change_permission(self, request, obj=None):
         return True
    


#admin.site.register(Shift, ShiftAdmin)