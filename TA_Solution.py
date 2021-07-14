#Acitivity 1
#Import pygame
import pygame
#Initialize pygame
pygame.init() 
#Create a screen
screen = pygame.display.set_mode((600,600))
#Set a caption to the screen
pygame.display.set_caption(" Racing Game")
#Begin the game loop
carryOn = True
while carryOn:
    for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                  carryOn = False 
    #Activity 2
    #Load the background image
    bgImg=pygame.image.load("C:/Users/dell/Documents/img/back_ground.jpg").convert_alpha()
    #Scale the background image
    bgImg_scaled=pygame.transform.smoothscale(bgImg,(600,600))
    #Display background image on screen
    screen.blit(bgImg_scaled,[0,0])
    #Update the display
    pygame.display.flip()
    
#Quit the game outside the loop   
pygame.quit()
