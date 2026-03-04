"""
URL configuration for reviews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin-panel/', admin.site.urls),  # changed here
    path('', views.home, name='home'),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("student-register/", views.student_register, name="student_register"),
    path('reviews/<int:course_id>/', views.course_reviews, name='course_reviews'),
    path('login/', views.student_login, name='student_login'),
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    path('feedback/', views.student_feedback, name='student_feedback'),
    path('logout/', views.student_logout, name='student_logout'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-students/', views.admin_students, name='admin_students'),
    path('admin-trainers/', views.admin_trainers, name='admin_trainers'),
    path('admin/trainers/add/', views.add_trainer, name='add_trainer'),
    path('admin-courses/', views.admin_courses, name='admin_courses'),
    path('admin/courses/add/', views.add_course, name='add_course'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('admin-feedback/', views.admin_feedback, name='admin_feedback'),
    path("add-student/", views.add_student, name="add_student"),
    path('admin/students/edit/<int:id>/', views.edit_student, name='edit_student'),
    path('admin/students/delete/<int:id>/', views.delete_student, name='delete_student'), 
    path('admin/questions/', views.admin_questions, name='admin_questions'),
    path('admin/questions/add/', views.add_question, name='add_question'),
    path('student-login/', views.student_login, name='student_login'),
]    

