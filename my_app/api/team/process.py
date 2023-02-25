## /////////////////////////////////////////////////////////////////////////////
## YOU CAN FREELY MODIFY THE CODE BELOW IN ORDER TO COMPLETE THE TASK
## /////////////////////////////////////////////////////////////////////////////

from django.http.response import JsonResponse
from rest_framework.request import Request
from rest_framework import status
from my_app.models.player import Player
from my_app.models.player_skill import PlayerSkill
from my_app.serializers.player import PlayerSerializer
from django.db.models import Q
        

def remove_duplicate_request_with_same_postion_and_skill(data): 
    non_duplicate_request = []
    checker = []
    for i in data : 
        checker_str = str(i['position']) + str(i['mainSkill'])
        if checker_str not in checker : 
            checker.append(checker_str)
            non_duplicate_request.append(i)
    return non_duplicate_request

def team_process_handler(request: Request):
    data = []
    
    ## Rule 4 he request should allow the same position and skill combination only once
    
    non_duplicate_request = remove_duplicate_request_with_same_postion_and_skill(request.data)
    
    
    for unique_request in non_duplicate_request : 
        required_position = unique_request['position']
        required_skill = unique_request['mainSkill']
        reqired_number_of_players = unique_request['numberOfPlayers']
        players = Player.objects.filter(Q(position=required_position) & Q(playerSkills__skill=required_skill)).order_by('-playerSkills__value')
        
        
        if players.count() == reqired_number_of_players : 
            for player in players : 
                data.append(player)
                
        elif players.count() > reqired_number_of_players :
            "Need to sort the best first players" 
            for player in players[:reqired_number_of_players] : 
                data.append(player)
        
        else :  
            if reqired_number_of_players > players.count() : 
                new_players = Player.objects.filter(position=required_position).order_by('-playerSkills__value')
                
                if new_players.count() < reqired_number_of_players : 
                    data.append("Insufficient number of players for position: " + str(required_position))
                else : 
                    for player in new_players[:reqired_number_of_players] : 
                        data.append(player)
    
    
    
            

    for i in data : 
        if isinstance(i, str) : 
            return JsonResponse({'error' : i}, status=status.HTTP_404_NOT_FOUND) 
    li  = [i.id for i in data if not isinstance(i, str)]       
    queryset = Player.objects.filter(id__in=li)
    serializer = PlayerSerializer(data=queryset, many=True)
    if serializer.is_valid(): 
        serializer.save()
    return JsonResponse(serializer.data,status=status.HTTP_500_INTERNAL_SERVER_ERROR, safe=False)