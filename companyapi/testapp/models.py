from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager


class User(models.Model):
    username=None
    email = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    is_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=500, null=True, blank=True)
    forget_password = models.CharField(max_length=500, null=True, blank=True)
    last_login_time = models.DateTimeField(null=True, blank=True)
    last_logout_time = models.DateTimeField(null=True, blank=True)

    objects=UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    about = models.TextField()
    type = models.CharField(max_length=500,choices=(('IT','IT'),
                                                   ('NON IT','NON IT'),('MOBILES PHONE','MOBILE PHONE')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + '--' + self.location


    #Employee Model
class Employee(models.Model):
        name = models.CharField(max_length=500)
        email = models.CharField(max_length=500)
        address = models.CharField(max_length=500)
        phone = models.CharField(max_length=500)
        about = models.TextField()
        position = models.CharField(max_length=500,choices=(('Manager','Manager'),
                                                       ('software Developer','SD'),('Project Leader','PL')))

        company=models.ForeignKey(Company, on_delete=models.CASCADE)
