#dev shiva gangula.
#intialized 02/11/2020
#last_edited 02/11/2020


from django.contrib import admin
from .models import *

@admin.register(Band_Status)
class Band_StatusAdmin(admin.ModelAdmin):
    list_display = ('student_email','hr_email', 'status')


@admin.register(Conversion_box)
class Conversion_boxAdmin(admin.ModelAdmin):
    list_display = ('student_email','hr_email','time_frame')

