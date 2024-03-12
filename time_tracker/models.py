from django.db import models
from datetime import datetime


class Task(models.Model):
    name = models.CharField(max_length=200)
    timestamp = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length = 200, default = 'on_work')
    def __str__(self):
        return self.name
