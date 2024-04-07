from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Users)
admin.site.register(Volunteer)
admin.site.register(Class)
admin.site.register(Student)