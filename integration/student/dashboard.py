#dev shiva gangula.
#intialized 02/11/2020
#last_edited 03/11/2020

from hr_managment.models import *
def available_hr():
    ahr = Hr_Detailes.objects.all()
    lhr = []
    for qobject in ahr:
        tem = {}
        tem['hr_name'] = qobject.hr_name
        tem['hr_company'] = qobject.hr_company
        tem['hr_company_type'] = qobject.hr_company_type
        tem['hr_doj'] = qobject.doj_portal
        lhr.append(tem)
    return lhr


def notifications(student_email):
    pass #return availble noftications
    """
    notification = [{'hr_name':rahul,'hr_status':'Pending'},
                    {'hr_name':ganesh,'hr_status':'Active'},
                    {'hr_name':siri,'hr_status':'Rejected'}]
    """

def hr_profile(hr_mail):
    pass #return hr details

