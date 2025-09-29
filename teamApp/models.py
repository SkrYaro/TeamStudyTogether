from django.db import models

# Create your models here.

class ClassModel(models.Model):
    name = models.CharField(max_length=123)
    num = models.IntegerField()

    def __str__(self):
        return self.name

