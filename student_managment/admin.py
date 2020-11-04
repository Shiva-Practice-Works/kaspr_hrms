#dev shiva 04/11/2020

from django.contrib import admin
from .models import *

@admin.register(StudentRegistration)
class StudentRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name','contact','emil')


