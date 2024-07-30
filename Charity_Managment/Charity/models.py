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

class TaskManager(models.Manager):
    def related_tasks_to_charity(self, user):
        return self.filter(charity__user=user)

    def related_tasks_to_benefactor(self, user):
        return self.filter(assigned_benefactor__user=user)
    

class Task(models.Model):
    GENDER = (
        ('f', 'famale'),
        ('m', 'male')
    )
    STATUS = (
        ('P', 'pending'),
        ('W', "waited"),
        ('A', 'assigend'),
        ('D', 'done'),
    )
    assigned_benefactor = models.ForeignKey(Benefactor, on_delete=models.DO_NOTHING, null=True)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    age_limit_from = models.IntegerField(null=True)
    age_limit_to = models.IntegerField(null=True)
    date = models.DateField()
    description = models.TextField(null=True)
    gender_limit = models.CharField(max_length=1, null=True, choices=GENDER)
    state = models.CharField(max_length=1, default='P', choices=STATUS)
    title = models.CharField(max_length=60)
    objects = TaskManager()
       