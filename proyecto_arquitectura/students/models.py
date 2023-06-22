from django.db import models

from users.models import User


class Student(models.Model):
    identification = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    email = models.EmailField()
    cellphone = models.CharField(max_length=15, default=None)
    birth_date = models.DateField()
    address = models.CharField(max_length=240)


    def __str__(self):
        """Return company and first_name and last_name."""
        return f'{self.name} {self.last_name} '