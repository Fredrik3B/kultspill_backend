from django.contrib import admin
from .models import Leaderboard, Player

# Register your models here.
admin.site.register(Leaderboard)
admin.site.register(Player)