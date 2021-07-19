import pygame
pygame.init() 

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption(" Racing Game")
carryOn = True
chk=pygame.Rect(100,450,20,20)

carx=130
cary=500


while carryOn:
    for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                  carryOn = False
    bgImg_location= "C:/Users/dell/Documents/img/back_ground.jpg"             
    bgImg=pygame.image.load(bgImg_location).convert_alpha()
    bgImg_scaled=pygame.transform.smoothscale(bgImg,(600,600))
    screen.blit(bgImg_scaled,[0,0])
    car2Img_location="C:/Users/dell/Documents/img/car2.png"
    car2Img=pygame.image.load(car2Img_location).convert_alpha()
    screen.blit(car2Img,[250,500])
    obsImg_location="C:/Users/dell/Documents/img/stone3.png"
    obsImg=pygame.image.load(obsImg_location).convert_alpha()
    obsImg_scaled=pygame.transform.scale(obsImg,[70,70])
    screen.blit(obsImg_scaled,[250,300])
    
    pygame.display.flip()
    
    
pygame.quit()
