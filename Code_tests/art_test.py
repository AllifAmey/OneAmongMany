import pygame
pygame.init()

screenSize = (640, 480)

pygame.display.set_caption("OneAmongMany")
screen = pygame.display.set_mode(screenSize)
"""Class creation"""

class colours:
    """display all sorts of colours here."""
    def __init__(self):
        self.sun_colour = pygame.color.Color("#f9f968")
        self.ground_colour = pygame.color.Color("#6d4e3a")
        self.sky_colour = pygame.color.Color("#42f4d9")

class arena(colours):
    """This class is used for music and environmental art."""

    def __init__(self):
        colours.__init__(self)

    def Environment(self,screen):
        """Environment which includes the sun,ground and sky"""
        pygame.draw.rect(screen, self.ground_colour, ((0,340),(640,140)))
        pygame.draw.rect(screen, self.sun_colour,((500,50),(50,50)))

    def Music_list(self):
        #allows the continued repetition of 2 or more pieces of music.
        Music_1 = pygame.mixer.Sound("C:/Users/Al-lif/PycharmProjects/Pygame/Music/Arena.ogg")
        Music_2 = pygame.mixer.Sound("C:/Users/Al-lif/PycharmProjects/Pygame/Music/TransitionToInsanity.ogg")
        #Music_3 = pygame.mixer.music.load("C:/Users/Al-lif/PycharmProjects/Pygame/Music/Almost_done.mp3")
        #Music_4 = pygame.mixer.music.load("C:/Users/Al-lif/PycharmProjects/Pygame/Music/Pec.mp3")

        pygame.mixer.set_num_channels(2)

        Arena_music1 = pygame.mixer.Channel(1)

        #music logic.
        if Arena_music1.get_busy() == False and pygame.mixer.music.get_busy() == False:
            if self.music_check == 1:
                Arena_music1.play(Music_1)
                self.music_check = 2
            elif self.music_check == 2:
                Arena_music1.play(Music_2)
                self.music_check = 3
            elif self.music_check == 3:
                pygame.mixer.music.load("C:/Users/Al-lif/PycharmProjects/Pygame/Music/Pec.mp3")
                pygame.mixer.music.play(1)
                self.music_check = 4
            elif self.music_check == 4:
                pygame.mixer.music.load("C:/Users/Al-lif/PycharmProjects/Pygame/Music/Almost_done.mp3")
                pygame.mixer.music.play(1)
                self.music_check = 1

class intro(colours):

    def __init__(self):
        colours.__init__(self)

    def Environment(self):
        """Environment for the 1st instance- intro."""
        #background image?
        pass
        #buttons.
        pass
        #Title.

    def Music(self):
        """Music for intro"""
        #Play continuous calm/relaxing music.
        pass
"""Class testing"""
game_loop = True

Enemy_arena = arena()

Enemy_arena.music_start = 5
Enemy_arena.music_check = 1

while game_loop == True:
    """iniate environment shapes."""

    """Here's where you fill the environment for Enemy Arena."""

    screen.fill(Enemy_arena.sky_colour)
    Enemy_arena.Environment(screen)

    Enemy_arena.Music_list()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False


pygame.quit()