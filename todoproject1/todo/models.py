from django.db import models

# Create your models here.

class Task(models.Model):
    # An ID field is automatically added to all Django models unless we tell it otherwise
    description = models.CharField(max_length=255)
