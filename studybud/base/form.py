from django import forms
# from base.models import Employee

# class Student(forms.Form):
#     first_name = forms.CharField(label = "Enter First Name",max_length=20)
#     last_name = forms.CharField(label="Enter Last Name", max_length=30)


# class EmployeeForm(forms.ModelForm):
#     class Meta:
#         model = Employee
#         fields = "__all__"


class StudentForm(forms.Form):
      firstname = forms.CharField(label="Enter first name",max_length=50)  
      lastname  = forms.CharField(label="Enter last name", max_length = 10)  
      email     = forms.EmailField(label="Enter Email")  
      