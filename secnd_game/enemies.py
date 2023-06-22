
import pygame
from player import Player,move_player
pygame.init()
win=pygame.display.set_mode((1280,720))
pygame.display.set_caption('enemies game')

bg=pygame.image.load('secnd_game\sky\pic3.webp')
char=pygame.image.load('secnd_game\sky\standing.png')
clock = pygame.time.Clock()




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
        
        
class Enemy(object):
    '''
    enemy class
    '''
    walkRight = [pygame.image.load('secnd_game\enemie\R1E.png'), pygame.image.load('secnd_game\enemie\R2E.png'), 
                 pygame.image.load('secnd_game\enemie\R3E.png'),
                 pygame.image.load('secnd_game\enemie\R4E.png'), pygame.image.load('secnd_game\enemie\R5E.png'), 
                 pygame.image.load('secnd_game\enemie\R6E.png'),
                 pygame.image.load('secnd_game\enemie\R7E.png'), pygame.image.load('secnd_game\enemie\R8E.png'), 
                 pygame.image.load('secnd_game\enemie\R9E.png'),
                 pygame.image.load('secnd_game\enemie\R10E.png'), pygame.image.load('secnd_game\enemie\R11E.png')]
    walkLeft = [pygame.image.load('secnd_game\enemie\L1E.png'), pygame.image.load('secnd_game\enemie\L2E.png'),
                pygame.image.load('secnd_game\enemie\L3E.png'),
                pygame.image.load('secnd_game\enemie\L4E.png'), pygame.image.load('secnd_game\enemie\L5E.png'),
                pygame.image.load('secnd_game\enemie\L6E.png'),
                pygame.image.load('secnd_game\enemie\L7E.png'), pygame.image.load('secnd_game\enemie\L8E.png'),
                pygame.image.load('secnd_game\enemie\L9E.png'), 
                pygame.image.load('secnd_game\enemie\L10E.png'), pygame.image.load('secnd_game\enemie\L11E.png')]
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        
    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        
        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        pygame.draw.rect(win, (255,0,0), self.hitbox,2)           
    def move(self):
        if self.vel > 0:
            # if player.
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
    def hit(self):
        print('hit')

def redrawGameWindow():
    
    
    win.blit(bg,(0,0))
    player_one.draw(win)
    player_two.draw(win)
    # first_enemy.draw(win)
    # sec_enemy.draw(win)
    # for bullet in bullets:
    #     bullet.draw(win)
    
    pygame.display.update()
    
    
active=True
player_one = Player(200, 537, 64,64,'player_one')
player_two=Player(200, 537, 64,64,'player_two')


first_enemy= Enemy(100, 537, 64, 64, 300)
sec_enemy=Enemy(30, 537, 64, 64, 450)
# bullets = []


pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for joystick in joysticks:
    print(joystick.get_name())

while active :
    clock.tick(27)
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
              active=False

                                       
              
    move_player(player_one)
    move_player(player_two)           
              

    redrawGameWindow()          
              
              
pygame.quit()
    
