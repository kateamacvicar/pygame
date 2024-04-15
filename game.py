import pygame
import spritesheet
from player import Player

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheet')

clock = pygame.time.Clock()
FPS = 60

scroll = 0
moving_left = False
moving_right=False
moving_up = False

#set up the background
bg_images = []
for i in range(1,5):
    bg_image = pygame.image.load(f"assets/background/background-{i}.png").convert_alpha()
    bg_images.append(bg_image)

bg_width = bg_images[0].get_width()

#function to draw my bacground images on the screen
def draw_bg():
    for x in range(100):
        speed = 1
        for i in bg_images:
            screen.blit(i,((x *bg_width) - scroll * speed,0))
            speed += 0.1

#create an instance of our player
#the 'player' bit is good for if you have multiple different sprites. But I only have the one. Right now that doesnt really do anything
player = Player('player', 200, 650, 1, 0.4)

#set up pygame window
# sprite_sheet_image = pygame.image.load('assets/idle_spritesheet.png').convert_alpha()
# #extract our image from the spritesheet
# sprite_sheet = spritesheet.Spritesheet(sprite_sheet_image)
# TRANS = (179, 190, 207)

# #create animation list
# animation_list = []
# #the sprite sheet is composed of different "actions" like walking, jumping, attakcing, etc. 
# #len of array is how many actions. Number dneotes how many frames within that action
# #i have one action- idle, with 2 frames
# animation_steps = 5
# action = 0
# last_update = pygame.time.get_ticks()
# animation_cooldown = 800
# frame = 0
# step_counter = 0

# #x is each frame within the action
# for x in range(animation_steps):
#     animation_list.append(sprite_sheet.get_image(x,250,280,1,TRANS))

run = True
while run:
    clock.tick(FPS)

    #draw on our background images
    draw_bg()
    #set up our player
    player.draw(screen)
    player.move(moving_left, moving_right, moving_up)

    #update animation
    player.update_animation()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and scroll > 0:
                moving_left = True
            if event.key == pygame.K_RIGHT and scroll < 3000:
                moving_right = True
            if event.key == pygame.K_SPACE:
                moving_up = True
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_SPACE:
                moving_right=False
                moving_left=False
                moving_up = False

    if moving_left:
        scroll -= 5
    if moving_right:
        scroll += 5
       
    pygame.display.update()

pygame.quit()