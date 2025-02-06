import pygame

from src.utils.check_beyond_boundary import is_beyond_boundary
from src.entities.base import GameObject
from config.settings import ENEMY_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, ENEMY_SIZE, ENEMY_CHANGE_DIRECTION_INTERVAL
from config.constants import IMAGE_PATH, Direction, ENEMY_DIRECTION_EVENT
import random

from src.managers.resource_manager import ResourceManager
from src.utils.vector2D import Vector2D


class Enemy(GameObject):
    def __init__(self, grid):
        # 在可通行位置随机生成
        position = grid.get_random_floor_position()

        # 初始化参数
        super().__init__(position, ENEMY_SIZE, grid)
        self.speed = ENEMY_SPEED

        # 确保初始方向是可行的
        available_directions = []
        for direction in Direction._all_direction.values():
            if direction != Direction._all_direction['NONE']:
                test_position = Vector2D(*position) + direction * self.speed
                if self.can_move_to(test_position):
                    available_directions.append(direction)

        # 从可用方向中随机选择一个
        self.direction = random.choice(available_directions) if available_directions else Direction._all_direction[
            'NONE']

        # 加载敌人图像
        enemy_index = random.randint(1, 4)
        image = ResourceManager().load_image(IMAGE_PATH + "ghost" + str(enemy_index) + ".png")
        self.load_image(image)

        # 设置方向改变计时器
        pygame.time.set_timer(ENEMY_DIRECTION_EVENT, ENEMY_CHANGE_DIRECTION_INTERVAL)
