from django.forms import ModelForm
from .models import *
from django import forms


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee

        fields = ['employee_name','employee_address', 'employee_email', 'employee_startdate', 'employee_enddate','employee_image','status']
        widgets = {
            'employee_name': forms.TextInput(attrs={'class': 'form-control'}),
            'employee_address': forms.Textarea(attrs={'class': 'form-control'}),
            'employee_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'employee_startdate': forms.DateInput(format=('%y/%m/%d'),attrs={'class': 'form-control', 'type': 'date'}),
            'employee_enddate': forms.DateInput(format=('%y/%m/%d'),attrs={'class': 'form-control', 'type': 'date'}),
            'employee_image': forms.FileInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

        def clean(self):
            pass