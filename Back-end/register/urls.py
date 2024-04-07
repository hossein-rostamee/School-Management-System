from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

app_name = "register"

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    path("list/<str:op>/<int:vln_id>/<str:username>/<str:password>/", views.listVolunteers, name="volunteers"),
    path("login/", views.login , name="login"),
    path('download/personelPhoto/<int:id>/<str:object>/<str:username>/<str:password>/', views.download_image_personelPhoto, name='download_image_personelPhoto'),
    path('download/birthCertificate/<int:id>/<str:object>/<str:username>/<str:password>/', views.download_image_birthCertificate, name='download_image_birthCertificate'),
    path('classesId/<str:username>/<str:password>/', views.getClassIds, name='getClassIds' ), 
    path('register_student/<str:username>/<str:password>/', views.registerStudent, name='register_student' ),
    path('liststu/<str:op>/<int:stu_id>/<str:username>/<str:password>/', views.listStudents, name='list_students'), 
    path('deleteuser/<str:userid>/<str:username>/<str:password>/', views.delete_user, name='deleteuser'), 
    path('listclass/<str:username>/<str:password>/', views.listClasses, name='listClasses'), 
    path('listclass/changeClass/<str:username>/<str:password>/', views.changeClass, name='changeClass'), 
    path('studentInfo/<str:username>/<str:password>/', views.studentInfo, name='studentInfo'), 
    path('classInfo/<str:username>/<str:password>/', views.classInfo, name='classInfo'), 
]   


router = routers.DefaultRouter()
router.register(r'', views.VolunteerView, 'list')

router_student = routers.DefaultRouter()
router_student.register(r'', views.StudentView, 'liststu')


