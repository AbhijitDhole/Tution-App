from django.urls import path
from . import views
urlpatterns = [
    path('reg/', views.signUpview, name = "signup_url"),
    path('login/', views.loginView, name= "login_url"),
    path('logout/', views.logoutView, name= "logout_url")
]
