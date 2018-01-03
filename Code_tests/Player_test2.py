
import pygame
import numpy

pygame.init()

screenSize = (640, 480)
WeirdColor = pygame.color.Color("#1c6bea")
clock = pygame.time.Clock()

pygame.display.set_caption("Player_testing")
screen = pygame.display.set_mode(screenSize)

class player:
    """Here we will test the movement and projectiles/potential."""
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
        self.fall_test = False
        self.tryhard = False

        ##################
        #Fall test.
        self.FallEquationX = -65.6
        self.FallX = 2.5
        self.FallIteration = 0
        self.InitY = 410
        self.InitX = 200

    def DoNotCrash(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_loop = False
            if event.key == pygame.K_h:
                self.fall_test = True

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

        if self.tryhard == True:
            screen.blit(self.player_idle, (200,410))
        else:
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
                y = -20 * x * (x - 5)
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

    def falling_physics(self,screen):
        """
        Mimic the supposed appearance of "falling" through acceleratio-
        n and subsequent smaller accelerations along the y axises.
        4 accelerations will be used.
        The equation chosen:
        The reason: Whilst it may provide the appearance of falling, i-
        also gives the user the pixelated character little room to mov-
        e along the x axises implying that the user was dropped with o-
        n a smooth surface which is the intention.
        Ask Sophia to satisfy this criteria:
        All curves must be small according to the x axis.
        Subsequent curves after the 1st curve must be 
        """
        #this issue will be solved using the current equation for "jump"
        """
        y=-99.2x(x-5)
        (2.5,620)
        self.jump_change = -99.2
        """
        # Numpy module is very important in making the jump seemingly smooth.

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
                print("wtf?")
                self.fall_test = False

        # first time i wrote the plan for this function on paper. Normally I type it instead but that lacks the visual.
        """
        It was faster to create because I had the plan on paper instead of the 
        usual fustration of constant trail and error. Whereby I would create 
        incomplete code and fix the errors that come along, amounting to massi-
        ve amounts of bug fixes. For this only 2 bugs were to be fixed because 
        I had forgotten to take into account the first iteration and where I 
        were to place the character.
        """
    def reformed_movement(self,screen):
        """Improving player_movement function to make it possible to jump on platforms."""
        pass
game_loop = True

user = player()

#player_movement

user.player_x = 320
user.player_y = 340
user.player_x_move = 0
user.player_y_move = 0
user.jumpx = 0
user.jumpy = 340
user.y = 0
user.x = 0
user.key_check = 0
user.jump = False
user.jump_check = 0

#Falling_test.
user.fall_test = False




while user.game_loop == True:

    screen.fill(WeirdColor)
    #after alot of testing, I realize the problem is:  You can't have 2 event handling loops.
    #https://stackoverflow.com/questions/42888013/why-can-pygame-event-get-only-be-called-once-per-frame



    user.player_movements(screen)
    user.player_x += user.player_x_move
    user.player_y += user.player_y_move
    user.player_movements(screen)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
quit()

