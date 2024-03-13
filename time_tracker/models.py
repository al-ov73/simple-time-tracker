from django.db import models
from django.utils import timezone
import pytz


class Task(models.Model):
    name = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length = 200, default = 'on_work')
    timespend = models.CharField(max_length = 200, null = True)
    
    def __str__(self):
        return self.name
