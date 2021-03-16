from leaderboard.models import Highscore
from django.urls import path
from .views import LeaderboardView, HighscoreView

urlpatterns = [
    path("leaderboards/<int:pk>/", LeaderboardView.as_view(), name="leaderboards"),
    path("highscore/<int:pk>/", HighscoreView.as_view(), name="leaderboards")
]