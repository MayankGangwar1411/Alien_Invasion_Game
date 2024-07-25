
import pygame
from pygame.sprite import Group
from ship import Ship
from settings import Settings
import game_functions as gf
from game_stats import GameStats
from button  import Button

def run_game():
    # Inititalize pygame, setting, and create a screen object
    pygame.init()
    ai_settings= Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Create an instance to store game statistics
    stats=GameStats(ai_settings)


    # MAke a ship
    ship=Ship(ai_settings,screen)

    #Make a group to store the bullets and aliens in.
    bullets= Group()
    aliens= Group()

    # create a fleet of  aliens
    gf.create_fleet(ai_settings,screen,ship,aliens)

    # Set teh background colour
    bg_colour=(230,230,230)

    # Make the Play button.
    play_button= Button(ai_settings, screen, "Play")

    
    #Start the main loop for the game
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
        
        gf.update_screen(ai_settings, screen, ship, aliens, bullets,play_button)
        

        

run_game()