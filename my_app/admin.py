from django.contrib import admin
from my_app.models.player_skill import PlayerSkill
from my_app.models.player import Player
# Register your models here.

admin.site.register(Player)
admin.site.register(PlayerSkill)