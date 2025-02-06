from typing import List, Callable

import pygame.event


class EventManager:
    _instance = None

    def __new__(cls) -> 'EventManager':
        if cls._instance == None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.event_handlers: List[Callable[..., None]] = []

    def add_handler(self, handler: Callable[..., None]):
        self.event_handlers.append(handler)

    def remove_handler(self, handler: Callable[..., None]):
        if handler in self.event_handlers:
            self.event_handlers.remove(handler)

    def handle_event(self,event:pygame.event.Event):
        for handler in self.event_handlers:
            handler(event)


