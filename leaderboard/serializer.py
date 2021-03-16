from django.db.models import fields
from rest_framework import serializers
from .models import Leaderboard, Player

class LeaderBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = "__all__"