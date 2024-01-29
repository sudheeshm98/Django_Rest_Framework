from django.db import models

# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length=250)
    phone_num = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=300)

