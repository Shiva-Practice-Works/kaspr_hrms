from django.contrib import admin
from .models import *


@admin.register(Hr_Detailes)
class Hr_DetailesAdmin(admin.ModelAdmin):
    list_display = ('hr_name','hr_company','hr_number')


