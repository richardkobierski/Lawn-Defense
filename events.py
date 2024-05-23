import pygame
from settings import Settings

class Events:
    def __init__(self):
        self.event = pygame.event
        self.settings = Settings()

    def check_events(self):
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif self.event.type == pygame.KEYDOWN:
                self.fullscreen_toggle()

    def fullscreen_toggle(self):
        if pygame.key.get_pressed()[pygame.K_f] and not self.settings.is_fullscreen:
            pygame.display.set_mode((self.settings.width, self.settings.height), pygame.FULLSCREEN)
            self.settings.is_fullscreen = True
        else:
            pygame.display.set_mode((self.settings.width, self.settings.height))
            self.settings.is_fullscreen = False