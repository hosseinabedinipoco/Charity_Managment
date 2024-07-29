from django.db import models
from account.models import User
# Create your models here.

class Charity(models.Model):
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
