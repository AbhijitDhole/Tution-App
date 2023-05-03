from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login , logout
# Create your views here.

def signUpview(request):
    form = UserCreationForm()
    template_name = 'authapp3/register.html'
    context = {'form': form}
    if request.method =="POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    return render(request, template_name, context)

def loginView(request):
    template_name = "authapp3/login.html"
    context = {}
    if request.method =="POST":
        u= request.POST.get('un')
        p = request.POST.get('pw')
        user=authenticate(username= u, password=p)
        if user is not None:   #it returns None if the user is not registered
            login(request, user)
            return redirect('showstudent_url')
    return render(request, template_name, context)

def logoutView(request):
    logout(request)
    return redirect('login_url')