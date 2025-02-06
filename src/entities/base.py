import pygame
from pygame.sprite import Sprite
from typing import Tuple, Optional
from config.constants import Direction
from src.utils.grid import Grid
from src.utils.vector2D import Vector2D


class GameObject(Sprite):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], grid: 'Grid'):
        super().__init__()
        self.position = Vector2D(*position)
        self.size = size
        self.direction=Direction._all_direction['NONE']
        self.image: Optional[pygame.Surface] = None
        self.rect: Optional[pygame.Rect] = None
        self.grid = grid
        self.speed = 0

    def load_image(self, surface: pygame.Surface):
        self.image = pygame.transform.scale(surface, self.size)
        self.rect = pygame.Surface.get_rect(self.image)
        self.rect.topleft = self.position.to_tuple()

    def can_move_to(self,next_pos:'Vector2D'):
        # 计算角落所处的网格位置
        corners = {
            'TOPLEFT': (next_pos.x-self.size[0]/2,next_pos.y-self.size[1]/2),
            'TOPRIGHT': (next_pos.x+self.size[0]/2,next_pos.y-self.size[1]/2),
            'BOTTOMLEFT': (next_pos.x-self.size[0]/2,next_pos.y+self.size[1]/2),
            'BOTTOMRIGHT': (next_pos.x+self.size[0]/2,next_pos.y+self.size[1]/2)
        }

        for pos in corners.values():
            if self.grid.is_wall(*self.grid.world_to_grid(Vector2D(*pos))):
                return False
        return True

    def update(self):
        # 计算新位置
        new_position = self.position + self.direction * self.speed

        if self.can_move_to(new_position):
            # 更新位置
            self.position = new_position
            self.rect.center = self.position.to_tuple()

    def draw(self, screen: pygame.Surface):
        if self.image and self.rect:
            screen.blit(self.image, self.rect)
