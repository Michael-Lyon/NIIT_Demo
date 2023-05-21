from django.contrib import admin
from . models import Classroom, Class, Schedule
# Register your models here.
admin.site.register(Class)
admin.site.register(Classroom)
admin.site.register(Schedule)