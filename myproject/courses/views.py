from django.shortcuts import render
from .models import Course

def course_list(request):
    courses = Course.objects.all()  # ดึงข้อมูลรายวิชาทั้งหมดจากฐานข้อมูล
    return render(request, 'courses/course_list.html', {'courses': courses})
