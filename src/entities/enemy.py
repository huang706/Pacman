import pygame

from src.utils.check_beyond_boundary import is_beyond_boundary
from src.entities.base import GameObject
from config.settings import ENEMY_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, ENEMY_SIZE, ENEMY_CHANGE_DIRECTION_INTERVAL
from config.constants import IMAGE_PATH, Direction, ENEMY_DIRECTION_EVENT
import random

from src.managers.resource_manager import ResourceManager


class Enemy(GameObject):
    def __init__(self,grid):
        # 随机位置
        position = (
            random.randint(0, SCREEN_WIDTH - ENEMY_SIZE[0]),  # 考虑水果大小
            random.randint(0, SCREEN_HEIGHT - ENEMY_SIZE[1])
        )

        # 初始化参数
        super().__init__(position, ENEMY_SIZE,grid)
        self.speed = ENEMY_SPEED
        self.direction = Direction.random_direction()

        # 加载敌人图像
        enemy_index = random.randint(1, 4)
        image = ResourceManager().load_image(IMAGE_PATH + "ghost" + str(enemy_index) + ".png")
        self.load_image(image)

        # 设置方向改变计时器
        pygame.time.set_timer(ENEMY_DIRECTION_EVENT, ENEMY_CHANGE_DIRECTION_INTERVAL)

    def update(self):
        if self.image and self.rect:
            unavailable_directions = []
            for value in Direction._all_direction.values():
                new_position = self.position + value * self.speed
                if is_beyond_boundary(new_position.to_tuple(), self):
                    unavailable_directions.append(value)
            if self.direction in unavailable_directions:
                # 从可用方向中随机选择一个新方向
                self.direction = Direction.random_new_direction(unavailable_directions)
            self.position += self.direction * self.speed
            self.rect.topleft = self.position.to_tuple()
