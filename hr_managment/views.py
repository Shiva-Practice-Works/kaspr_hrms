#dev shiva gangula.
#intialized 02/11/2020
#last_edited 04/11/2020


from django.shortcuts import render
from hr_managment.models import Hr_Detailes
from .models import *
import datetime

def Hr_registration(request):
    if request.method == 'POST':
        hrname = request.POST['hrname']
        hrcompany = request.POST['hrcompany']
        hremail = request.POST['hremail']
        hrpassword = request.POST['hrpassword']
        hrctype = request.POST['hrctype']
        hrmobile = request.POST['hrmobile']
        if Hr_Detailes.objects.filter(hr_mail=hremail).exists():
            data = {'method':'post','status':'Email already existed','code':'error'}
            return render(request, 'hr_managment/hr_reg.html',data)
        else:
            query = Hr_Detailes( hr_name =hrname,
                            hr_company =  hrcompany,
                            hr_company_type = hrctype,
                            hr_mail = hremail,
                            hr_password = hrpassword,
                            hr_number = hrmobile,
                            doj_portal = datetime.datetime.now())
            query.save()
            data = {'method':'post','status':'Details saved sucessfully','code':'ok'}
            return render(request, 'hr_managment/hr_reg.html',data)
    else:
        data = {'method':'get'}
        return render(request, 'hr_managment/hr_reg.html',data)

from integration.hr.dashboard import availeble_requests
def Hr_login(request):
    if request.method == 'POST':
        hremail = request.POST['hremail']
        hrpassword = request.POST['hrpassword']
        if Hr_Detailes.objects.filter(hr_mail=hremail,hr_password = hrpassword,).exists():
            data = {'a_requ':availeble_requests(hremail),'hr_email':hremail}
            return render(request, 'hr_managment/hr_dashboard.html',data)
        else:
            data = {'method':'post','status':'Email Or Password Wrong','code':'error',}
            return render(request, 'hr_managment/hr_login.html',data)
    else: 
        return render(request, 'hr_managment/hr_login.html')

