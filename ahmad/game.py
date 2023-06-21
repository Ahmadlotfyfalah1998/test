import pygame
from sys import exit

def display_score():
    current_time=int(pygame.time.get_ticks()/1000) - start_time
    score_surface=test_font.render(f'score {current_time}',False,(64,64,64))
    score_rect=score_surface.get_rect(center=(400,50))
    screen.blit(score_surface,score_rect)
pygame.init()
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption('runner')
clock=pygame.time.Clock()
test_font=pygame.font.Font('ahmad\line\Pixeltype (1).ttf',50)

game_active=True
start_time=0
ground_surface=pygame.image.load('ahmad\pics\ground and sky\ground.png').convert()
sky_surface=pygame.image.load('ahmad\pics\ground and sky\Sky.png').convert()

# score_surface=test_font.render('my game',False,'Black')
# score_rect=score_surface.get_rect(center=(400,50))

snail_surface=pygame.image.load('ahmad\pics\snail\snail1.png').convert_alpha()
snail_rect=snail_surface.get_rect(midbottom=(600,300))

player_surface=pygame.image.load('ahmad\pics\player\player_walk_1.png').convert_alpha()
player_rect=player_surface.get_rect(midbottom=(80,300))

player_stand=pygame.image.load('ahmad\pics\player\player_stand.png').convert_alpha()
player_stand_rect=player_stand.get_rect(center=(400,200))
player_gravity=0
snail_x_position=600

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for joystick in joysticks:
    print(joystick.get_name())




while True:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if game_active: 
            if event.type == pygame.JOYBUTTONDOWN:
                 print(event)   
            if event.type == pygame.JOYHATMOTION:
                print(event)
            if event.type == pygame.JOYAXISMOTION:
                print(event)         
            if event.type ==pygame.KEYDOWN and player_rect.bottom==300:
                if event.key==pygame.K_SPACE:
                    player_gravity=-20
            if event.type ==pygame.MOUSEBUTTONDOWN and player_rect.bottom==300:
                if player_rect.collidepoint(event.pos):
                    player_gravity=-20
                    
            if event.type ==pygame.JOYBUTTONDOWN and player_rect.bottom==300:
                 if event.button == 0:
                    player_gravity=-20   
            if event.type ==pygame.JOYHATMOTION and player_rect.bottom==300:
                 if event.value == (1,0):
                    player_gravity=-20   

                           
        else: 
            if event.type ==pygame.KEYDOWN :
              if event.key==pygame.K_r:  
                game_active=True  
                snail_rect.left=800  
                start_time=int(pygame.time.get_ticks()/1000)
    if game_active:      
        screen.blit(sky_surface,(0,0))        
        screen.blit(ground_surface,(0,300))
        display_score()
        # screen.blit(score_surface,score_rect)
        snail_rect.x -=7
        if snail_rect.left< -100:
            snail_rect.left=800
    
        screen.blit(snail_surface,snail_rect) 
        # player
        player_gravity+=1
        player_rect.y+=player_gravity
        if player_rect.bottom >=300:
            player_rect.bottom=300
        screen.blit(player_surface,player_rect)
        # coll
        if snail_rect.colliderect(player_rect):
           game_active=False
    else:
        screen.fill('Red')
        screen.blit(player_stand,player_stand_rect)
    pygame.display.update()
    clock.tick(60)