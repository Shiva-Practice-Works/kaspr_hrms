
#dev shiva gangula.
#intialized 02/11/2020
#last_edited 02/11/2020

from django.contrib import admin
from django.urls import path ,include
from integration.views import home



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('hrm/',include('hr_managment.urls')), 
    path('su/',include('student_managment.urls')), 
    path('inti/',include('integration.urls')), 
]
