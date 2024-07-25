class Settings():
    # A class to store all settings for Alien Invasion
    
    def __init__(self):
        # Screen settings
        self.screen_width=1200
        self.screen_height= 800
        self.bg_color=(230,230,230)
        

        # SHIP Settings
        self.ship_speed_factor= 0.7
        self.ship_limit=3

        # Bullet Settings
        self.bullet_speed_factor= 0.5
        self.bullet_width = 300
        self.bullet_height= 15
        self.bullet_colour=(60,60,60)
        self.bullets_allowed= 4
        self.bullet_disappear= False    # False for non disapperaing bullets
        
        # Alien Settings
        self.alien_speed_factor= 0.1
        self.alien_drop_speed= 50
        self.fleet_direction= 1          # fleet_direction of 1 represents right; -1 represents left