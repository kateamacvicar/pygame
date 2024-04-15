import pygame

class Player(pygame.sprite.Sprite, ):

    def __init__(self, char_type, x, y,scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type #this defines the image we look at
        self.speed = speed #assign the argument to the instance itself so that they can be unique to the instance
        self.direction = 1
        self.flip = False
        self.animation_list = []
        self.frame_index=0
        self.update_time = pygame.time.get_ticks()

        for i in range(5):
            img = pygame.image.load(f'assets/idle/player_idle_{i}.png')
            #img = pygame.image.load(f'assets/{self.char_type}) or whatever LOL
            img = pygame.transform.scale(img, (int(img.get_width())*scale, int(img.get_height())*scale))
            #adds the list that we just loaded into the list. at the end of the loop we will have a list full of images
            self.animation_list.append(img)

        self.image = self.animation_list[self.frame_index] #starting with the first image
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    #allows me to control my player
    def move(self, moving_left, moving_right, moving_up):
        #reset movement variables
        dx=0
        dy=0
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1

        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        if moving_up:
            dy = self.speed

        self.rect.x += dx
        self.rect.y += dy

    def update_animation(self):
        ANIMATION_COOLDOWN = 100
        #update image depending on current frae
        self.image = self.animation_list[self.frame_index]
        #update animation
        current_time = pygame.time.get_ticks()

        #if it has time to cooldown.. so if 500 milliseconds have passed, then we can move onto the next frame
        if current_time - self.update_time > ANIMATION_COOLDOWN:
            self.frame_index += 1
            self.update_time = current_time
            if self.frame_index >= len(self.animation_list):
                self.frame_index = 0
        



    def draw(self, screen):
        #the False is saying we dont want to flip on the y axis. AKA we dont want it to be upside down
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
