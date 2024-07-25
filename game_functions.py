import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_events(event,ai_settings,screen,ship,bullets):
    '''Respond to keypresses'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right= True
    elif event.key == pygame.K_LEFT:
        ship.moving_left= True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    '''Fire a bullet if limit not reached yet'''
    #Create a new bullet and add it to the bullets group
    if len(bullets)< ai_settings.bullets_allowed:    
        new_bullet= Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    '''Respond to key releases'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings,screen,ship,bullets):
    '''respond to keypresses and mouse events'''
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings,screen, ship, bullets)
        
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)    



def update_screen(ai_settings, screen, ship,aliens, bullets,play_button):
    '''Update images on the screen and flip to the new screen'''
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    #Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    #Draw the play button if the game is inactive
    if not game_stats.game_active:
        play_button.draw_button()
    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(ai_settings,screen,ship,aliens,bullets):
    '''Update position of bullet and get rid of old bullets'''
    # Update bullet positions.
    bullets.update()

    # Check if any bullet has hit an alien if so, delete the bullet and the alien
    collisions=pygame.sprite.groupcollide(bullets, aliens, ai_settings.bullet_disappear , True )                                    # False for higher bullet penetration

    if len(aliens)==0:
        # destroy existing bullets and create new fleet
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)
    
    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)

def create_fleet(ai_settings,screen,ship,aliens):
    '''Create a full fleet of aliens'''
    # Create an alien and find the number of aliens in a row.
    #Spacing beteween each alien is equal to one alien width.
    alien= Alien(ai_settings, screen)
    number_aliens_x=get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows= get_number_rows(ai_settings,ship.rect.height, alien.rect.height  )

    # Create the first row of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # Create an alien and place it in the row.
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

def get_number_aliens_x(ai_settings,alien_width):
    '''Determine the number of aliens that fit in a row'''
    available_space_x= ai_settings.screen_width- 2*alien_width
    number_aliens_x= int(available_space_x/(2* alien_width))
    return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """Create an alien and place it in a row"""
    alien= Alien(ai_settings,screen)
    alien_width=alien.rect.width
    alien.x=alien_width+ 2*alien_width*alien_number
    alien.rect.x= alien.x
    alien.rect.y= alien.rect.height+ 2* alien.rect.height*row_number
    aliens.add(alien)

def get_number_rows(ai_settings,ship_height,aliens_height):
    """Get the number of rows available for the aliens"""
    available_space_y= (ai_settings.screen_height) - (ship_height) - (3*aliens_height)
    number_rows= int(available_space_y/(2*aliens_height))
    return number_rows

def update_aliens(ai_settings, stats , screen, ship, aliens, bullets):
    "check if the fleet is at an edge and then update the positions of all the aliens in a fleet"
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    # Look for alien - ship collisions
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings, stats , screen, ship, aliens, bullets)

    #Look for aliens hitting the bottom of the screen
    check_aliens_bottom(ai_settings, stats , screen, ship, aliens, bullets)


def check_fleet_edges(ai_settings,aliens):
    "Respond appropriately if any aliens have reached an edge"
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    "drop the entire fleet and change the fleets direction"
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.alien_drop_speed ####################################
    ai_settings.fleet_direction *=-1


def ship_hit(ai_settings, stats , screen, ship, aliens, bullets):
    "Respond to ship being hit by alien"
    if stats.ships_left>0 :
        # Decrement ships left
        stats.ships_left -= 1

        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        #Create a new fleet  and centre the ship
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

        # Pasue'
        sleep(0.5)
    
    else:
        stats.game_active= False

def check_aliens_bottom(ai_settings, stats , screen, ship, aliens, bullets):
    "Check if the aliens have reached the bottom of the screen"
    screen_rect= screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this as if the ship got hit
            ship_hit(ai_settings, stats , screen, ship, aliens, bullets)
            break

