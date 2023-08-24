from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Trainer(models.Model):

    department_options = (('backend', 'Backend'),
                          ('frontend', 'Frontend'),
                          ('network', 'Network'))

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    course = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    department = models.CharField(max_length=10, choices=department_options)
    active = models.BooleanField(default=True)
    profile = models.ImageField(upload_to='profiles/', blank=True, null=True) #se poate pune si default = 'default.jpg', dar nu e neaparat nevoie. cred ca incarca baza de date aiurea...

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class HistoryTrainer(models.Model):
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.message