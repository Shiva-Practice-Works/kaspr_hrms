#dev shiva gangula.
#intialized 02/11/2020
#last_edited 04/11/2020

from django.shortcuts import render, HttpResponse
from integration.models import Conversion_box
from integration.student import dashboard
import datetime


def home(request):
    return render(request, 'integration/home.html')


from django.http import JsonResponse



def hr_student_conversions(request):
    out = """ <html><head>
                <meta http-equiv="refresh" content="3;url=/su/student_login_details/" />
                </head><body>
                <h6>{}</h6>
                </body></html>
                """
    if request.method == "POST":
        student_email = request.POST['student_email']
        hr_email = request.POST['hr_email']
        student_msg = request.POST['student_msg']
        if Conversion_box.objects.filter(student_email =student_email, hr_email=hr_email).exists():
            
            return  HttpResponse(out.format('You Already Made Request See in Notifications'))
        else:
            qdata = Conversion_box(student_email=student_email, 
                                   hr_email=hr_email,
                                   student_msg = student_msg,
                                   hr_msg = 'Pending',
                                   time_frame = datetime.datetime.now(),
                                   status='Pending')
            qdata.save()
            return HttpResponse(out.format('requested sucessfully'))
    else:
        pass
def hr_request_accept_reject(request):
    out = """ <html><head>
                <meta http-equiv="refresh" content="3;url=/hrm/hrl/"/>
                </head><body>
                <h3>{}</h3>
                </body></html>
                """
    if request.method == "POST":
        student_email = request.POST['student_email']
        hr_email = request.POST['hr_email']
        status = request.POST['status']
        if Conversion_box.objects.filter(student_email =student_email, hr_email=hr_email,status='Pending').exists():
            if status == 'Accept':
              hrround = request.POST['round']
              hrmsg = request.POST['message']
              hrrounddate = request.POST['rounddate']
              Conversion_box.objects.filter(student_email =student_email, hr_email=hr_email).update(
                                                             status='Accept',
                                                             hr_msg=hrmsg,
                                                             hrround=hrround,
                                                             Hrrounwillbe=hrrounddate)
              return HttpResponse(out.format('You Accepted Student request'))
            else:
              Conversion_box.objects.filter(student_email =student_email, hr_email=hr_email).update(status='Rejected')
              return HttpResponse(out.format('You Rejected Student request'))
        else:
           return HttpResponse(out.format('Sometihng went Wrong'))