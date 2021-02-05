from django.db import models
from django.shortcuts import render
# Create your models here.


class Signup(models.Model):

    user_id = models.CharField('user_id', max_length=20)
    user_pw = models.CharField('user_pw', max_length=20)
    email = models.CharField('email', max_length=30)

    def __str__(self):
        return self.user_id


