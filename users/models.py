from django.contrib.auth.models import User
from django.db import models


class RegisteredUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Results(models.Model):
    results_type = models.CharField(max_length=3, null=True)

    def __str__(self):
        return self.results_type


class ImportedResults(models.Model):
    user = models.ForeignKey(RegisteredUser, null=True, on_delete=models.CASCADE)
    results = models.ForeignKey(Results, null=True, on_delete=models.CASCADE)
    result_value = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user} - {self.results} - {self.result_value} - {self.date_created}'

