import pygame

class Text:

    def __init__(self, message):
        self.font = pygame.font.Font("freesansbold.ttf", 30)
        self.message = message

        #what we will be taking out of the message as we scroll through it
        self.snip = self.font.render('', True, 'white')
        self.counter = 0
        self.speed = 3
        self.is_done = False

    def animate(self):
        #check if we have written the entire message onto the screen yet
        if self.counter < self.speed * len(self.message):
            #if not....
            self.counter += 1
        elif self.counter >= self.speed* len(self.message):
            self.is_done = True

        self.snip = self.font.render(self.message[0:self.counter//self.speed], True, 'white')
        return self.snip