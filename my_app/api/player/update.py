## /////////////////////////////////////////////////////////////////////////////
## YOU CAN FREELY MODIFY THE CODE BELOW IN ORDER TO COMPLETE THE TASK
## /////////////////////////////////////////////////////////////////////////////

from django.http.response import JsonResponse
from rest_framework.request import Request
from rest_framework import status
from typing import Any
from my_app.models.player import Player
from my_app.serializers.player import PlayerSerializer

def update_player_handler(request: Request, id: Any):
    if request.data.get('position') not in  ['defender', 'midfielder','forward']:
        message = 'Invalid value for position: ' + str(request.data.get('position'))

        return JsonResponse({'message': message}, status=status.HTTP_400_BAD_REQUEST)
    else : 
        for skill in request.data.get('playerSkills'):
            if skill['skill'] not in ['defense', 'attack', 'speed', 'strength', 'stamina']:
                message = 'Invalid value for position: ' + str(skill['skill'])
                return JsonResponse({'error': 'Invalid skill'}, status=status.HTTP_400_BAD_REQUEST)
    player = Player.objects.get(id=id)
    serializer = PlayerSerializer(player, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
    
    else : 
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)
