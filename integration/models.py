#dev shiva gangula.
#intialized 02/11/2020
#last_edited 04/11/2020


from django.db import models

#table for handling msg from students
class Conversion_box(models.Model):
     student_email  = models.EmailField(max_length=100)
     hr_email = models.EmailField(max_length=100)
     student_msg = models.CharField(max_length=180) #do not exceed more then 180 char
     hr_msg = models.CharField(max_length=180) #do not exceed more then 180 char
     time_frame = models.DateTimeField()
     status = models.CharField(max_length=100)
     def __str__(self):
        return self.status
