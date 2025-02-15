from src.entities.base import GameObject
from config.settings import ENEMY_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, ENEMY_SIZE
from config.constants import IMAGE_PATH, Direction
import random
from src.utils.vector2D import Vector2D
from src.managers.resource_manager import ResourceManager


class Enemy(GameObject):
    def __init__(self, grid):
        # 随机位置
        position = grid.get_random_floor_position()

        # 初始化参数
        super().__init__(position, ENEMY_SIZE, grid)
        self.speed = ENEMY_SPEED
        self.direction = Direction.random_direction()

        # 加载敌人图像
        enemy_index = random.randint(1, 4)
        image = ResourceManager().load_image(IMAGE_PATH + "ghost" + str(enemy_index) + ".png")
        self.init_image(image)

    def get_available_directions(self):
        """获取所有可行的方向"""
        available_directions = []
        for direction in Direction.all_direction.values():
            # 跳过NONE方向
            if direction == Direction.all_direction['NONE']:
                continue
            # 计算新位置
            new_position = self.position + direction * self.speed
            next_pos = Vector2D(new_position.x, new_position.y)
            # 使用can_move_to方法检查是否可以移动到新位置
            if self.can_move_to(next_pos):
                available_directions.append(direction)
        return available_directions

    def update(self):
        if self.image and self.rect:
            # 计算下一个位置
            next_position = self.position + self.direction * self.speed
            next_pos = Vector2D(next_position.x, next_position.y)

            # 检查是否可以移动到下一个位置
            if not self.can_move_to(next_pos):
                # 获取所有可行的方向
                available_directions = self.get_available_directions()
                if available_directions:  # 如果有可行的方向
                    # 随机选择一个可行的方向
                    self.direction = random.choice(available_directions)
                    # 使用新方向计算新位置
                    next_position = self.position + self.direction * self.speed
                    next_pos = Vector2D(next_position.x, next_position.y)
                    # 再次检查新方向是否可行
                    if self.can_move_to(next_pos):
                        self.position = next_position
            else:
                # 如果当前方向可行，正常移动
                self.position = next_position

            # 更新精灵的位置
            self.rect.center = self.position.to_tuple()