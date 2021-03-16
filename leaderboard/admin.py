from django.contrib import admin
from .models import Leaderboard, Player, Highscore

# Register your models here.
admin.site.register(Highscore)
admin.site.register(Player)
admin.site.register(Leaderboard)