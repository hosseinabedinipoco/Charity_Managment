from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):

    GENDER = (
        ('f', 'famale'),
        ('m', 'male')
    )

    address = models.TextField(null=True)
    age = models.PositiveSmallIntegerField(null=True)
    description = models.TextField(null=True)
    email = models.EmailField(null=True)
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=1, choices=GENDER, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True)
    last_name = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=11, null=True)
    username = models.CharField(max_length=20, unique=True)