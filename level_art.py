import pygame
from Player_test import *
import level_art

pygame.init()

screenSize = (640, 480)
WeirdColor = pygame.color.Color("#1c6bea")

pygame.display.set_caption("OneAmongMany")
screen = pygame.display.set_mode(screenSize)

class InstanceArt:
    """Instance art include intro, levels and end."""
    """ 
    The art will primarily be based on using pygame's draw function.
    
    Create Intro, 2 basic puzzle levels and end.
     
    1 basic - Grab the key.
    2 basic - Press right colour according to colour of door.
    
    Once all instances are created, expand upon the current level variation to:
    
    5 basic puzzle levels, instead of 2 basic puzzle levels
    2 medium puzzle levels
    1 hard puzzle level
    1 boss fight.
    End.
    """

    def __init__(self):
        pass

    def Intro(self):
        """Art and interaction for Intro."""
        pass
    def GrabtheKey(self):
        """Art and interaction for 1st level"""
        pass
    def RightColour(self):
        """Art and interactions for 2nd level"""
        pass
    def Credits(self):
        """Art and interactions for Credits"""
        pass

Instance = 0
while user.game_loop == True:

    screen.fill(WeirdColor)
    #after alot of testing, I realize the problem is:  You can't have 2 event handling loops.
    #https://stackoverflow.com/questions/42888013/why-can-pygame-event-get-only-be-called-once-per-frame
    """
    user.player_movements()
    user.player_x += user.player_x_move
    user.player_y += user.player_y_move
    user.player_movements()
    """

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
quit()