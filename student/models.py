from django.contrib.auth.models import User
from django.db import models

from trainer.models import Trainer


# Create your models here.


class Student(models.Model):

    gender_options = (
        ("male","MALE"),
        ("female","FEMALE")
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(max_length=100)
    description = models.TextField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)
    gender = models.CharField(max_length=6, choices=gender_options)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)
    profile = models.ImageField(upload_to='profiles_student/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    #auto_now_add = stocheaza data si ora cand a fost adaugata inregistrarea. nu se mai modifica
    #auto_now = stocheaza data si ora cand a fost adaugata inregistrarea. se modifica dara atunci cand se fac modificari pe inregistrare.

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class HistoryStudent(models.Model):
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.message