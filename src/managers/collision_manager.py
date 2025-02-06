from typing import Type, Callable

import pygame.sprite
from pygame.sprite import Group

from src.entities.base import GameObject


class CollisionManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.collision_handlers = {}

    def add_handler(self, type1: Type[GameObject], type2: Type[GameObject],
                   handler: Callable[[GameObject, GameObject], None]):
        collision_pair = tuple(sorted([type1, type2], key=lambda x: x.__name__))
        self.collision_handlers[collision_pair] = handler

    def handle_collision(self, group1: Group, group2: Group):
        collisions = pygame.sprite.groupcollide(group1, group2, False, False)

        for sprite1, collided_objects in collisions.items():
            for sprite2 in collided_objects:
                collision_pair = tuple(sorted([type(sprite1), type(sprite2)], key=lambda x: x.__name__))
                if collision_pair in self.collision_handlers:
                    handler = self.collision_handlers[collision_pair]
                    # 确保参数顺序与collision_pair中的类型顺序匹配
                    if type(sprite1) == collision_pair[0]:
                        handler(sprite1, sprite2)
                    else:
                        handler(sprite2, sprite1)

    def handle_collision_groups(self, *groups: Group):
        for i in range(len(groups)):
            for j in range(i + 1, len(groups)):
                self.handle_collision(groups[i], groups[j])