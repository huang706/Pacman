import json

import pygame

from config.constants import IMAGE_PATH
from src.managers.resource_manager import ResourceManager
from src.utils.grid import Grid


class LevelManager:
    _instance = None

    def __new__(cls):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()
        self.current_level: int = 1
        self.grid = None
        self.background = None

    def get_grid(self) -> 'Grid':
        return self.grid

    def get_background(self) -> pygame.Surface:
        return self.background

    def load_level(self, level_number: int) -> None:
        with open(f'config/levels/level{level_number}.json', 'r') as f:
            level_data = json.load(f)
        self._create_map(level_data)

    def _create_map(self, level_data: dict) -> 'None':
        # 加载数据
        map_data = level_data["map_data"]
        cell_size = level_data["map_cell_size"]

        # 创建网格
        self.grid = Grid(len(map_data[0]), len(map_data), cell_size)

        # 创建窗口screen
        width = len(map_data[0]) * cell_size
        height = len(map_data) * cell_size
        self.background = pygame.Surface((width, height))

        # 设置墙壁
        for i, row in enumerate(map_data):
            for j, col in enumerate(row):
                if map_data[i][j] == 'W':
                    self.grid.set_wall(j, i)

        # 加载背景资源并绘图
        wall = ResourceManager().load_image(f"{IMAGE_PATH}Wall.png")
        floor = ResourceManager().load_image(f"{IMAGE_PATH}Floor.png")
        for i in range(len(map_data[0])):
            for j in range(len(map_data)):
                position = self.grid.grid_to_world((i, j))
                if self.grid.is_wall(i, j):
                    self.background.blit(wall, position.to_tuple())
                else:
                    self.background.blit(floor, position.to_tuple())
