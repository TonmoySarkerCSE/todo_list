from django.db import models

# Create your models here.
class TaskModel(models.Model):
    task_title = models.CharField(max_length=64, verbose_name='Task Title')
    task_description = models.TextField()
    is_completed = models.BooleanField(default=False)