import pygame
import numpy
import random
pygame.init()

screenSize = (640, 480)
WeirdColor = pygame.color.Color("#1c6bea")
clock = pygame.time.Clock()

pygame.display.set_caption("OneAmongMany")
screen = pygame.display.set_mode(screenSize)
class Enemy:
    """Here we will test Enemy spawn times."""
    def __init__(self):
        self.enemy_1st = pygame.image.load("C:/Users/Al-lif/PycharmProjects/Pygame/Art/Enemy_1st.png")

    """
    Forget doing enemy spawn. Try platform game.
    
    """
    def Enemyspawn(self):
        """Spawning and MOVEMENT."""
        #40px width 20px height
        if self.enemy_spawn == 0:
            #movement direction logic.
            if self.move_check == 0:
                self.enemy_x += 5
            else:
                self.enemy_x -= 5
            #collison detection
            #boundaries.
            if self.enemy_x == 600:
                self.enemy_x = 600
                self.move_check = 1
            elif self.enemy_x == 0:
                self.enemy_x = 0
                self.move_check = 0
            #player

            #right-side of enemy
            if self.player_x <= self.enemy_x + 40 and self.player_x >= self.enemy_x + 35 and self.jumpy == 340 and self.player_y == 340:
                self.enemy_spawn = 1
                print("1")
            #left-side of enemy.
            elif self.player_x + 50 >= self.enemy_x and self.player_x + 50 <= self.enemy_x + 5  and self.jumpy == 340 and self.player_y == 340:
                self.enemy_spawn = 2
                print("2")
            #up
            elif self.jumpy+60 >= self.enemy_y and self.player_x >= self.enemy_x and self.player_x <= self.enemy_x+40 :
                self.enemy_spawn = 3
                print("3")

            #spawn

            screen.blit(self.enemy_1st,(self.enemy_x, self.enemy_y))
        else:
            pass
            print(self.enemy_spawn)
            self.enemy_spawn = 0

            if self.player_x <= 110:

                self.enemy_x = self.player_x + 100
                screen.blit(self.enemy_1st, (self.enemy_x, self.enemy_y))
            elif self.player_x >= 500:
                self.enemy_x = self.player_x - 100
                screen.blit(self.enemy_1st, (self.enemy_x, self.enemy_y))
            else:
                if self.move_check == 0:
                    self.enemy_x = self.player_x + 100
                elif self.move_check == 1:
                    self.enemy_x = self.player_x - 100





        #user.enemy_x = 270
        #user.enemy_y = 340

class player(Enemy):
    """Here we will test the movement and projectiles/potential."""
    def __init__(self):
        Enemy.__init__(self)
        self.player_left = pygame.image.load("C:/Users/Al-lif/PycharmProjects/Pygame/Art/Player_left.png")
        self.player_right = pygame.image.load("C:/Users/Al-lif/PycharmProjects/Pygame/Art/Player_right.png")
        self.player_idle = pygame.image.load("C:/Users/Al-lif/PycharmProjects/Pygame/Art/Player_idle.png")
        self.game_loop = True

    def player_movements(self):
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
            jump_x_list = numpy.arange(0,5.1,0.1)
            x = jump_x_list[self.jump_check]
            #more the number -15 lower such as -30 to make the user jump higher.
            #power up idea to jump higher than normal? Gives them more time to jump and kill/avoid enemies.
            y = -15*x*(x-5)
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
                self.player_y =340
                self.jumpy = 340
                self.jump = False
                self.jump_check = 0


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
#enemy_movement
user.enemy_x = 270
user.enemy_y = 360
user.move_check = 0
user.enemy_spawn = 0
while user.game_loop == True:

    screen.fill(WeirdColor)
    #after alot of testing, I realize the problem is:  You can't have 2 event handling loops.
    #https://stackoverflow.com/questions/42888013/why-can-pygame-event-get-only-be-called-once-per-frame
    user.player_movements()
    user.player_x += user.player_x_move
    user.player_y += user.player_y_move
    user.player_movements()
    user.Enemyspawn()
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
quit()
