from django.http import Http404
from leaderboard.models import Leaderboard
from .serializer import LeaderBoardSerializer

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class LeaderboardView(APIView):
    def get_object(self, pk):
        try:
            return Leaderboard.objects.get(pk=pk)
        except Leaderboard.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        leaderboard = self.get_object(pk)
        serializer = LeaderBoardSerializer(leaderboard)
        return Response(serializer.data)
