import mc_pgzrun
from pgzero.game import screen
from pgzero.keyboard import keyboard

from pgzhelper import *

WIDTH = 564
HEIGHT = 764

player = Actor('player')
player.x = 370
player.y = 550

def update():
    if keyboard.left:
        player.x = player.x - 5
    if keyboard.right:
        player.x = player.x + 5

def draw(background='background'):
    screen.blit(background, (0, 0))
    player.draw()



mc_pgzrun.go()
