#dev shiva gangula.
#intialized 02/11/2020
#last_edited 02/11/2020


from django.shortcuts import render
from hr_managment.models import Hr_Detailes

def Hr_registration(request):
    if request.method == 'POST':
        print('reg POST')
        return render(request, 'hr_managment/hr_login.html')
    else:
        print('reg GET')
        return render(request, 'hr_managment/hr_reg.html')


def Hr_login(request):
    if request.method == 'POST':
        print('login POST')
        return render(request, 'hr_managment/hr_dashboard.html')
    else:
        print('login GET')
        return render(request, 'hr_managment/hr_login.html')

