class Settings:
    def __init__(self):
        # Screen Settings
        self.screen_width = 1280 # sets screen width VARIABLE.
        self.screen_height = 720 # sets screen height VARIABLE.
        self.bg_color = (230, 230, 230) # sets background color VARIABLE.
        # This can also be used to make an options file that is editable in-game by the user with the use of json.
        # To use this, import it in the main game.

        # Bullet Settings
        self.rain_speed = 1.5 # 1 speed
        self.rain_width = 3 # 3 pixels wide
        self.rain_height = 15 # 15 pixels high
        self.rain_color = (135, 206, 235) # lightskyblue
