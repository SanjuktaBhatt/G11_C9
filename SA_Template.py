import pygame
pygame.init() 

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption(" Racing Game")
carryOn = True
while carryOn:
    for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                  carryOn = False
    #Change location of background image according to the absolute path you have got in your computer
    bgImg_location= ""             
    bgImg=pygame.image.load(bgImg_location).convert_alpha()
    bgImg_scaled=pygame.transform.smoothscale(bgImg,(600,600))
    screen.blit(bgImg_scaled,[0,0])
    
    #Create a variable "carImg_location" to store absolute path of car image on your computer
    
    #Load the car image into a variable "carImg"  and use convert_alpha() to convert to compatible pixel format
   
    #Display the car image at location (130,500)
   
    
    pygame.display.flip()
    
pygame.quit()
