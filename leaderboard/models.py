from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import PositiveIntegerField

# Create your models here.
class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    playername = models.CharField(max_length=30)
    highscore_arcade = models.PositiveIntegerField(default=0)
    car = models.PositiveSmallIntegerField(default=0)
    coins = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.playername

class Highscore(models.Model):
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    score = PositiveIntegerField()

    def __str__(self):
        return self.player + self.score
    
    


class Leaderboard(models.Model):
    leaderboard_name = models.CharField(max_length=100)
    nr_of_players = models.PositiveIntegerField(default=0)
    highscores = models.ManyToManyField(Highscore, blank=True)

    def __str__(self):
        return self.leaderboard_name
    

    