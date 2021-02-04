from django.db import models

# Create your models here.


class Signup(models.Model):
    user_id = models.CharField('user_id', max_length=20)
    user_pw = models.CharField('user_pw', max_length=20)

    def __str__(self):
        return self.user_id

