import pygame

class Text:

    def __init__(self, message):
        self.font = pygame.font.Font("freesansbold.ttf", 14)
        self.text_timet = pygame.time.Clock()
        self.message = message

        #what we will be taking out of the message as we scroll through it
        self.snip = self.font.render('', True, 'white')
        self.counter = 0
        self.speed = 3
        self.is_done = False