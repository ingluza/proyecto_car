from django.db import models
from students.models import Student
from courses.models import Course


class Qualification(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.DecimalField(null=True, max_digits=3, decimal_places=2)


    def __str__(self):
        
        return f'{self.student_id.name} | {self.course_id.name} | {self.score} '