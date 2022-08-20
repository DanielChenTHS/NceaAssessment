import mc_pgzrun
from pgzhelper import *
import random

WIDTH = 564
HEIGHT = 764

player = Actor('player')
player.x = 282
player.y = 724

can = Actor('can')
can.x = random.randint(20, 544)
can.y = 0

score = 0
game_over = False


def update():
    global score, game_over

    if keyboard.left:
        player.x = player.x - 5
    if keyboard.right:
        player.x = player.x + 5

    can.y = can.y + 4 + score / 5
    if can.y > 764:
        game_over = True

        can.x = random.randint(20, 544)
        can.y = 0

    if can.colliderect(player):
        can.x = random.randint(20, 544)
        can.y = 0
        score = score + 1


def draw():
    screen.blit('background', (0, 0))

    if game_over:
        screen.draw.text('Game Over', (182, 402), color=(255, 255, 255), fontsize=60)
        screen.draw.text('Score: ' + str(score), (182, 362), color=(255, 255, 255), fontsize=60)
    else:
        can.draw()
        player.draw()
        screen.draw.text('Score: ' + str(score), (15, 10), color=(255, 255, 255), fontsize=30)


mc_pgzrun.go()  # Must be last line
