from django.contrib.auth.models import User
from django.db import models


class RegisteredUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Results(models.Model):
    ft3 = models.FloatField(null=True)
    ft4 = models.FloatField(null=True)
    tsh = models.FloatField(null=True)
    mat = models.FloatField(null=True)
    tat = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    user = models.ForeignKey(RegisteredUser, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.date_created}"
