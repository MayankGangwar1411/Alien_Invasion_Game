import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        """A class to represent a single alien in the fleet"""
        super(Alien,self).__init__()
        self.screen= screen
        self.ai_settings= ai_settings

        # Load the ship image
        self.image = pygame.image.load('images/alien.bmp')
        
        # Resize the image
        default_image_size=(50,50)
        self.image = pygame.transform.scale(self.image, default_image_size)
        
        # get the alien rect
        self.rect= self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x= self.rect.width
        self.rect.y= self.rect.height

        #Store the alien's exact position.
        self.x= float(self.rect.x)
    
    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        "Move the alien to the right or left"
        self.x += (self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)
        self.rect.x=self.x
    
    def check_edges(self):
        "Return true if alien is at an edge"
        screen_rect=self.screen.get_rect()
        if self.rect.right>= screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True
        
        