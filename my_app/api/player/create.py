## /////////////////////////////////////////////////////////////////////////////
## YOU CAN FREELY MODIFY THE CODE BELOW IN ORDER TO COMPLETE THE TASK
## /////////////////////////////////////////////////////////////////////////////

from django.http.response import JsonResponse
from rest_framework.request import Request
from rest_framework import status
from my_app.serializers.player import PlayerSerializer

def create_player_handler(request: Request):
    
    if request.data.get('position') not in  ['defender', 'midfielder','forward']:
        message = 'Invalid value for position: ' + str(request.data.get('position'))

        return JsonResponse({'message': message}, status=status.HTTP_400_BAD_REQUEST)
    else : 
        for skill in request.data.get('playerSkills'):
            if skill['skill'] not in ['defense', 'attack', 'speed', 'strength', 'stamina']:
                message = 'Invalid value for position: ' + str(skill['skill'])
                return JsonResponse({'error': 'Invalid skill'}, status=status.HTTP_400_BAD_REQUEST)
                
    serializer = PlayerSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
    else : 
        return JsonResponse(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR, safe=False)