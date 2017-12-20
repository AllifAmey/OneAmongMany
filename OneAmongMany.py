"""
This is a game where you , the player, will hack and slash your way,
through every wave of enemies and gain currency to upgrade your gear.
This game should contain 2 instances:
1. Enemy Arena.
2. gladiatorial Shop.

Enemy Arena.
1. Collision detection system for contact between the player and en-,
emy.
2. Player status system to calculate player damage,hitpoints and cu-,
rrency.
3. Instancing - From Enemy Arena to Shop.
4. Enemy wave system to enable the spawning of enemies and timing of,
wave distribution. Waves increase in difficulty based on player sta-,
tus? To be decided...

Gladiatorial Shop.
1.Basic,simple interface aimed for speed. You pick a feature from ,
your player status to upgrade.
2. Instancing - you are provided with the option to transfer to ano-,
ther instance, that being the Enemy Arena.
3. Possibly give more options.
4. Item selection - boost to player health, damage.

__________________________________

Enemies and their descriptions:

Brute orc - simple brute that gets close and hits.
Bright orc - Shoots projectiles that reduces the player's health by a,
amount.

Player_status:
'aim of this playstyle is to focus more on dodging than shooting ,
pressure is mounted onto the player as more enemies piles up against,
the player.

range weapon - one-shots but slow.
movement - limited but can be upgraded.

"""


import pygame

pygame.init()

screenSize = (640, 480)
WeirdColor = pygame.color.Color("#1c6bea")

pygame.display.set_caption("OneAmongMany")
screen = pygame.display.set_mode(screenSize)

game_loop = True

while game_loop == True:

    screen.fill(WeirdColor)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

    pygame.display.flip()

pygame.quit()