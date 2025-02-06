from src.entities.base import GameObject
from config.settings import PLAYER_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SIZE, PLAYER_LIVES
from config.constants import IMAGE_PATH
from src.utils.grid import Grid
from src.managers.resource_manager import ResourceManager


class Player(GameObject):
    def __init__(self,grid:'Grid'):
        # 出生点在中央
        position = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        super().__init__(position, PLAYER_SIZE,grid)
        self.speed = PLAYER_SPEED
        self.lives = PLAYER_LIVES
        self.is_invincible: bool = False
        self.score = 0

        # 创建图像
        image = ResourceManager().load_image(IMAGE_PATH + 'player.png')
        self.load_image(image)
