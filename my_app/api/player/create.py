## /////////////////////////////////////////////////////////////////////////////
## YOU CAN FREELY MODIFY THE CODE BELOW IN ORDER TO COMPLETE THE TASK
## /////////////////////////////////////////////////////////////////////////////

from django.http.response import JsonResponse
from rest_framework.request import Request
from rest_framework import status

def create_player_handler(request: Request):
    return JsonResponse('', status=status.HTTP_500_INTERNAL_SERVER_ERROR, safe=False)
