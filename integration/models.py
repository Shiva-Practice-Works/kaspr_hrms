#dev shiva gangula.
#intialized 02/11/2020
#last_edited 02/11/2020

from django.db import models

#table for hr and student acepet ,rejection table
class Band_Status(models.Model):
    student_uniq_portal_id = models.CharField(max_length=100)
    hr_uniq_portal_id = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    def __str__(self):
        return self.status


#table for handling msg from students( before accept student request ) 
class Conversion_box(models.Model):
     student_uniq_portal_id  = models.CharField(max_length=100)
     hr_uniq_portal_id = models.CharField(max_length=100)
     student_msg = models.CharField(max_length=180) #do not exceed more then 180 char
     hr_msg = models.CharField(max_length=180) #do not exceed more then 180 char
     time_frame = models.DateTimeField()
     def __str__(self):
        return self.time_frame
