import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    '''A class to manage the bullet fired from the ship'''
    def __init__(self,ai_settings,screen,ship):
        '''Create a bullet obeject at the ship's current location'''
        super(Bullet,self).__init__()
        self.screen = screen

        #Create a bullet rect at (0,0) and then set the correct postion
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx= ship.rect.centerx
        self.rect.top= ship.rect.top

        #Store the bullets positon as a decimal value
        self.y= float(self.rect.y)

        self.colour= ai_settings.bullet_colour
        self.speed_factor= ai_settings.bullet_speed_factor

    def update(self):
        '''Move the bullet up the screen'''
        # Update the decimal positions of the bullet
        self.y -= self.speed_factor
        # Update the rect postion.
        self.rect.y = self.y
    
    def draw_bullet(self):
        '''Draw the bullet to the screen'''
        pygame.draw.rect(self.screen, self.colour, self.rect)
