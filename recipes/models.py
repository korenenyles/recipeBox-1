from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chef(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField('Recipe', symmetrical=False, related_name='favorites', default=None, blank=True)
    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=30)
    instructions = models.TextField()
    

    def __str__(self):
        return self.title


