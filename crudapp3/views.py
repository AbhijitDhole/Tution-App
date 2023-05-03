from django.shortcuts import render, redirect
from .models import Student, Courses
from .forms import StudentForm, CourseForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login_url')
def studentView(request):
    form = StudentForm()
    template_name = "crudapp3/add.html"
    context = {'form': form}
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courseview_url')
    return render(request, template_name, context)

@login_required(login_url='login_url')
def courseView(request):
    form = CourseForm()
    template_name = "crudapp3/course.html"
    context = {'form': form}
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("showstudent_url")       
    return render(request, template_name, context)

def showstudentView(request):
    data = Student.objects.all()
    template_name = "crudapp3/showstu.html"
    context = {'obj': data}
    return render(request, template_name, context)

def showcourseView(request):
    data = Courses.objects.all()
    template_name = "crudapp3/showcor.html"
    context = {'obj': data}
    return render(request, template_name, context)

def UpdateView(request, pk):
    obj = Student.objects.get(s_id = pk) 
    form = StudentForm(instance=obj)
    template_name = "crudapp3/add.html"
    context = {'form': form}
    if request.method == "POST":
        form = StudentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('showstudent_url')
    return render(request, template_name, context)

def deleteView(request, pk):
    obj = Student.objects.get(s_id=pk)
    template_name = "crudapp3/confirm.html"
    context = {'data': obj}
    if request.method == "POST":
        obj.delete()
        return redirect('showstudent_url')
    return render(request, template_name, context)
    
