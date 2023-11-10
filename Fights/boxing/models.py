from django.db import models

# Create your models here.

class Fighters(models.Model):
    first_name = models.CharField(max_length=24)
    initial = models.CharField(max_length=1, blank=True)
    last_name = models.CharField(max_length=24)
    
    def __str__(self):
        return f"{self.first_name} {self.initial} {self.last_name}"
    
    