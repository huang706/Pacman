from src.entities.base import GameObject
from config.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FRUIT_SIZE
from config.constants import FruitType, IMAGE_PATH
import random

from src.managers.resource_manager import ResourceManager

class Fruit(GameObject):
    def __init__(self,grid):
        # 随机位置
        position = grid.get_random_floor_position()

        super().__init__(position, FRUIT_SIZE,grid)

        #随机选取图像并创建
        fruit_type = random.choice(list(FruitType))
        image=ResourceManager().load_image(IMAGE_PATH+fruit_type.value+".png")
        self.init_image(image)
