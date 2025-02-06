import pygame
from config .settings import SFX_VOLUME


class AudioManager:
    def __init__(self):
        self.BGM_is_player=False

    def play_SFX(self, SFX: pygame.mixer.Sound) -> None:
        if SFX:
            SFX.set_volume(SFX_VOLUME)
            SFX.play()

    def play_BGM(self, resource_manager: 'ResourceManager') -> None:
        if resource_manager.load_bgm("assets/bgm.mp3"):
            pygame.mixer.music.play(-1)  # 循环播放
            self.BGM_is_player =True

    def stop_BGM(self):
        if self.BGM_is_player:
            pygame.mixer.music.stop()