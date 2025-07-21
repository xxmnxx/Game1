import pygame
from sys import exit
#initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Run! Run! Run!")

# Set up the clock for frame rate control
clock = pygame.time.Clock()

# Set up the font for text rendering
test_font = pygame.font.Font('font/Pixeltype.ttf',50)

# Load the background image
sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = test_font.render('My game', False, 'Black')
while True:
    #check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0,0)) # draw the sky first
    screen.blit(ground_surface, (0,300)) # draw the ground second
    screen.blit(text_surface, (300,50))

    pygame.display.update() # update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS