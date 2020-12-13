from datetime import date
from django.core.exceptions import ValidationError
from django.db import models
from phone_field import PhoneField
from django.utils.translation import gettext_lazy as _


def no_future(value):
    today = date.today()
    if value > today:
        raise ValidationError('Date cannot be in the future.')


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.CharField(max_length=8, unique=True)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, unique=True)
    phone = PhoneField(blank=True)
    address = models.CharField(max_length=400)
    birth_date = models.DateField(validators=[no_future])

    def __str__(self):
        return self.first_name+' '+self.last_name


class Course(models.Model):

    class Degree(models.TextChoices):
        BACHELOR = 'BACH', _('Bachelor')
        MASTER = 'MAST', _('Master')
        DOCTORATE = 'DOCT', _('Doctorate')

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=8, unique=True)
    credit = models.PositiveSmallIntegerField()
    type = models.CharField(max_length=4, choices=Degree.choices, default=Degree.BACHELOR)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
