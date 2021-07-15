import pygame
pygame.init() 

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption(" Racing Game")
carryOn = True



while carryOn:
    for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                  carryOn = False
    bgImg_location= "C:/Users/dell/Documents/img/back_ground.jpg"             
    bgImg=pygame.image.load(bgImg_location).convert_alpha()
    bgImg_scaled=pygame.transform.smoothscale(bgImg,(600,600))
    screen.blit(bgImg_scaled,[0,0])
    carImg_location="C:/Users/dell/Documents/img/car.png"
    carImg=pygame.image.load(carImg_location).convert_alpha()
    screen.blit(carImg,[130,500])
    car2Img_location="C:/Users/dell/Documents/img/car2.png"
    car2Img=pygame.image.load(car2Img_location).convert_alpha()
    screen.blit(car2Img,[250,500])
    
    pygame.display.flip()
    
    
pygame.quit()
