import pygame as pygame

def MoveBall():
    """
    This function will move the ball
    """
    pass

def MovePaddle():
    """
    Moves the paddle up and down but not off the screen
    """
    pass

timer = pygame.time.Clock()

window = pygame.display.set_mode([320, 240])

while True:
    timer.tick(60)
    #check quit event
    #check up, down, spacebar event