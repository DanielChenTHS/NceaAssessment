import mc_pgzrun
from pgzhelper import *
import random
import sys
import pygame

pygame.init()

clock = pygame.time.Clock()

WIDTH = 564
HEIGHT = 764

screen_width = 564
screen_height = 764
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Click To Begin The Game")

font = pygame.font.SysFont("segoeui", 30)
smallfont = pygame.font.SysFont("segoeui", 14)
slategray = (112, 128, 144)
lightgray = (165, 175, 185)
blackish = (10, 10, 10)
#background_image = 'background'

player = Actor('player')
player.x = 282
player.y = 724

can = Actor('can')
can.x = random.randint(20, 544)
can.y = 0

game_over = False
score = 0
#  end of initialisation section #


#  Function definitions begin here  #

def create_button(msg, x, y, width, height, hovercolor, defaultcolor):

    mouse = pygame.mouse.get_pos()
    # assume that the mouse has 3 buttons that can be clicked
    click = pygame.mouse.get_pressed(3)
    if x+width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen,hovercolor, (x, y, width, height))
        if click[0] == 1:  # left button clicked
            start()  # first_level is the function where the main game starts
    else:
        pygame.draw.rect(screen, defaultcolor, (x, y, width, height))

    start_button_text = smallfont.render(msg, True, blackish)
    screen.blit(start_button_text, (int(780 + (width/2)), int(y + (y/2))))

def start_menu():
    """
    This function displays the splash screen.
    The screen includes a button to click on that starts the main game

    :return:
    """
    start_text = font.render("Catch The Rubbish", True, slategray)
    while True:
        screen.fill((0, 100, 10))
        screen.blit(start_text, ((screen_width - start_text.get_width()) / 2, 0))
        create_button("Start", screen_width - 130, 7, 125, 26, lightgray, slategray)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)
        return True

def start():
    """
    def first_level is the function for the main game.
    This function has its own game loop.
    At this stage all it does is display "Playing the game now"

    :return: Null
    """
    start_text = font.render("Playing the game now", True, slategray)
    while True:
        screen.blit("background", (0,0))
        screen.blit(start_text, ((screen_width - start_text.get_width()) / 2, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)

def update():
    global score, game_over

    if keyboard.left:
        player.x = player.x - 5
        if player.x < 10:
            player.x = 10

    if keyboard.right:
        player.x = player.x + 5
        if player.x > (screen_width - 10):
            player.x = 554

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


def on_key_down(key):
    if key == keys.F:
        screen.surface = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    elif key == keys.W:
        screen.surface = pygame.display.set_mode((screen_width, screen_height))

while True:
    start_menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(15)
