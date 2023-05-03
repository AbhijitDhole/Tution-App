from django import forms
from .models import Student, Courses

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        labels = {
            's_id':'Student ID:',
            'name': 'Student Name:',
            'dob': 'Date of Birth',
            'address':'Address'
        }
        
class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = "__all__"
        labels = {
            'Student':'Student Info:',
            'c_name': 'Course Name',
            'c_fees':'Course Fees',
            'date':'Date of admission:'
        }