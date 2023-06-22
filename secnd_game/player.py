import pygame



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



class Player(object):
    def __init__(self,player_x,player_y,player_width,player_height,name=None):
        self.player_x = player_x
        self.player_y = player_y
        self.player_width = player_width
        self.player_height=player_height
        self.player_velocity = 5
        self.isjump = False
        self.left = False
        self.right = False
        self.walk_count = 0
        self.jump_count= 10
        self.standing=True
        self.hitbox = (self.player_x + 17, self.player_y + 11, 29, 52)
        self.name=name
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
        
      self.hitbox = (self.player_x + 17, self.player_y + 11, 29, 52)
      
      pygame.draw.rect(win, (255,0,0), self.hitbox,2)

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for joystick in joysticks:
    print(joystick.get_name())
    

def move_player(player):
    
   keys=pygame.key.get_pressed()
 
   if player.name == 'player_one':
         
        if keys[pygame.K_LEFT]  :
            player.player_x -= player.player_velocity
            player.left=True
            player.right=False
            player.standing=False
        
        elif keys[pygame.K_RIGHT]  :
            player.player_x += player.player_velocity  
            player.right=True
            player.left=False
            player.standing=False
        else :
            player.standing=True
            player.walk_count=0    
        if not (player.isjump) :
            

            if keys[pygame.K_UP] :
                player.isjump = True 
                player.right=False
                player.left= False
                player.walk_count=0         
                    
        else :
            if player.jump_count >= -10 :
                negative=1
                if player.jump_count <0 :
                    negative=-1 
                player.player_y -= (player.jump_count**2)*0.3 *negative
                player.jump_count -=1
            else :
                player.isjump = False
                player.jump_count =10        
   elif player.name == 'player_two':

  
    if keys[pygame.K_a] :
        player.player_x -= player.player_velocity
        player.left=True
        player.right=False
        player.standing=False
    elif keys[pygame.K_d] :
        player.player_x += player.player_velocity  
        player.right=True
        player.left=False
        player.standing=False
    else :
        player.standing=True
        player.walk_count=0    
    if not (player.isjump) :
        

        if keys[pygame.K_SPACE]:
            player.isjump = True 
            player.right=False
            player.left= False
            player.walk_count=0         
                 
    else :
        if player.jump_count >= -10 :
            negative=1
            if player.jump_count <0 :
                negative=-1 
            player.player_y -= (player.jump_count**2)*0.3 *negative
            player.jump_count -=1
        else :
            player.isjump = False
            player.jump_count =10        
        
    
        