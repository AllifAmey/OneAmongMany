import pygame
from player import *

pygame.init()

screenSize = (640, 480)
WeirdColor = pygame.color.Color("#1c6bea")
clock = pygame.time.Clock()

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

    """
    IMPORTANT:
    Remember the player is 50x50. Base your art around that.
    """

    def __init__(self):
        #colours?
        self.dark_purple = pygame.color.Color("#f9f968")
        self.light_purple = None
        #Images
        self.intro = pygame.image.load("C:/Users/Al-lif/PycharmProjects/Pygame/Art/Intro_background.jpg").convert()
        self.intro_door = pygame.image.load("C:/Users/Al-lif/PycharmProjects/Pygame/Art/Intro_door.png").convert()
        self.intro_fade = pygame.image.load("C:/Users/Al-lif/PycharmProjects/Pygame/Art/Intro_background.jpg").convert()
        self.music_check = 0
        #Intro variables.
        self.ImageFade = 0
        self.ImageFade_check = False
        self.ImageFade_plus = 0.05
        self.Image_init = "Temp"

    def Intro(self,screen):
        """Art for Intro."""

        #Fade in
        if not(self.ImageFade >= 255) and self.ImageFade_check == False:
            self.ImageFade += self.ImageFade_plus

        self.intro.set_alpha(self.ImageFade)
        screen.blit(self.intro, (0, 0))

        if self.ImageFade >= 60:
            self.intro_door.set_alpha(self.ImageFade)
            screen.blit(self.intro_door,(620,345))

    def blit_alpha(self, target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)
        target.blit(temp, location)

    def intro_fade(self,screen):
        print("hello")
        #screen.fill((0, 0, 0))
        """
        if self.Image_init == "Temp":
            self.Image_init = "Catnoise"
            self.ImageFade = 255

        if self.ImageFade <= 0:
            self.ImageFade = 0

        self.ImageFade -= self.ImageFade_plus + 5
        print(self.ImageFade)
        """

    def intro_interaction(self):
        """Interaction for Intro"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                user.game_loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.ImageFade_check = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.ImageFade_check = False





    def GrabtheKey(self):
        """Art and interaction for 1st level"""
        pass
    def RightColour(self):
        """Art and interactions for 2nd level"""
        pass
    def Credits(self):
        """Art and interactions for Credits"""
        pass

    def Music_list(self, level):
        #"C:/Users/Al-lif/PycharmProjects/Pygame/"
        if level == "intro":

            pygame.mixer.set_num_channels(2)
            Intro_fadeout = pygame.mixer.Channel(1)

            if pygame.mixer.music.get_busy() == False:
                pygame.mixer.music.set_volume(1.0)
                if self.music_check == 0:
                    pygame.mixer.music.load("C:/Users/Al-lif/PycharmProjects/Pygame/Music/Intro_1.ogg")
                    pygame.mixer.music.play(-1)
                self.musicTemp = "Temp"
            if self.music_check == 2:
                if pygame.mixer.music.get_busy() == True and self.musicTemp == "Temp":
                    Voice1 = pygame.mixer.Sound("C:/Users/Al-lif/PycharmProjects/Pygame/Music/Voice1.ogg")
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("C:/Users/Al-lif/PycharmProjects/Pygame/Music/Puzzle_1_1.mp3")
                    pygame.mixer.music.play(-1)
                    #Intro_fadeout.play(Voice1)
                    self.musicTemp = "Temp1"

        elif level == "tutorial":
            pass




###############
Instance = 0

user = player()

##################

instance = 0
instancemaster = InstanceArt()

while user.game_loop == True:
    if instance == 0:
        #You need an event handling loop or you will crash.
        instancemaster.Intro(screen)
        instancemaster.Music_list("intro")

        if instancemaster.ImageFade >= 40:
            instancemaster.ImageFade_plus = 1
            user.player_movements(screen)
            user.player_x += user.player_x_move
            user.player_y += user.player_y_move
            user.player_movements(screen)
            #door interaction.
            if user.player_x >= 580 and user.player_y >= 290:
                #screen.fill((0,0,0))
                #print(self.ImageFade)
                instance = 0.5
        else:
            instancemaster.intro_interaction()
    elif instance == 0.25:

        pass
    elif instance == 0.5:
        """
        This is the strangest error I have received. Apprantly there is an issue with the intro_fade() method.
        Even when intro_fade() contains screen.fill((0 , 0, 0)), it will return an error: 
        "TypeError: 'pygame.Surface' object is not callable"
        But when I do screen.fill((0, 0, 0)) without calling the method, I receieve no error. 
        In conclusion, to solve this problem I will have to "fix" the method intro_fade(). Perhaps a rename is in order.
        """

        #screen.fill((0 , 0, 0))
        instancemaster.intro_fade(screen)
        instancemaster.music_check = 2
        instancemaster.Music_list("intro")
        instancemaster.intro_interaction()


    elif instance == 1:

        user.player_movements(screen)
        user.player_x += user.player_x_move
        user.player_y += user.player_y_move
        user.player_movements(screen)


    pygame.display.flip()
    clock.tick(30)

pygame.quit()
quit()

"""
Self-improvement before I forget: 

1.Make class methods more self-contained and not reliant on globals such as:

    def Intro(self):
        \"""Art for Intro.\"""
        #Fade in

        if not(self.ImageFade >= 255) and self.ImageFade_check == False:
            self.ImageFade += self.ImageFade_plus
            #print(self.ImageFade)

        self.intro.set_alpha(self.ImageFade)

        screen.blit(self.intro, (0, 0))
        if self.ImageFade >= 60:
            self.intro_door.set_alpha(self.ImageFade)
            screen.blit(self.intro_door,(620,345))
    
    INTO:
    
    def Intro(self,screen):
        \"""Art for Intro.\"""
        #Fade in

        if not(self.ImageFade >= 255) and self.ImageFade_check == False:
            self.ImageFade += self.ImageFade_plus
            #print(self.ImageFade)

        self.intro.set_alpha(self.ImageFade)

        screen.blit(self.intro, (0, 0))
        if self.ImageFade >= 60:
            self.intro_door.set_alpha(self.ImageFade)
            screen.blit(self.intro_door,(620,345))
    
    The "screen" parameter replaces the global variable "screen" and makes it easier to import
    the file as a subprogram while also making the class feel more like a true class variable.
    
    
The reason I ,personally, want it to be more self-reliant is because it doesn't feel like
a true object, it isn't self-contained as it is reliant on globals and the point of classes -
as far as I can tell - is to try and make things more local so that one small change doesn't
affect the whole program and only affects the object , the class.

2. Have a clear vision for what functions you are going to make so that you can create variabl-
e names that portray more clearer the intent of the function.
"""