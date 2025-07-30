import pygame 

class Paddle:
    def __init__(self,width,height):
        paddle_image= pygame.image.load("paddle_image.png")
        self.image= pygame.transform.smoothscale(paddle_image,(100,20))
        self.rect = self.image.get_rect()
        self.rect.centerx = width//2
        self.rect.bottom = height - 25
        self.velocity=15 

    def update(self,event):
        #Paddle movement left to right
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                self.rect.x -= self.velocity
            
            if event.key == pygame.K_RIGHT:
                self.rect.x += self.velocity

    def draw(self,screen):
        screen.blit(self.image,self.rect)

