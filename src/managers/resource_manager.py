from typing import Dict, Optional

import pygame


class ResourceManager:
    _instance: 'ResourceManager' = None

    def __new__(cls) -> Optional['ResourceManager']:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.images: Dict[str, pygame.Surface] = {}
        self.sounds: Dict[str, pygame.mixer.Sound] = {}

    def load_image(self, path: str) -> pygame.Surface:
        if path not in self.images:
            try:
                self.images[path] = pygame.image.load(path).convert_alpha()
            except pygame.error as e:
                print(f"error loading image {path}:{e}")
                self.images[path] = pygame.Surface((32, 32))
                self.images[path].fill((255, 0, 255))
        return self.images[path]

    def load_sound(self, path: str) -> Optional[pygame.mixer.Sound]:
        if path not in self.sounds:
            try:
                self.sounds[path] = pygame.mixer.Sound(path)
            except pygame.error as e:
                print(f"error loading sound {path}:{e}")
                return None  # 或者返回一个默认的空音效
        return self.sounds[path]

    def load_bgm(self, path: str) -> bool:
        try:
            pygame.mixer.music.load(path)
            return True
        except pygame.error as e:
            print(f"error loading bgm {path}:{e}")
            return False

    def clear_cache(self) -> None:
        """清除所有资源缓存"""
        # 清理音效（需要先停止播放）
        for sound in self.sounds.values():
            sound.stop()
        self.sounds.clear()

        # 清理图像
        self.images.clear()

        # 清理背景音乐
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
