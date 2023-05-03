from django.urls import path
from . import views

urlpatterns = [
    path('sv/', views.studentView, name= "student_url"),
    path('cv/', views.courseView, name = "courseview_url"),
    path('showstu/', views.showstudentView, name="showstudent_url"),
    path('showcor/', views.showcourseView, name = "showcor_url"),
    path('up/<int:pk>/', views.UpdateView, name = "update_url"),
    path('dl/<int:pk>/', views.deleteView, name = "delete_url")
    
    
]
