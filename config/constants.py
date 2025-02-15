import random
from enum import Enum
from typing import List

import pygame

from src.utils.vector2D import Vector2D

# 自定义事件
ENEMY_DIRECTION_EVENT = pygame.USEREVENT + 1
PLAYER_IS_INVINCIBLE_END = pygame.USEREVENT + 2

#定义方向
class Direction(Vector2D):
    all_direction = {
        'UP': Vector2D(0, -1),
        'DOWN': Vector2D(0, 1),
        'LEFT': Vector2D(-1, 0),
        'RIGHT': Vector2D(1, 0),
        'NONE': Vector2D(0, 0)
    }

    @classmethod
    def random_direction(cls) -> 'Vector2D':
        return random.choice([d for d in cls.all_direction.values() if d != cls.all_direction['NONE']])

    @classmethod
    def random_new_direction(cls, origin: List['Vector2D']) -> 'Vector2D':
        return random.choice([d for d in cls.all_direction.values() if d != cls.all_direction['NONE'] and d not in origin])


# 颜色
COLORS = {
    'BLACK': (0, 0, 0),
    'WHITE': (255, 255, 255),
    'BLUE': (0, 0, 255),
    'RED': (255, 0, 0),
    'YELLOW': (255, 255, 0),
    'BACKGROUND': (161, 238, 246),
    'CYAN': (14, 245, 234)
}

# 路径
IMAGE_PATH = "assets/images/"
SOUND_PATH = "assets/sounds/"
BGM_PATH = "assets/bgm/"


# 水果种类
class FruitType(Enum):
    BANANA = "banana"
    CHERRY = "cherry"
    DOT = "dot"
    DOTITEM = "dotitem"
