from django.contrib import admin
from .models import *



@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name','company_mail', 'company_number')


@admin.register(Hr_Detailes)
class Hr_DetailesAdmin(admin.ModelAdmin):
    list_display = ('hr_name','hr_company','hr_number')


