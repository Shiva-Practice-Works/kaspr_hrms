#dev shekar 03/11/2020
#dev shiva 04/11/2020

from django.shortcuts import render
from .models import StudentRegistration
# Create your views here.
def student_register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        contact=request.POST.get('contact')
        date_of_birth=request.POST.get('date_of_birth')
        qualification=request.POST.get('qualification')
        passing_year=request.POST.get('passing_year')
        email=request.POST.get('email')
        password=request.POST.get('password')
        student=StudentRegistration(name=name,contact=contact,date_of_birth=date_of_birth,qualification=qualification,
                            passing_year=passing_year,emil=email,password=password)
        student.save()
        message='successfully registration'
        return render(request,'student_managment/registration.html',{'mesage':message})
    else:
        return render(request, 'student_managment/registration.html')

from integration.student.dashboard import available_hr
def student_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        login=StudentRegistration.objects.filter(emil=email,password=password)
        if login:
            data = {'hr_details':available_hr(email),
                    'student_email':email,
                    }
            return render(request,'student_managment/home.html',data)
    else:
        return render(request,'student_managment/student_login.html')
    message = 'invalid email or password'
    return render(request,'student_managment/student_login.html',{'mesage':message})

