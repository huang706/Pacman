import pygame.time

from config.constants import PLAYER_IS_INVINCIBLE_END
from config.settings import PLAYER_INVINCIBLE_TIME
from src.entities.enemy import Enemy
from src.entities.fruit import Fruit
from src.entities.player import Player


def handle_player_fruit_collision(fruit: Fruit, player: Player) -> None:
    fruit.kill()
    player.score+=100

def handle_player_enemy_collision(enemy:Enemy,player:Player) ->None:
    if not player.is_invincible:
        player.lives-=1
        player.is_invincible = True
        pygame.time.set_timer(PLAYER_IS_INVINCIBLE_END,PLAYER_INVINCIBLE_TIME,1)

