import pygame
from pygame.sprite import Sprite

class Rain(Sprite):
    def __init__(self, ai_game):
        # Initializing parent class, getting information from other classes.
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.rain_color

        # Creating a bullet at 0, 0 and then setting it to the correct position.
        self.rect = pygame.Rect(0, 0, self.settings.rain_width, self.settings.rain_height)

        # Storing bullet's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        # Moving the bullet up the screen when you shoot it.
        self.y += self.settings.rain_speed
        # Updating bullet position
        self.rect.y = self.y

    def draw_rain(self):
        # Drawing the bullet to the screen
        pygame.draw.rect(self.screen, self.color, self.rect)
