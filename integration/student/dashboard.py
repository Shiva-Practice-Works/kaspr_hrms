#dev shiva gangula.
#intialized 02/11/2020
#last_edited 05/11/2020

from hr_managment.models import *
from integration.models import *

def available_hr(st_email):
    hrs = Hr_Detailes.objects.all()
    hrdata = []
    for hobject in hrs:
        tem = {}
        tem['hr_name'] = hobject.hr_name
        tem['hr_company'] = hobject.hr_company
        tem['hr_email'] = hobject.hr_mail
        tem['student_email'] = st_email
        if Conversion_box.objects.filter(hr_email= hobject.hr_mail,student_email = st_email).exists():
           hr_conversions = Conversion_box.objects.get(hr_email = hobject.hr_mail,student_email = st_email)
           tem['hr_status'] = hr_conversions.status
           if hr_conversions.status == 'Accept':
              tem['hr_msg'] = hr_conversions.hr_msg
              tem['hrround'] = hr_conversions.hrround
              tem['Hrrounwillbe'] = hr_conversions.Hrrounwillbe
              d=hobject.hr_mail.split('@')
              tem['code'] = d[0]
        else:
           tem['hr_status'] = 'Request'
        hrdata.append(tem)
    return hrdata
    """
    data = [
           {'hr_name':'hrname1', *
            'hrcompany':'tcs', *
            'status':'Request/Accepted/Rejected/Pending',
            'hrmsg':'message',
            'hr_email':hr@email.com, *
            'student_email':student@email.com,
            'hr_round':'hrround',
            'round_will':date}]
    """