from config.settings import GRID_WIDTH, GRID_HEIGHT
from src.utils.vector2D import Vector2D
from typing import Tuple


class Grid:
    def __init__(self, width: int, height: int, cell_size: int):
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.cell_size = cell_size
        self.width = width
        self.height = height

    def world_to_grid(self, position: 'Vector2D') -> Tuple[int, int]:
        pos_x = position.x // self.cell_size
        pos_y = position.y // self.cell_size
        return pos_x, pos_y

    def grid_to_world(self, grid_pos: Tuple[int, int]) -> 'Vector2D':
        x = grid_pos[0] * self.cell_size
        y = grid_pos[1] * self.cell_size
        return Vector2D(x, y)

    def set_wall(self, x: int, y: int):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = 1

    def is_wall(self, x: int, y: int):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x] == 1
        else:
            return True
