from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    status = models.CharField(max_length = 200, default = 'on_work')
    def __str__(self):
        return self.name
