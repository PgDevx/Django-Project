from django.db import models
from django.contrib.auth.models import User

class Bank(models.Model):
    name = models.OneToOneField(User, default="", on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    account_number = models.CharField(max_length=20)
    account_balance = models.CharField(max_length=100)

    def __str__(self):
        return self.name.__str__()

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    desc = models.TextField()

    def __str__(self):
        return self.name
