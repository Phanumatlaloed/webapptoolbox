from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)  # ชื่อรายวิชา
    code = models.CharField(max_length=10)  # รหัสรายวิชา
    description = models.TextField()  # รายละเอียดของวิชา
    credits = models.IntegerField()  # จำนวนหน่วยกิต

    def __str__(self):
        return self.name
