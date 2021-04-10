from django.db import models
import uuid

# Create your models here.

class Employee(models.Model):
    employee_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee_name = models.CharField(max_length=30)
    employee_address = models.CharField(max_length=250)
    employee_email = models.EmailField()
    employee_startdate = models.DateField()
    employee_enddate = models.DateField()
    employee_image = models.ImageField(upload_to='uploads/emp', null=True, blank=True)
    action=(('1','Active'),
            ('2','Terminated'),
            ('3','Temporary'),
            ('4','On Notice Period'))
    status=models.CharField(max_length=30,choices=action)


    def __str__(self):
        return self.employee_name
