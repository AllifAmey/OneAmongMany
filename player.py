import pygame
import numpy

class player:
    """
    This class is used to initiate the movement of the player, mostly.
    You can change the initial placing of the player by simply changing
    self.player_x, for the x coordinate, self.player_y, for the y coordinate.
    """
    def __init__(self):
        self.player_left = pygame.image.load("C:/Users/Al-lif/PycharmProjects/Pygame/Art/Player_left.png")
        self.player_right = pygame.image.load("C:/Users/Al-lif/PycharmProjects/Pygame/Art/Player_right.png")
        self.player_idle = pygame.image.load("C:/Users/Al-lif/PycharmProjects/Pygame/Art/Player_idle.png")
        self.game_loop = True
        #################
        self.player_x = 320
        self.player_y = 340
        self.player_x_move = 0
        self.player_y_move = 0
        self.jumpx = 0
        self.jumpy = 340
        self.y = 0
        self.x = 0
        self.key_check = 0
        self.jump = False
        self.jump_check = 0
        ##################
        self.FallEquationX = -65.6
        self.FallX = 2.5
        self.FallIteration = 0
        self.InitY = 410
        self.InitX = 200

    def player_movements(self,screen):
        """Player movements here."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.player_x_move = -5
                    self.key_check = 1

                if event.key == pygame.K_d:
                    self.player_x_move = 5
                    self.key_check = 2

                if event.key == pygame.K_w:
                    self.jump = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    self.player_x_move = 0
                    self.key_check = 0

        if self.jump != True:
            self.player_x += self.player_x_move
            self.player_y += self.player_y_move

            # Collision detection.
            # screen boundaries.
            if self.player_x >= 590:
                self.player_x = 590
            if self.player_x <= 0:
                self.player_x = 0
            if self.key_check == 2:
                screen.blit(self.player_right, (self.player_x, self.player_y))
            if self.key_check == 1:
                screen.blit(self.player_left, (self.player_x, self.player_y))
            if self.key_check == 0:
                screen.blit(self.player_idle, (self.player_x, self.player_y))
        else:
            # x = self.player_x
            # y = self.player_y
            # y = -15x(x-5)

            # Numpy module is very important in making the jump seemingly smooth.
            jump_x_list = numpy.arange(0, 5.1, 0.1)
            x = jump_x_list[self.jump_check]
            # more the number -15 lower such as -30 to make the user jump higher.
            # power up idea to jump higher than normal? Gives them more time to jump and kill/avoid enemies.
            y = -15 * x * (x - 5)
            self.jumpy = self.player_y - y
            self.jumpx = self.player_x + x
            if self.jumpx >= 590:
                self.jumpx = 590
            if self.player_x <= 0:
                self.jumpx = 0
            screen.blit(self.player_idle, (self.jumpx, self.jumpy))
            self.jump_check += 1
            if self.jump_check == 50:
                self.player_x += 5
                self.player_y = 340
                self.jumpy = 340
                self.jump = False
                self.jump_check = 0

    def physics_jump(self,screen):
        """The fall for scene"""

        jump_x_list = numpy.arange(self.FallX, 5.0, 0.1)
        x = jump_x_list[self.jump_check]
        y = self.FallEquationX * x * (x - 5)
        self.jumpy = self.InitY - y
        self.jumpx = self.InitX + x
        if self.jumpx >= 590:
            self.jumpx = 590
        if self.player_x <= 0:
            self.jumpx = 0
        screen.blit(self.player_idle, (self.jumpx, self.jumpy))
        self.jump_check += 1
        if self.jump_check == 50 or self.jump_check == 25 and self.FallIteration == 0:
            self.FallX = 0
            self.FallEquationX /= 2
            self.jump_check = 0
            if self.FallIteration == 0:
                self.InitX += 2.5
            else:
                self.InitX += 5
            self.FallIteration += 1
            if self.FallIteration == 4:
                self.fall_test = False

