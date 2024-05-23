import pygame
from settings import Settings
from events import Events

class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.events = Events()
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        pygame.display.set_caption("Game Window")
        self.frames_per_second = pygame.time.Clock()

    def run_game(self):
        while True:
            self.frames_per_second.tick(self.settings.fps)
            self.events.check_events()
            self.draw_screen() 

    def draw_screen(self):
        self.screen.fill(self.settings.default_backround_color)
        pygame.display.flip()

