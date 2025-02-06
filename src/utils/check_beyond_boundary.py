from config.settings import SCREEN_WIDTH, SCREEN_HEIGHT
from src.entities.base import GameObject
from typing import Tuple

def is_beyond_boundary(position:Tuple[int,int],entity:GameObject) -> bool:
    #检验垂直是否出界
    if position[0]<0 or position[0]>SCREEN_WIDTH-entity.size[0]:
        return True
    elif position[1]<0 or position[1]>SCREEN_HEIGHT-entity.size[1]:
        return True
    else:
        return False

