from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Sports(models.Model):
    sport = models.CharField(max_length=48)

    def __str__(self):
        return f"{self.sport}"

class Teams(models.Model):
    team_name = models.CharField(max_length=48)
    sport = models.ForeignKey(Sports, on_delete=models.CASCADE, related_name="team_sport")

    def __str__(self):
        return f"{self.team_name}, {self.sport}"



class Players(models.Model):
    first_name = models.CharField(max_length=24)
    middle = models.CharField(max_length=1)
    last_name = models.CharField(max_length=24)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name="team")

    def __str__(self):
        return f"{self.first_name} {self.middle} {self.last_name} part of {self.team}"


    