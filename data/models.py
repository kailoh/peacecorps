from django.db import models
from django_options import *
from django.contrib import admin

class Volunteer(models.Model):
    first_name = models.CharField(max_length = 48)
    last_name = models.CharField(max_length = 48)
    home_state = models.CharField(max_length = 2, choices = STATES)
    country = models.CharField(max_length = 2, choices = COUNTRY_NAME_CHOICES, verbose_name = "country of service")
    sector = models.CharField(max_length = 2, choices = SECTORS, verbose_name = "sector of service")
    start_date = models.DateField(verbose_name = "start date of service")
    end_date = models.DateField(verbose_name = "end date of service")
    email = models.EmailField(verbose_name = "email address")
    language = models.CharField(max_length = 48, verbose_name = "primary language of communication in the field")
    keywords = models.CharField(max_length = 2, choices = KEYWORDS, verbose_name = "list of keywords")


class Teacher(models.Model):
    first_name = models.CharField(max_length = 48)
    last_name = models.CharField(max_length = 48)
    school = models.CharField(max_length = 48, verbose_name = "School name")
    city = models.CharField(max_length = 80, verbose_name = "City")
    state = models.CharField(max_length = 2, verbose_name = "state", choices = STATES)
    zip = models.IntegerField(verbose_name = "zipcode")
    phone = models.CharField(max_length=15, verbose_name="work phone")
    email = models.EmailField(verbose_name = "email address")
    grade = models.CharField(max_length = 2, choices=GRADES, verbose_name = "grade of students")
    num_students = models.IntegerField(verbose_name = "number of students")
    keywords = models.CharField(max_length = 2, choices = KEYWORDS, verbose_name = "list of keywords")

admin.site.register(Teacher)
admin.site.register(Volunteer)