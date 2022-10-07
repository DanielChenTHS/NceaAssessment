import pgzrun
from pgzhelper import *
import random

# Constants
WIDTH = 564
HEIGHT = 764

# Global Variables
game_startup = True
game_running = False
game_ended = True
score = 0

# Actors
player = Actor('player')
player.x = 282
player.y = 724

can = Actor('can')
can.x = random.randint(20, 544)
can.y = 0

background = Actor('background')
background.x = 0
background.y = 200


#  end of initialisation section #


#  Function definitions begin here  #
def update():
    global score, game_startup, game_running, game_ended, score
    if game_startup:  # display splash screen
        while game_startup == True:
            if keyboard.s:
                game_startup = False
            else:
                game_startup = True
    elif game_running:  # display  gameplay screen  - game running code goes in this block…
        if keyboard.left:
            player.x = player.x - 5
        if keyboard.right:
            player.x = player.x + 5
        if player.x < 10:
            player.x = 10
        if player.x > (WIDTH - 10):
            player.x = 504

        can.y = can.y + 4 + score / 5
        if can.y > 764:
            game_running = False

            can.x = random.randint(20, 544)
            can.y = 0

        if can.colliderect(player):
            can.x = random.randint(20, 544)
            can.y = 0
            score = score + 1

def draw():
    if game_startup:  # game has not yet started
        background.draw()
        screen.draw.text("Click to start ",
                         midbottom=(282, 382), width=460, fontname="boogaloo", fontsize=48,
                         color="#AAFF00", gcolor="#66AA00", owidth=1.5, ocolor="black", alpha=0.8)

    elif game_running:  # game is playing
        screen.fill((0, 0, 0))
        player.draw()
    else:  # game has ended
        screen.fill((100, 100, 100))
        screen.draw.text("Your final score is :  " + str(score),
                         midbottom=(400, 300), width=460, fontname="boogaloo", fontsize=15,
                         color="#AAFF00", gcolor="#66AA00", owidth=1.5, ocolor="black", alpha=0.8)


def on_key_down(key):
    if key == keys.F:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    elif key == keys.W:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))


pgzrun.go()
