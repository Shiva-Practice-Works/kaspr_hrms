#dev shiva gangula.
#intialized 02/11/2020
#last_edited 03/11/2020

from django.db import models


#table for intrested hr's on portal
class Hr_Detailes(models.Model):
    hr_uniq_portal_id = models.CharField(max_length=100)
    hr_name = models.CharField(max_length=100)
    hr_company = models.CharField(max_length=100) 
    hr_company_type = models.CharField(max_length=100)
    hr_mail = models.EmailField()
    hr_password = models.CharField(max_length=100)
    hr_number = models.IntegerField()
    doj_portal = models.CharField(max_length=100) #date of joining on portal
    def __str__(self):
    	return self.hr_name

