from __future__ import unicode_literals
from django.db import models
import re
import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors["name"] = "Your name is too short"
        elif not postData['name'].isalpha():
            errors["first_alpha"] = "No numbers allowed"
        if len(postData['username']) < 3:
            errors["username"] = "Your Username is too short"
        elif not postData['username'].isalpha():
            errors["last_alpha"] = "No numbers allowed"
        if len(postData['password']) < 8:
            errors["password"] = "Password is too short"
        if postData['password'] != postData['confirm']:
            errors["confirmation"] = "Your passwords don't match"
        return errors

class TravelManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['destination']) < 1:
            errors["destination"] = "Aren't you going somewhere?"
        if len(postData['startdate']) < 1:
            errors["startdate"] = "You need a startdate"
        if len(postData['enddate']) < 1:
            errors["enddate"] = "So you're never coming bakc?"
        if len(postData['plans']) < 3:
            errors["plans"] = "So you're not doing anything while you're there?"
        return errors



class User(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()


class Travel(models.Model):
    destination = models.CharField(max_length=1000)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    plans = models.CharField(max_length=1000)
    user = models.ForeignKey (User, related_name="user_travel", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = TravelManager()

