import pygame 
from paddle_design import Paddle 

# Initialize pygame
pygame.init()

# Screen settings
WIDTH,HEIGHT = 600,600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Paddle Movement")

# Create the character 
paddle=Paddle(WIDTH,HEIGHT)

# Gameloop
running=True 
clock=pygame.time.Clock()

while running:
    screen.fill("black") # Black screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False 

        paddle.update(event)
    
    paddle.draw(screen)

    pygame.display.update()
    clock.tick(30)

pygame.quit()