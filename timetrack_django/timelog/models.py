from django.db import models
from users.models import User


class Timelog(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=120)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="User")

    def __str__(self):
        return f"Timelog: {self.name}"
