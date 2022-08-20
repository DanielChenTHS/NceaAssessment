import mc_pgzrun
from pgzhelper import *
import random

WIDTH = 564
HEIGHT = 764

player = Actor('player')
player.x = 282
player.y = 724

can = Actor('can')
can.x = random.randint(20,544)
can.y = 0


def update():
    if keyboard.left:
        player.x = player.x - 5
    if keyboard.right:
        player.x = player.x + 5

    can.y = can.y + 4
    if can.y > 764:
        can.x = random.randint(20,544)
        can.y = 0

    if can.colliderect(player):
        can.x = random.randint(20, 544)
        can.y = 0


def draw():
    screen.blit('background', (0, 0))
    player.draw()
    can.draw()

mc_pgzrun.go() # Must be last line
