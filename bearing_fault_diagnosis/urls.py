# filepath: /d:/Arjun/project/bearing-fault-diagnosis/bearing_fault_diagnosis/urls.py
from django.contrib import admin
from django.urls import path
from .views import index, diagnose
from bearing_fault_diagnosis import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('diagnose/', diagnose, name='diagnose'),
    path('savecontact/',views.savecontact, name='savecontact'),
]