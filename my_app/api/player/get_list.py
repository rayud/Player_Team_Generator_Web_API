## /////////////////////////////////////////////////////////////////////////////
## YOU CAN FREELY MODIFY THE CODE BELOW IN ORDER TO COMPLETE THE TASK
## /////////////////////////////////////////////////////////////////////////////

from django.http.response import JsonResponse
from rest_framework.request import Request
from rest_framework import status
from my_app.models import player
from my_app.serializers.player import PlayerSerializer


def get_player_list_handler(request: Request):
    list_of_players = player.Player.objects.all()
    serializer = PlayerSerializer(list_of_players, many=True)
    print(serializer.data)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
