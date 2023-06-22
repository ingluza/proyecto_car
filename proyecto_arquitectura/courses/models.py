from django.db import models
from teachers.models import Teacher


class Course(models.Model):
    name = models.CharField(max_length=240)
    teacher_id = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)
    description = models.TextField( null=True)
    rating = models.CharField( null=True)


    def __str__(self):
        
        return f'{self.name} | {self.description} '