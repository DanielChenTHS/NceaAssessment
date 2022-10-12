import pgzrun
from pgzhelper import *
import random

# Constants
WIDTH = 564
HEIGHT = 764

# global variables
game_startup = True
game_running = True  # game ends when rubbish falls
game_ended = True
score = 0

# Actors
player = Actor('player')
player.y = 724
player.x = 282

rubbish = Actor('can')
rubbish.x = random.randint(20, 544)  # random function to decide x value when game is running
rubbish.y = 0

background = Actor('background')
background.x = 282
background.y = 382

# Rubbish actors that will cycle for variation
rubbish_list = ["can", "trash", "bottle"]
number_rubbish = 0
for x in range(len(rubbish_list)):
    number_rubbish += 1


# functions for when game is running
def update():
    global game_startup, game_running, game_ended, score  # variables listed
    if game_startup:  # display splash screen
        if keyboard.space:  # confirming startup of game
            game_startup = False
    elif game_running:  # display  gameplay screen  - game running code goes in this block…
        if keyboard.left:
            player.x = player.x - 5  # player movement to the left / detecting input for left arrow

        if keyboard.right:
            player.x = player.x + 5  # player movement to the right / detecting input for right arrow

        if player.x < 27:
            player.x = 27
        if player.x > 537:
            player.x = 537
        # setting constraints for world border / limited at x 537 and x 27 to stop player from leaving the playing field

        rubbish.y = rubbish.y + 4 + score / 5  # function to increase game difficulty
        if rubbish.y > 764:
            game_running = False

        if rubbish.colliderect(player):
            rubbish.x = random.randint(20, 544)  # spawning rubbish at random x coordinate
            index = random.randint(0, number_rubbish - 1)  # choosing which rubbish sprite to send down
            rubbish.image = rubbish_list[index]  # taking sprite image from list
            rubbish.y = 0  # rubbish spawn point
            score = score + 1  # if player collides with rubbish, score increases by one

        #  code to write:  need to turn game_running to False when the tank collides with a missile or something….

    else:  # display endgame screen
        pass  # nothing to do here as when player is dead will automatically go to end-game screen


def draw():
    if game_startup:  # game has not yet started
        background.draw()  # game instructions
        screen.draw.text("Space key to start ",
                         midbottom=(282, 500), width=460, fontname="boogaloo", fontsize=48,
                         color="#AAFF00", gcolor="#66AA00", owidth=1.5, ocolor="black", alpha=0.8)
        screen.draw.text("Controls | Left / Right Arrow Keys for movement",
                         midbottom=(282, 300), width=460, fontname="boogaloo", fontsize=48,
                         color="#AAFF00", gcolor="#66AA00", owidth=1.5, ocolor="black", alpha=0.8)

    elif game_running:  # game is playing
        background.draw()  # background actor
        player.draw()  # player actor
        rubbish.draw()  # rubbish actor
        screen.draw.text("Score :  " + str(score),
                         topleft=(1, 1), width=460, fontname="boogaloo", fontsize=48,
                         color="#AAFF00", gcolor="#66AA00", owidth=1.5, ocolor="black", alpha=0.8)
    else:  # game has ended
        background.draw()
        screen.draw.text("Your final score is :  " + str(score),
                         midbottom=(275, 500), width=460, fontname="boogaloo", fontsize=48,
                         color="#AAFF00", gcolor="#66AA00", owidth=1.5, ocolor="black", alpha=0.8)
        screen.draw.text("You Died",
                         midbottom=(275, 300), width=460, fontname="boogaloo", fontsize=48,
                         color="#AAFF00", gcolor="#66AA00", owidth=1.5, ocolor="black", alpha=0.8)


pgzrun.go()
