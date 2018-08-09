from django.contrib import admin

# Register your models here.
from django.contrib import admin
from icazeler.models import Attend
class AttendAdmin(admin.ModelAdmin):
    

    list_display = ['user','leave_type', 'leave_start', 'leave_end','status']

    class Meta:
        model = Attend
  
admin.site.register(Attend,AttendAdmin)
