#dev shiva gangula.
#intialized 02/11/2020
#last_edited 04/11/2020

from hr_managment.models import *
def available_hr():
    ahr = Hr_Detailes.objects.all()
    lhr = []
    for qobject in ahr:
        tem = {}
        tem['hr_name'] = qobject.hr_name
        tem['hr_company'] = qobject.hr_company
        tem['hr_mail'] = qobject.hr_mail
        tem['hr_company_type'] = qobject.hr_company_type
        tem['hr_doj'] = qobject.doj_portal
        lhr.append(tem)
    return lhr

from integration.models import *
def notifications(student_email):
    student_status = Conversion_box.objects.filter(student_email=student_email)
    lnoti = []
    for status_details in student_status:
        tem = {}
        hr_query = Hr_Detailes.objects.get(hr_mail=status_details.hr_email)
        tem['hr_name'] = hr_query.hr_name
        tem['hr_company'] = hr_query.hr_company
        tem['hr_company_type'] = hr_query.hr_company_type
        tem['student_email'] = status_details.student_email
        tem['hr_email'] = status_details.hr_email
        tem['hr_msg'] = status_details.hr_msg
        tem['student_msg'] = status_details.student_msg
        tem['time_frame'] = status_details.time_frame
        tem['status'] = status_details.status
        lnoti.append(tem)
    return lnoti



