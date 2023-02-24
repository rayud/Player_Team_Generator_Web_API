from rest_framework import serializers 

from .player_skill import PlayerSkillSerializer
from ..models.player import Player

class PlayerSerializer(serializers.ModelSerializer):
    playerSkills = PlayerSkillSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = ['id', 'name', 'position', 'playerSkills']
