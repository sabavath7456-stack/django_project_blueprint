from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models. CharField(max_length=100)
    location = models.IntegerField(max_length=100, default=0)

    def __str__(self):
        return self.title

    