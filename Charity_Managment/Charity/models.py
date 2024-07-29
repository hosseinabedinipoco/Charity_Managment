from django.db import models
from account.models import User
# Create your models here.

class Charity(models.Model):
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Benefactor(models.Model):
    LEVEL = (
        (0, "Bigginer"),
        (1, 'Midlevel'),
        (2, 'expert')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.SmallIntegerField(default=0, choices=LEVEL)
    free_time_per_week = models.PositiveIntegerField(default=0)

        
