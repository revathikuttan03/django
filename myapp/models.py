from django.db import models 

# Create your models here.

class TaskList(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=100,default="pending")
    def __str__(self):
        return self.name