#dev shiva gangula.
#intialized 02/11/2020

from django.db import models

#table for intrested company's on portal
class Company(models.Model):
	company_uniq_portal_id = models.CharField(max_length=100)
	company_name = models.CharField(max_length=100)
	company_location = models.CharField(max_length=100)
	company_pincode = models.CharField(max_length=100)
	company_mail = models.EmailField()
	company_number = models.IntegerField()
	company_type = models.CharField(max_length=100)
	company_gstin = models.CharField(max_length=100)
	doj_portal = models.CharField(max_length=100) #date of joining on portal
	def __str__(self):
		return self.company_name


#table for intrested hr's on portal
class Hr_Detailes(models.Model):
    hr_uniq_portal_id = models.CharField(max_length=100)
    hr_name = models.CharField(max_length=100)
    hr_company = models.CharField(max_length=100) #relation with company
    hr_mail = models.EmailField()
    hr_dob = models.DateField()
    hr_number = models.IntegerField()
    hr_joining_date = models.DateField()
    doj_portal = models.CharField(max_length=100) #date of joining on portal
    def __str__(self):
    	return self.hr_name

