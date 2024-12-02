from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),  # ให้ URL '/' ชี้ไปที่ views.course_list
]
