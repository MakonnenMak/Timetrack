from django.db import models
from timelog.models import Timelog
from users.models import User


class Category(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="User")

    def __str__(self):
        return f"Category title: {self.title}"


class Event(models.Model):
    # Foreign keys
    timelog = models.ForeignKey(
        Timelog, on_delete=models.CASCADE, default='Timelog')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="User")
    # Time attributes
    date = models.DateField(True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    # Helper
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.description
