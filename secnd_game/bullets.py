import pygame
pygame.init()
win=pygame.display.set_mode((500,480))
pygame.display.set_caption('enemies game')
walk_right=[pygame.image.load('secnd_game\pics_right\R1.png'),pygame.image.load('secnd_game\pics_right\R2.png'),
            pygame.image.load('secnd_game\pics_right\R3.png'),pygame.image.load('secnd_game\pics_right\R4.png'),
            pygame.image.load('secnd_game\pics_right\R5.png'),pygame.image.load('secnd_game\pics_right\R6.png'),
            pygame.image.load('secnd_game\pics_right\R7.png'),pygame.image.load('secnd_game\pics_right\R8.png'),
            pygame.image.load('secnd_game\pics_right\R9.png')
            ]
walk_left=[pygame.image.load('secnd_game/left/L1.png'),pygame.image.load('secnd_game/left/L2.png'),
           pygame.image.load('secnd_game/left/L3.png'),pygame.image.load('secnd_game/left/L4.png'),
           pygame.image.load('secnd_game/left/L5.png'),pygame.image.load('secnd_game/left/L6.png'),
           pygame.image.load('secnd_game/left/L7.png'),pygame.image.load('secnd_game/left/L8.png'),
           pygame.image.load('secnd_game/left/L9.png'),]
bg=pygame.image.load('secnd_game\sky\sky.jpg')
char=pygame.image.load('secnd_game\sky\standing.png')
clock = pygame.time.Clock()



class Player(object):
    def __init__(self,player_x,player_y,player_width,player_height):
        self.player_x = player_x
        self.player_y = player_y
        self.player_width = player_width
        self.player_height=player_height
        self.player_move = 5
        self.isjump = False
        self.left = False
        self.right = False
        self.walk_count = 0
        self.jump_count= 10
        self.standing=True
    def draw(self,win):
      if self.walk_count + 1 >= 27:
          self.walk_count = 0
      if not (self.standing):
          if self.left:
                win.blit(walk_left[self.walk_count//3], (self.player_x,self.player_y))
                self.walk_count += 1
          elif self.right:
                win.blit(walk_right[self.walk_count//3], (self.player_x ,self.player_y))
                self.walk_count +=1

      else:
            if self.right:
                win.blit(walk_right[0], (self.player_x, self.player_y))
            else:
                win.blit(walk_left[0], (self.player_x, self.player_y))       
        
        
        
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
        
        
# player_x=250
# player_y=400
# player_width=64
# player_height=64
# player_move=5
# isjump= False
# jump_count=10
# left=False
# right=False
# walk_count=0


def redrawGameWindow():
    
    
    win.blit(bg, (0,0))
    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    
    pygame.display.update()
    
    
active=True
man = Player(200, 410, 64,64)
bullets = []
while active :
    clock.tick(27)
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
              active=False
    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LCTRL] or event.type ==pygame.MOUSEBUTTONDOWN:
        if man.left:
            facing = -1
        else:
            facing = 1
            
        if len(bullets) < 5:
            bullets.append(projectile(round(man.player_x + man.player_width //2), round(man.player_y + man.player_height//2), 6, (0,0,0), facing))    
    if keys[pygame.K_LEFT] and man.player_x > man.player_move:
        man.player_x -= man.player_move
        man.left=True
        man.right=False
        man.standing=False
    elif keys[pygame.K_RIGHT] and man.player_x <500-man.player_width-man.player_move:
        man.player_x += man.player_move  
        man.right=True
        man.left=False
        man.standing=False
    else :
        man.standing=True
        man.walk_count=0    
    if not (man.isjump) :
        
        # if keys[pygame.K_UP] and player_y > player_move:
        #     player_y -= player_move        
        # if keys[pygame.K_DOWN] and player_y <500 -player_height - player_move:
        #     player_y += player_move  
            
        if keys[pygame.K_SPACE]:
            man.isjump = True 
            man.right=False
            man.left= False
            man.walk_count=0         
                 
    else :
        if man.jump_count >= -10 :
            negative=1
            if man.jump_count <0 :
                negative=-1 
            man.player_y -= (man.jump_count**2)*0.5 *negative
            man.jump_count -=1
        else :
            man.isjump = False
            man.jump_count =10        

         
    redrawGameWindow()          
              
              
pygame.quit()
    