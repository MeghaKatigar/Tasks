from django.db import models

# Create your models here.
class Task(models.Model):

    class TaskStatusChoices(models.TextChoices):
        CREATED = "CR", "created"
        IN_PROGRESS = "IP", "in_progress"
        COMPLETED = "CP", "completed"

    task_name = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=TaskStatusChoices, default=TaskStatusChoices.CREATED)
    target_date = models.DateField(null=True)
    completed_at = models.DateTimeField(null=True) 