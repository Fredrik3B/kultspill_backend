from rest_framework import serializers
from .models import Highscore, Leaderboard, Player

class HighscoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Highscore
        fields = ["score", "player"]

class LeaderBoardSerializer(serializers.ModelSerializer):
    highscores = HighscoreSerializer(many=True, read_only=True)
    class Meta:
        # ordering = ["highscores.score"]
        model = Leaderboard
        fields = ["leaderboard_name", "highscores"]