from django.contrib import admin
from classes.models import ClassSession,CoachClasses,ClientsAttendance,Days
# Register your models here.
admin.site.register(ClassSession)
admin.site.register(CoachClasses)
admin.site.register(ClientsAttendance)
admin.site.register(Days)
