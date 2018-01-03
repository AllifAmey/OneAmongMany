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
        self.Aquamarine = pygame.color.Color("#7fffd4")
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

    def Skipmaster(self,Skip):
        """For debugging."""
        return Skip

    def text(self,text,screen,Coordinates, text_colour, text_size = 20):
        """Enables the use of text."""
        background = pygame.Surface((50,50))
        text_object = pygame.font.Font("Intro_text.ttf",text_size)
        text_object = text_object.render(text, True ,(text_colour))
        x = Coordinates[0]
        y = Coordinates[1]
        screen.blit(text_object,(x,y))

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

    def Intro_fading(self,screen):

        if self.Image_init == "Temp":
            self.Image_init = "Catnoise"
            self.ImageFade = 200
            self.ImageFade_plus = 0.5

        self.ImageFade -= self.ImageFade_plus

        if self.ImageFade <= 0:
            self.ImageFade = 0

        screen.set_alpha(self.ImageFade)
        print(self.ImageFade)
        screen.fill((0,0,0))
        self.intro.set_alpha(self.ImageFade)
        self.TempSurface = pygame.Surface((640,480)).convert()
        self.TempSurface.blit(self.intro, (0,0))
        screen.blit(self.TempSurface, (0,0))


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





    def GrabtheKey(self,screen, status="pre-level"):
        """Art and interaction for 1st level"""
        if status == "pre-level":
            """Here we will perhaps create the scene of the player falling from the sky."""
            screen.fill((255,0,0))
            pygame.draw.rect(screen, (0,255,0),(0,460, 640,20))

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
                pygame.mixer.music.set_volume(0.5)
                if pygame.mixer.music.get_busy() == True and self.musicTemp == "Temp":
                    Voice1 = pygame.mixer.Sound("C:/Users/Al-lif/PycharmProjects/Pygame/Music/Intro_voice2.ogg")
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("C:/Users/Al-lif/PycharmProjects/Pygame/Music/Intro_2.mp3")
                    pygame.mixer.music.play(-1)
                    Intro_fadeout.play(Voice1)
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
            if user.jumpy == 340:
                instancemaster.text("I'm alive!", screen, (user.player_x- 10, user.player_y - 25), (0,0,0), 10)
            else:
                instancemaster.text("Weee!", screen, (user.player_x + 10, user.jumpy - 25), (0,0,0), 10)

            #door interaction.
            if user.player_x >= 580 and user.player_y >= 290:

                instance = 0.5
        else:
            instancemaster.intro_interaction()
    elif instance == 0.25:

        pass
    elif instance == 0.5:
        #screen.fill((0 , 0, 0))
        if instancemaster.ImageFade == 0:
            instance = 0.75
        instancemaster.Intro_fading(screen)
        instancemaster.music_check = 2
        instancemaster.Music_list("intro")
        instancemaster.intro_interaction()

    elif instance == 0.75:
        instancemaster.GrabtheKey(screen)
        instancemaster.intro_interaction()
        user.physics_jump(screen)
        if user.FallIteration == 4:
            user.player_x = 220
            user.player_y = 413
            instance = 1
    elif instance == 1:
        screen.blit(user.player_right, (user.player_x,user.player_y))
        instancemaster.intro_interaction()
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
quit()

