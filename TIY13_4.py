import sys
import pygame
from TIY13_3Settings import Settings
from TIY13_3Rain import Rain
from random import randint

class TIY13_3:
    def __init__(self):
        pygame.init()  # initialize pygame

        self.settings = Settings()  # creating setting init

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # The above sets the display info height and width from the settings class.

        pygame.display.set_caption("Raindrop")  # sets window title.

        self.rain = pygame.sprite.Group()  # creating a group of rain sprites.

        self._create_fleet()  # creating the fleet.

    def _update_drops(self): # updating drop helper method
        self.rain.update()
        for drop in self.rain.copy():
            if drop.rect.bottom >= self.screen.get_rect().bottom+720:
                self.rain.remove(drop)
                self.drop2 = Rain(self)
                self.drop_rect = self.drop2.rect
                self.drop_x, self.drop_y = self.drop_rect.width, self.drop_rect.height
                available_space_x = 1280 - (2 * self.drop_x)
                number_drops_x = available_space_x // (2 * self.drop_x)
                self._create_drop(randint(0, number_drops_x+1), 1)

    def _create_fleet(self):
        self.drop = Rain(self)
        self.drop_rect = self.drop.rect
        self.drop_x, self.drop_y = self.drop_rect.width, self.drop_rect.height
        available_space_x = 1280 - (
                    2 * self.drop_x)  # gets space available by removing two aliens (the edges of the screen) from the length.
        number_stars_x = available_space_x // (
                    2 * self.drop_x)  # Basically one alien is technically two (because its space counts as one) so we check how many 2 we can draw to screen.

        # Getting the number of rows of aliens that fits on the screen.
        available_space_y = (720 - (2 * self.drop_y))
        number_rows = available_space_y // (2 * self.drop_y)
        for row_number in range(number_rows):
            for drop_number in range(number_stars_x):
                self._create_drop(drop_number, row_number)

    def _create_drop(self, drop_number, row_number):
        drop = Rain(self)
        rain_width, rain_height = drop.rect.size
        drop.x = rain_width + 2 * rain_width*2 * drop_number
        drop.rect.x = drop.x + randint(-10, 10)
        drop.rect.y = drop.rect.height + 2 * drop.rect.height * 2 * row_number + randint(-20, 20)
        drop.y = drop.rect.y
        self.rain.add(drop)

    def _check_events(self):  # single leading underscores definte helper methods
        for event in pygame.event.get():  # getting a event invoked from pygame or the user.
            if event.type == pygame.QUIT:  # checking if that event is quit.
                sys.exit()  # exiting the application.
            elif event.type == pygame.KEYDOWN:  # checks if key was pressed
                self._check_keydown_events(event)  # runs our helper method for keydown events.

    def _check_keydown_events(self, event):  # keydown event helper.
        if event.key == pygame.K_q:  # checks if key pressed was q
            sys.exit()  # exits the program

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)  # fills the background with the rgb color.
        for drop in self.rain:
            drop.draw_rain()
        pygame.display.flip()  # makes most recent drawn screen visible.

    def _check_drops_bottom(self):
        """Check if any aliens have reached the bottom of the screen"""

        screen_rect = self.screen.get_rect()
        for drops in self.rain.sprites():
            if drops.rect.bottom >= screen_rect.bottom:
                self.rain.remove(drops)

    def run_game(self):
        while True:  # always running
            self._check_events()  # runs the check events method... which checks events by the user.
            self._update_drops()
            self._update_screen()  # runs the updating screen, which draws objects to the screen and backgrounds and such.


if __name__ == '__main__':
    ai = TIY13_3()
    ai.run_game()
