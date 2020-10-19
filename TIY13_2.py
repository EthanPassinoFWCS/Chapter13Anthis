import sys
import pygame
from TIY13_1Stars import Star
from random import randint

class Stars:
    def __init__(self):
        pygame.init()  # initialize pygame

        self.screen = pygame.display.set_mode((1280, 720))
        # The above sets the display info height and width from the settings class.
        self.stars = pygame.sprite.Group()
        self._create_star_fleet()
        pygame.display.set_caption("Stars")  # sets window title.

    def _create_star(self, star_number, row_number):
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x + randint(-10, 10)
        star.rect.y = star.rect.height + 2 * star.rect.height * row_number + randint(-10, 10)
        self.stars.add(star)

    def _create_star_fleet(self):
        self.star = pygame.image.load("images/star.bmp")
        self.star_rect = self.star.get_rect()
        self.star_x, self.star_y = self.star_rect.width, self.star_rect.height
        available_space_x = 1280 - (2 * self.star_x) # gets space available by removing two aliens (the edges of the screen) from the length.
        number_stars_x =   available_space_x // (2 * self.star_x) # Basically one alien is technically two (because its space counts as one) so we check how many 2 we can draw to screen.

        # Getting the number of rows of aliens that fits on the screen.
        available_space_y = (720 - (2 * self.star_y))
        number_rows = available_space_y // (2 * self.star_y)
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _check_events(self): # single leading underscores definte helper methods
        for event in pygame.event.get():  # getting a event invoked from pygame or the user.
            if event.type == pygame.QUIT:  # checking if that event is quit.
                sys.exit()  # exiting the application.
            elif event.type == pygame.KEYDOWN: # checks if key was pressed
                self._check_keydown_events(event) # runs our helper method for keydown events.

    def _check_keydown_events(self, event): # keydown event helper.
        if event.key == pygame.K_q: # checks if key pressed was q
            sys.exit() # exits the program

    def _update_screen(self):
        self.screen.fill((230, 230, 230)) # sets background color VARIABLE.
        self.stars.draw(self.screen)
        pygame.display.flip()  # makes most recent drawn screen visible.

    def run_game(self):
        while True:  # always running
            self._check_events() # runs the check events method... which checks events by the user.
            self._update_screen() # runs the updating screen, which draws objects to the screen and backgrounds and such.


if __name__ == '__main__':
    ai = Stars()
    ai.run_game()
