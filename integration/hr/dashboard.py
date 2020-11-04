from integration.models import *
from student_managment.models import * 

def availeble_requests(hr_mail):
    avre = Conversion_box.objects.filter(hr_email=hr_mail,status='Pending')
    avre_out = []
    for i in avre:
        student_details = StudentRegistration.objects.filter(emil=i.student_email)
        for j in student_details:
            tem = {}
            tem['student_msg'] = i.student_msg
            tem['student_name'] = j.name
            tem['student_contact'] = j.contact
            tem['student_dob'] = j.date_of_birth
            tem['student_quali'] = j.qualification
            tem['student_pass_year'] = j.passing_year
            tem['student_email'] = j.emil
            avre_out.append(tem)
    return avre_out
        