from django.db import models
from django.utils.timezone import now

class Task(models.Model):
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=250)
    due_date = models.DateField(default=now)
    status = models.TextField(max_length=100, default='Due Today')    