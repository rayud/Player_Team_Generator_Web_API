## /////////////////////////////////////////////////////////////////////////////
## YOU CAN FREELY MODIFY THE CODE BELOW IN ORDER TO COMPLETE THE TASK
## /////////////////////////////////////////////////////////////////////////////

from django.http.response import JsonResponse
from rest_framework.request import Request
from rest_framework import status
from typing import Any
from my_app.models.player import Player
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes


def delete_player_handler(request: Request, id: Any):
    
    try: 
        player = Player.objects.get(id=id)
    except Player.DoesNotExist:
        return JsonResponse("Player not existed", status=status.HTTP_404_NOT_FOUND, safe=False)
    player.delete()
    return JsonResponse('Player Deleted', status=status.HTTP_204_NO_CONTENT, safe=False)