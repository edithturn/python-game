import pygame
import time
import random
from random import randint
pygame.init()

#Music
music_hit = pygame.mixer.Sound('music/smb_bump.wav')
final_music = pygame.mixer.Sound('music/smas-smb3_peach-letter.wav')
pygame.mixer.music.load('music/SuperMarioBros.wav')


# Variables
# Colors
black = (0,0,0)
white = (255, 255, 255)
red = (188, 7, 51 )
green = (77, 122, 4)
red_sparkly = (251, 1, 61)
green_sparkly = (83, 189, 5)
# character
character_width = 73

# surface
surface_width = 1500
surface_height = 900

background_image = pygame.image.load("img/aaa.jpg")


def getRandomColors():
    return  (randint(0,255),randint(0,255),randint(0,255))


# Surface
surface = pygame.display.set_mode((surface_width, surface_height))
pygame.display.set_caption('Game01')
# Clock
reloj = pygame.time.Clock()
# Image
character = pygame.image.load('img/mbros.jpg')

# Functions
def things_dodged (count):
    letters = pygame.font.SysFont(None, 40)
    texto = letters.render("Dodged : "  + str(count), True, black )
    surface.blit(texto, (0, 0))

def  show_character(x,y):
    surface.blit(character, (x, y))

def show_blocks(xblocks, yblocks, width_block,  height_block, color):
    pygame.draw.rect(surface, color, [xblocks, yblocks, width_block, height_block ])

def objects_text(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()

def show_message(text):
    big_text = pygame.font.SysFont("comicsansms", 30)
    supertext, recttexto = objects_text(text, big_text)
    recttexto.center = ((surface_width/2), (surface_height/2)) 
    surface.blit(supertext, recttexto)
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(music_hit)
    pygame.display.update()
    time.sleep(2)
    game_loop()


def show_final_message(text):
    big_text = pygame.font.SysFont("comicsansms", 40)
    supertext, recttexto = objects_text(text, big_text)
    recttexto.center = ((surface_width/2), (surface_height/2)) 
    surface.blit(supertext, recttexto)
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(final_music)        
    pygame.display.update()        
    time.sleep(12)
    #game_loop()
   

def you_won():
      show_final_message("bla")
      

def touch_front():
    show_message("You hit!!!")
    




def button(msg, x, y, width, height , button_inactive, button_active, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed() 
        print(click)
        #print(mouse)

        if x+width  > mouse[0] and y+height > mouse[1] > y:
            pygame.draw.rect(surface, button_active, (x,y, width, height))
            if  click[0] == 1 and action != None:
                if action == "Play!":
                    game_loop()
                elif action == "Exit!":
                    pygame.quit()
                    quit()
        else:
            pygame.draw.rect(surface, button_inactive, (x,y, width, height))
      
        big_text = pygame.font.SysFont("comicsansms", 30)
        supertext, recttexto = objects_text(msg, big_text)
        recttexto.center = ((x+(width/2)), (y+(height/2)) )
        surface.blit(supertext, recttexto)
        mouse = pygame.mouse.get_pos()

def game_into():
    surface.blit(background_image, (0, 0))
    pygame.mixer.music.play(1)
    intro = True
    surface.blit(background_image, (0, 0))
    while  intro:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            #screen.blit(background_image, [0, 0])
            big_text = pygame.font.SysFont("comicsansms", 30)
            supertext, recttexto = objects_text("Get 10 points, there is a message for you at the end!", big_text)
            recttexto.center = ((surface_width/2), (surface_height/2)) 
            surface.blit(supertext, recttexto)

            button("Go!", 150, 450, 100, 50 , green, green_sparkly, "Play!")
            button("Exit!", 550, 450, 100, 50 , red, red_sparkly, "Exit!")          

            pygame.display.update()
            reloj.tick(15)


def game_loop():
    # Background
    surface.blit(background_image, (0, 0))
    #Music
    pygame.mixer.music.play(1)

    x = (surface_width * .45)
    y = (surface_height * 0.769)
    # Image changes
    x_change = 0
    # blocks
    start_xblocks = random.randrange(0, surface_width)
    start_yblocks =  -600
    block_speed = 5
    width_block =  100
    height_block = 100
    game_exit = False
    dodged = 0


    # Game
    while not game_exit:
        
        #pygame.mixer.music.play(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if  event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change =  5
            if event.type  == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change
        #surface.fill(white)
        show_blocks(start_xblocks, start_yblocks, width_block, height_block, getRandomColors() )
        start_yblocks += block_speed
        show_character (x, y)
        things_dodged(dodged)

        # Limits
        if x > surface_width  -  character_width or x < 0:
            touch_front()
            pygame.mixer.music.stop()
        if start_yblocks > surface_width:
            start_yblocks = 0 - height_block
            start_xblocks = random.randrange(0, surface_width)
            dodged  += 1 
            block_speed += 1
            width_block += (dodged * 1.2)

        if y < start_yblocks + width_block:
            if x > start_xblocks and x < start_xblocks or x + character_width > start_xblocks and x + character_width < start_xblocks + width_block:
                touch_front()
                pygame.mixer.music.stop()

        if dodged == 11 :
            you_won()
            #TODO: Doesnt jum OMG
            #show_character(350,350)




        # Update
        pygame.display.update()
        reloj.tick(60)

# Call game
game_into()
# Call funcitons
game_loop()
quit()


