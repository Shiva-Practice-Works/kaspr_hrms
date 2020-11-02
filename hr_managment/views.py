from django.shortcuts import render
from hr_managment.models import Hr_Detailes

def Hr_registration(request):
   return render(request, 'hr_managment/hr_reg.html')


def Hr_login(request):
   return render(request, 'hr_managment/hr_login.html')



def Hr_dashboard(request):
   return render(request, 'hr_managment/hr_login.html')