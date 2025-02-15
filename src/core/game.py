import pygame
from config.settings import FPS, FRUIT_NUM, ENEMY_NUM, SCREEN_WIDTH, SCREEN_HEIGHT
from config.constants import (
    IMAGE_PATH, Direction,
    PLAYER_IS_INVINCIBLE_END
)
from src.managers.collision_manager import CollisionManager
from src.core.handlers.collision_handlers import (
    handle_player_fruit_collision,
    handle_player_enemy_collision
)
from src.entities.enemy import Enemy
from src.entities.fruit import Fruit
from src.entities.player import Player
from src.managers.level_manager import LevelManager
from src.managers.resource_manager import ResourceManager


class Game:
    def __init__(self):
        # 初始化 Pygame
        pygame.init()

        # 初始化管理器
        self._init_managers()

        # 初始化游戏属性和对象
        self._init_game()

    def _init_managers(self):
        """初始化各种管理器"""
        self.resource_manager = ResourceManager()
        self.collision_manager = CollisionManager()
        self.level_manager = LevelManager()

        # 设置碰撞处理器
        self.collision_manager.add_handler(Player, Fruit, handle_player_fruit_collision)
        self.collision_manager.add_handler(Player, Enemy, handle_player_enemy_collision)

    def _init_game(self):
        # 创建游戏窗口
        self.screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pacman")

        # 加载关卡和设置窗口
        self.level_manager.load_level(1)
        self.grid = self.level_manager.get_grid()

        # 设置游戏图标
        icon = self.resource_manager.load_image(f"{IMAGE_PATH}icon.png")
        pygame.display.set_icon(icon)

        # 初始化游戏对象
        self._init_game_objects()

        # 初始化游戏控制
        self._init_game_controls()

    def _init_game_objects(self):
        """初始化游戏实体"""
        # 创建玩家
        self.player = Player(self.grid)

        # 创建敌人组
        self.enemies = pygame.sprite.Group()
        for _ in range(ENEMY_NUM):
            self.enemies.add(Enemy(self.grid))

        # 创建水果组
        self.fruits = pygame.sprite.Group()
        for _ in range(FRUIT_NUM):
            self.fruits.add(Fruit(self.grid))

    def _init_game_controls(self):
        """初始化游戏控制相关"""
        self.clock = pygame.time.Clock()
        self.running = True

        # 初始化按键状态
        self.key_pressed = {
            pygame.K_UP: False,
            pygame.K_DOWN: False,
            pygame.K_LEFT: False,
            pygame.K_RIGHT: False
        }

        # 设置按键方向映射
        self.key_to_direction = {
            pygame.K_UP: Direction.all_direction['UP'],
            pygame.K_DOWN: Direction.all_direction['DOWN'],
            pygame.K_LEFT: Direction.all_direction['LEFT'],
            pygame.K_RIGHT: Direction.all_direction['RIGHT']
        }

    def run(self):
        """游戏主循环"""
        while self.running and self.player.lives > 0:
            self._handle_events()
            self._update()
            self._handle_collisions()
            self._render()
            self._maintain_fps()

        pygame.quit()

    def _handle_events(self):
        """处理游戏事件"""
        for event in pygame.event.get():
            self._handle_system_events(event)
            self._handle_game_events(event)

        self._handle_player_input()

    def _handle_system_events(self, event):
        """处理系统事件"""
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.running = False

    def _handle_game_events(self, event):
        """处理游戏相关事件"""
        if event.type == pygame.KEYDOWN and event.key in self.key_pressed:
            self.key_pressed[event.key] = True
        elif event.type == pygame.KEYUP and event.key in self.key_pressed:
            self.key_pressed[event.key] = False
        elif event.type == PLAYER_IS_INVINCIBLE_END:
            self.player.is_invincible = False

    def _handle_player_input(self):
        """处理玩家输入"""
        self.player.direction = Direction.all_direction['NONE']  # 重置方向
        for key, is_pressed in self.key_pressed.items():
            if is_pressed:
                self.player.direction += self.key_to_direction[key]
        if any(self.key_pressed.values()):
            self.player.direction.normalize()

    def _update(self):
        """更新游戏状态"""
        self.player.update()
        self.enemies.update()

    def _handle_collisions(self):
        """处理碰撞"""
        player_group = pygame.sprite.Group(self.player)
        self.collision_manager.handle_collision_groups(
            player_group, self.enemies, self.fruits
        )

    def _render(self):
        """渲染游戏画面"""
        # 绘制地图（如果需要）
        self.screen.fill((0,0,0))
        self.screen.blit(self.level_manager.get_background(), (0, 0))

        # 绘制游戏对象
        self.player.draw(self.screen)
        self.fruits.draw(self.screen)
        self.enemies.draw(self.screen)

        # 更新显示
        pygame.display.flip()

    def _maintain_fps(self):
        """维持游戏帧率"""
        self.clock.tick(FPS)