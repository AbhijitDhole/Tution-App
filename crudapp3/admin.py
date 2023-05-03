from django.contrib import admin
from .models import Student, Courses

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display= ['s_id', 'name', 'dob', 'address']
admin.site.register(Student, StudentAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = [ 'c_name', 'c_fees', 'date']
admin.site.register(Courses, CourseAdmin)