from rest_framework import serializers 

from .player_skill import PlayerSkillSerializer
from ..models.player import Player
from ..models.player_skill import PlayerSkill

class PlayerSerializer(serializers.ModelSerializer):
    playerSkills = PlayerSkillSerializer(many=True)

    class Meta:
        model = Player
        fields = ['id', 'name', 'position', 'playerSkills']
        
    def create(self, validated_data):
        player_skills = validated_data.pop('playerSkills')
        player = Player.objects.create(**validated_data)
        for player_skill in player_skills:
            PlayerSkill.objects.create(player=player, **player_skill)
        return player
    
    
    def update(self, instance, validated_data):
        player_skills = validated_data.pop('playerSkills')
        instance = super().update(instance, validated_data)
        instance.playerSkills.all().delete()
        for player_skill in player_skills:
            PlayerSkill.objects.create(player=instance, **player_skill)
        
        return instance

    
    
    def validate(self, data):
        if len(data.get('playerSkills')) == 0 : 
            raise serializers.ValidationError('playerSkills is required')
        return data
