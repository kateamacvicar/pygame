import pygame
'''
a custom class for extracting an image from a spritesheet
'''
class Spritesheet():
    def __init__(self,image):
        self.sheet = image

    '''
    we can use this method to get different animations and poses from a spritesheet
    '''  
    def get_image(self, frame, width, height, scale, color):
        #create a blank surface
        image = pygame.Surface((width, height)).convert_alpha()
        image.fill((179, 190, 207))
        #blit a certain portion of the sheet onto our blank surface
        #blit determines the section of the spritesheet we want.
        image.blit(self.sheet, (0,0), ((frame * width),0, width, height))
        image = pygame.transform.scale(image, (width* scale, height*scale))
        #get rid of the extra blackness around the sprite
        image.set_colorkey(color)
        #self.speed = speed
        #create the collision box
        # self.rect = image.get_rect()
        # self.rect.center = (0,0)
        return image
    
    # def move(self, moving_left, moving_right):
    #     #reset movement variables
    #     dx=0
    #     dy=0
    #     #assign movement variables if moving left or right
    #     if moving_left:
    #         dx = -5
    #     if moving_right:
    #         dx = +5

    #     #update rectangle
    #         self.rect.x += dx
    #         self.rect.y += dy
