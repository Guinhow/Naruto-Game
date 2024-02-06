import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 800
altura = 400

font = pygame.font.SysFont('arial', 20, True, False)
hpBar1 = 0
hpBar2 = 0
points1 = 0
points2 = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Naruto")

pause = False

x_sprite = 70
y_sprite = 180

x_sprite2 = 620
y_sprite2 = 160

#background

back = pygame.image.load('fundo.png')
back2 = pygame.image.load('gameover.png')

#stand right

stand1 = pygame.image.load('stand/standright1.png')
stand2 = pygame.image.load('stand/standright2.png')
stand3 = pygame.image.load('stand/standright3.png')

stand1 = pygame.transform.scale(stand1, (50*2,80*2))
stand2 = pygame.transform.scale(stand2, (50*2,80*2))
stand3 = pygame.transform.scale(stand3, (50*2,80*2))

stand = [stand1, stand2, stand3]
ind_stand = 0

#stand left

standleft1 = pygame.image.load('stand/standleft1.png')
standleft2 = pygame.image.load('stand/standleft2.png')
standleft3 = pygame.image.load('stand/standleft3.png')
standleft4 = pygame.image.load('stand/standleft4.png')
standleft5 = pygame.image.load('stand/standleft5.png')
standleft6 = pygame.image.load('stand/standleft6.png')

standleft1 = pygame.transform.scale(standleft1, (40*3,60*3))
standleft2 = pygame.transform.scale(standleft2, (40*3,60*3))
standleft3 = pygame.transform.scale(standleft3, (40*3,60*3))
standleft4 = pygame.transform.scale(standleft4, (40*3,60*3))
standleft5 = pygame.transform.scale(standleft5, (40*3,60*3))
standleft6 = pygame.transform.scale(standleft6, (40*3,60*3))

standleft = [standleft1, standleft2, standleft3, standleft4, standleft5, standleft6]
ind_standleft = 0

#run right

runright1 = pygame.image.load('run/runright1.png')
runright2 = pygame.image.load('run/runright2.png')
runright3 = pygame.image.load('run/runright3.png')
runright4 = pygame.image.load('run/runright4.png')
runright5 = pygame.image.load('run/runright5.png')
runright6 = pygame.image.load('run/runright6.png')

runright1 = pygame.transform.scale(runright1, (50*2,80*2))
runright2 = pygame.transform.scale(runright2, (50*2,80*2))
runright3 = pygame.transform.scale(runright3, (50*2,80*2))
runright4 = pygame.transform.scale(runright4, (50*2,80*2))
runright5 = pygame.transform.scale(runright5, (50*2,80*2))
runright6 = pygame.transform.scale(runright6, (50*2,80*2))

runright = [runright1, runright2, runright3, runright4, runright5, runright6]
ind_runright = 0

runright11 = pygame.image.load('run/runright11.png')
runright12 = pygame.image.load('run/runright12.png')
runright13 = pygame.image.load('run/runright13.png')
runright14 = pygame.image.load('run/runright14.png')
runright15 = pygame.image.load('run/runright15.png')
runright16 = pygame.image.load('run/runright16.png')

runright11 = pygame.transform.scale(runright11, (50*3,60*3))
runright12 = pygame.transform.scale(runright12, (50*3,60*3))
runright13 = pygame.transform.scale(runright13, (50*3,60*3))
runright14 = pygame.transform.scale(runright14, (50*3,60*3))
runright15 = pygame.transform.scale(runright15, (50*3,60*3))
runright16 = pygame.transform.scale(runright16, (50*3,60*3))

runright0 = [runright11, runright12, runright13, runright14, runright15, runright16]
ind_runright0 = 0

#run left

runleft1 = pygame.image.load('run/runleft1.png')
runleft2 = pygame.image.load('run/runleft2.png')
runleft3 = pygame.image.load('run/runleft3.png')
runleft4 = pygame.image.load('run/runleft4.png')
runleft5 = pygame.image.load('run/runleft5.png')
runleft6 = pygame.image.load('run/runleft6.png')

runleft1 = pygame.transform.scale(runleft1, (50*2,80*2))
runleft2 = pygame.transform.scale(runleft2, (50*2,80*2))
runleft3 = pygame.transform.scale(runleft3, (50*2,80*2))
runleft4 = pygame.transform.scale(runleft4, (50*2,80*2))
runleft5 = pygame.transform.scale(runleft5, (50*2,80*2))
runleft6 = pygame.transform.scale(runleft6, (50*2,80*2))

runleft = [runleft1, runleft2, runleft3, runleft4, runleft5, runleft6]
ind_runleft = 0

runleft11 = pygame.image.load('run/runleft11.png')
runleft12 = pygame.image.load('run/runleft12.png')
runleft13 = pygame.image.load('run/runleft13.png')
runleft14 = pygame.image.load('run/runleft14.png')
runleft15 = pygame.image.load('run/runleft15.png')
runleft16 = pygame.image.load('run/runleft16.png')

runleft11 = pygame.transform.scale(runleft11, (50*3,60*3))
runleft12 = pygame.transform.scale(runleft12, (50*3,60*3))
runleft13 = pygame.transform.scale(runleft13, (50*3,60*3))
runleft14 = pygame.transform.scale(runleft14, (50*3,60*3))
runleft15 = pygame.transform.scale(runleft15, (50*3,60*3))
runleft16 = pygame.transform.scale(runleft16, (50*3,60*3))

runleft0 = [runleft11, runleft12, runleft13, runleft14, runleft15, runleft16]
ind_runleft0 = 0

#jump

jump1 = pygame.image.load('jump/jump1.png')
jump2 = pygame.image.load('jump/jump1.png')
jump3 = pygame.image.load('jump/jump2.png')
jump4 = pygame.image.load('jump/jump2.png')
jump5 = pygame.image.load('jump/jump3.png')
jump6 = pygame.image.load('jump/jump3.png')
jump7 = pygame.image.load('jump/jump4.png')
jump8 = pygame.image.load('jump/jump4.png')

jump1 = pygame.transform.scale(jump1, (50*2,80*2))
jump2 = pygame.transform.scale(jump2, (50*2,80*2))
jump3 = pygame.transform.scale(jump3, (50*2,80*2))
jump4 = pygame.transform.scale(jump4, (50*2,80*2))
jump5 = pygame.transform.scale(jump5, (50*2,80*2))
jump6 = pygame.transform.scale(jump6, (50*2,80*2))
jump7 = pygame.transform.scale(jump7, (50*2,80*2))
jump8 = pygame.transform.scale(jump8, (50*2,80*2))

jump = [jump1, jump2, jump3, jump4, jump5, jump6, jump7, jump8]
ind_jump = 0

jump11 = pygame.image.load('jump/jump11.png')
jump12 = pygame.image.load('jump/jump11.png')
jump13 = pygame.image.load('jump/jump12.png')
jump14 = pygame.image.load('jump/jump12.png')
jump15 = pygame.image.load('jump/jump13.png')
jump16 = pygame.image.load('jump/jump13.png')
jump17 = pygame.image.load('jump/jump14.png')
jump18 = pygame.image.load('jump/jump14.png')

jump11 = pygame.transform.scale(jump11, (60*3,70*3))
jump12 = pygame.transform.scale(jump12, (60*3,70*3))
jump13 = pygame.transform.scale(jump13, (60*3,70*3))
jump14 = pygame.transform.scale(jump14, (60*3,70*3))
jump15 = pygame.transform.scale(jump15, (60*3,70*3))
jump16 = pygame.transform.scale(jump16, (60*3,70*3))
jump17 = pygame.transform.scale(jump17, (60*3,70*3))
jump18 = pygame.transform.scale(jump18, (60*3,70*3))

jump0 = [jump11, jump12, jump13, jump14, jump15, jump16, jump17, jump18]
ind_jump0 = 0

velocidade_y = 0
gravidade = 4
pulo = -20  

no_ar = False  

velocidade_y2 = 0
no_ar2 = False  


#duck

duck1 = pygame.image.load('jump/duck1.png')
duck2 = pygame.image.load('jump/duck1.png')
duck3 = pygame.image.load('jump/duck1.png')
duck4 = pygame.image.load('jump/duck1.png')
duck5 = pygame.image.load('jump/duck1.png')
duck6 = pygame.image.load('jump/duck1.png')

duck1 = pygame.transform.scale(duck1, (50*2,80*2))
duck2 = pygame.transform.scale(duck2, (50*2,80*2))
duck3 = pygame.transform.scale(duck3, (50*2,80*2))
duck4 = pygame.transform.scale(duck4, (50*2,80*2))
duck5 = pygame.transform.scale(duck5, (50*2,80*2))
duck6 = pygame.transform.scale(duck6, (50*2,80*2))

duck = [duck1, duck2, duck3, duck4, duck5, duck6]
ind_duck = 0

duck11 = pygame.image.load('jump/duck11.png')
duck12 = pygame.image.load('jump/duck11.png')
duck13 = pygame.image.load('jump/duck11.png')
duck14 = pygame.image.load('jump/duck11.png')
duck15 = pygame.image.load('jump/duck11.png')
duck16 = pygame.image.load('jump/duck11.png')

duck11 = pygame.transform.scale(duck11, (60*3,70*3))
duck12 = pygame.transform.scale(duck12, (60*3,70*3))
duck13 = pygame.transform.scale(duck13, (60*3,70*3))
duck14 = pygame.transform.scale(duck14, (60*3,70*3))
duck15 = pygame.transform.scale(duck15, (60*3,70*3))
duck16 = pygame.transform.scale(duck16, (60*3,70*3))

duck0 = [duck11, duck12, duck13, duck14, duck15, duck16]
ind_duck0 = 0

#attack

punch1 = pygame.image.load('attack/punch1.png')
punch2 = pygame.image.load('attack/punch2.png')

punch1 = pygame.transform.scale(punch1, (50*2,80*2))
punch2 = pygame.transform.scale(punch2, (50*2,80*2))

punch = [punch1, punch2]
ind_punch = 0

kick1 = pygame.image.load('attack/kick1.png')
kick2 = pygame.image.load('attack/kick1.png')
kick3 = pygame.image.load('attack/kick1.png')
kick4 = pygame.image.load('attack/kick2.png')
kick5 = pygame.image.load('attack/kick2.png')
kick6 = pygame.image.load('attack/kick2.png')

kick1 = pygame.transform.scale(kick1, (50*2,80*2))
kick2 = pygame.transform.scale(kick2, (50*2,80*2))
kick3 = pygame.transform.scale(kick3, (50*2,80*2))
kick4 = pygame.transform.scale(kick4, (50*2,80*2))
kick5 = pygame.transform.scale(kick5, (50*2,80*2))
kick6 = pygame.transform.scale(kick6, (50*2,80*2))

kick = [kick1, kick2, kick3, kick4, kick5, kick6]
ind_kick = 0

#JIRAYA FROG

frog1 = pygame.image.load('attack/frog1.png')
frog2 = pygame.image.load('attack/frog2.png')
frog3 = pygame.image.load('attack/frog3.png')
frog4 = pygame.image.load('attack/frog4.png')
frog5 = pygame.image.load('attack/frog5.png')
frog6 = pygame.image.load('attack/frog6.png')
frog7 = pygame.image.load('attack/frog7.png')
frog8 = pygame.image.load('attack/frog8.png')

frog1 = pygame.transform.scale(frog1, (80*3,80*3))
frog2 = pygame.transform.scale(frog2, (80*3,80*3))
frog3 = pygame.transform.scale(frog3, (120*3,80*3))
frog4 = pygame.transform.scale(frog4, (120*3,80*3))
frog5 = pygame.transform.scale(frog5, (150*3,80*3))
frog6 = pygame.transform.scale(frog6, (150*3,80*3))
frog7 = pygame.transform.scale(frog7, (150*3,80*3))
frog8 = pygame.transform.scale(frog8, (150*3,80*3))

frog = [frog1, frog2, frog3, frog4, frog5, frog6, frog7, frog8]
ind_frog = 0

#hit

hit1 = pygame.image.load('damage/hit1.png')
hit2 = pygame.image.load('damage/hit2.png')
hit3 = pygame.image.load('damage/hit3.png')
hit4 = pygame.image.load('damage/hit4.png')
hit5 = pygame.image.load('damage/hit5.png')
hit6 = pygame.image.load('damage/hit6.png')
hit7 = pygame.image.load('damage/hit7.png')
hit8 = pygame.image.load('damage/hit8.png')

hit1 = pygame.transform.scale(hit1, (60*2,80*2))
hit2 = pygame.transform.scale(hit2, (60*2,80*2))
hit3 = pygame.transform.scale(hit3, (60*2,80*2))
hit4 = pygame.transform.scale(hit4, (60*2,80*2))
hit5 = pygame.transform.scale(hit5, (60*2,80*2))
hit6 = pygame.transform.scale(hit6, (60*2,80*2))
hit7 = pygame.transform.scale(hit7, (60*2,80*2))
hit8 = pygame.transform.scale(hit8, (80*2,80*2))

hit = [hit1, hit2, hit3, hit4, hit5, hit6, hit7, hit8]
ind_hit = 0


hit11 = pygame.image.load('damage/hit11.png')
hit12 = pygame.image.load('damage/hit12.png')
hit13 = pygame.image.load('damage/hit13.png')
hit14 = pygame.image.load('damage/hit14.png')
hit15 = pygame.image.load('damage/hit15.png')
hit16 = pygame.image.load('damage/hit16.png')
hit17 = pygame.image.load('damage/hit17.png')

hit11 = pygame.transform.scale(hit11, (50*3,70*3))
hit12 = pygame.transform.scale(hit12, (50*3,70*3))
hit13 = pygame.transform.scale(hit13, (50*3,70*3))
hit14 = pygame.transform.scale(hit14, (60*3,70*3))
hit15 = pygame.transform.scale(hit15, (60*3,70*3))
hit16 = pygame.transform.scale(hit16, (60*3,70*3))
hit17 = pygame.transform.scale(hit17, (60*3,70*3))

hit0 = [hit11, hit12, hit13, hit14, hit15, hit16, hit17]
ind_hit0 = 0

#DEAD
dead1 = pygame.image.load('damage/hit8.png')
dead1 = pygame.transform.scale(dead1, (80*2,80*2))

dead11 = pygame.image.load('damage/hit16.png')
dead11 = pygame.transform.scale(dead11, (50*3,70*3))

#stance

stance = stand
stance2 = standleft

gameover = False

velocidade = pygame.time.Clock()

tecla_acionada1 = False
tecla_acionada2 = False

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        tela.blit(self.image, (self.rect.x, self.rect.y))    
        return action
    
        

menuImage = pygame.transform.scale(pygame.image.load('menubtn.png'), (160*2, 60*2))
playImage = pygame.transform.scale(pygame.image.load('playbtn.png'), (120*2, 40*2))
quitImage = pygame.transform.scale(pygame.image.load('quitbtn.png'), (120*2, 40*2))

menuButton = Button(400,80, menuImage)
playButton = Button(400,200, playImage)
quitButton = Button(400,300, quitImage)


def run():
    global stance, ind_stand, tecla_acionada1
    if control[pygame.K_RIGHT] and not tecla_acionada1:
        tecla_acionada1 = True
        stance = runright  
        ind_stand = 0      
    
    if tecla_acionada1 and ind_stand == len(runright) - 1:
        tecla_acionada1 = False  
        stance = stand 

def run2():
    global stance, ind_stand, tecla_acionada1
    if control[pygame.K_LEFT] and not tecla_acionada1:
        tecla_acionada1 = True
        stance = runleft  
        ind_stand = 0  
        
    if tecla_acionada1 and ind_stand == len(runleft) - 1:
        tecla_acionada1 = False
        stance = stand

def ducking():
    global stance, ind_stand, tecla_acionada1
    if control[pygame.K_DOWN] and not tecla_acionada1:
        tecla_acionada1 = True
        stance = duck  
        ind_stand = 0  
        
    if tecla_acionada1 and ind_duck == len(duck) -1:
        tecla_acionada1 = False  
        stance = stand

start = True
while start:
     
    velocidade.tick(12)
    tela.blit(back, (0,0))
    msg1 = f'Hits: {points1}'
    msg2 = f'Hits: {points2}'
    msgFormat1 = font.render(msg1, True , (0,0,0))
    msgFormat2 = font.render(msg2, True , (0,0,0))
    if gameover == True:
        tela.blit(back2, (0,0))  
        if control[K_F1]:
            gameover = False
            x_sprite = 70
            x_sprite2 = 620
            hpBar1 = 0
            hpBar2 = 0
            points1 = 0
            points2 = 0
            naruto = pygame.Rect(tela.blit(stance[ind_stand], (x_sprite, y_sprite)))
            jiraya = pygame.Rect(tela.blit(stance2[ind_standleft], (x_sprite2, y_sprite2)))
    if pause == True:
        menuButton.draw()
        if playButton.draw():
            pause = False
        if quitButton.draw():
            exit()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    focus = pygame.key.get_focused()              
    control = pygame.key.get_pressed()

    if event.type == KEYDOWN and event.key == K_ESCAPE:
        if pause:
            pause = False
        else:
            pause = True

#UP NARUTO

    if not no_ar and control[pygame.K_UP]:
        velocidade_y = pulo
        no_ar = True

    y_sprite += velocidade_y
    velocidade_y += gravidade

    if y_sprite >= 180:
        y_sprite = 180
        no_ar = False
        velocidade_y = 0

    if control[pygame.K_UP] and not tecla_acionada1:
        tecla_acionada1 = True
        stance = jump  
        ind_stand = 0  
        
    if tecla_acionada1 and ind_jump == len(jump) -1:
        tecla_acionada1 = False  
        stance = stand    

#UP JIRAYA

    if not no_ar2 and control[pygame.K_w]:
        velocidade_y2 = pulo
        no_ar2 = True

    y_sprite2 += velocidade_y2
    velocidade_y2 += gravidade

    if y_sprite2 >= 160:
        y_sprite2 = 160
        no_ar2 = False
        velocidade_y2 = 0

    if control[pygame.K_w] and not tecla_acionada2:
        tecla_acionada2 = True
        stance2 = jump0
        ind_standleft = 0  
        
    if tecla_acionada2 and ind_jump0 == len(jump0) -1:
        tecla_acionada2 = False  
        stance2 = standleft                                                              

#MOVEMENT ON SCREEN
            
    if control[pygame.K_RIGHT]:
        run()
        x_sprite += 10
        
    if control[pygame.K_LEFT]:
        run2()
        x_sprite -= 10

    if control[pygame.K_DOWN]:
        ducking()    

    if control[K_d]:
        x_sprite2 += 10
        
    if control[K_a]:
        x_sprite2 -= 10


#RIGHT
        
    #if control[pygame.K_RIGHT] and not tecla_acionada1:
    #    tecla_acionada1 = True
    #    stance = runright  
    #    ind_stand = 0 

    #if tecla_acionada1 and ind_stand == len(runright) - 1:
    #    tecla_acionada1 = False  
    #    stance = stand   
        


    if control[pygame.K_d] and not tecla_acionada2:
        tecla_acionada2 = True
        stance2 = runright0  
        ind_standleft = 0 

    if tecla_acionada2 and ind_standleft == len(runright0) - 1:
        tecla_acionada2 = False  
        stance2 = standleft

#LEFT

    #if control[pygame.K_LEFT] and not tecla_acionada1:
    #    tecla_acionada1 = True
    #    stance = runleft  
    #    ind_stand = 0  
        
    #if tecla_acionada1 and ind_stand == len(runleft) - 1:
    #    tecla_acionada1 = False
    #    stance = stand

    if control[pygame.K_a] and not tecla_acionada2:
        tecla_acionada2 = True
        stance2 = runleft0  
        ind_standleft = 0 

    if tecla_acionada2 and ind_standleft == len(runleft0) - 1:
        tecla_acionada2 = False  
        stance2 = standleft

#DOWN

    #if control[pygame.K_DOWN] and not tecla_acionada1:
    #    tecla_acionada1 = True
    #    stance = duck  
    #    ind_stand = 0  
        
    #if tecla_acionada1 and ind_duck == len(duck) -1:
    #    tecla_acionada1 = False  
    #    stance = stand

    if control[pygame.K_s] and not tecla_acionada2:
        tecla_acionada2 = True
        stance2 = duck0  
        ind_standleft = 0  
        
    if tecla_acionada2 and ind_duck0 == len(duck0) -1:
        tecla_acionada2 = False  
        stance2 = standleft

#KICK

    if control[pygame.K_z] and not tecla_acionada1:
        tecla_acionada1 = True
        stance = kick  
        ind_stand = 0  
        
    if tecla_acionada1 and ind_kick == len(kick) -1:
        tecla_acionada1 = False  
        stance = stand    

#PUNCH        

    if control[pygame.K_x] and not tecla_acionada1:
        tecla_acionada1 = True
        stance = punch  
        ind_stand = 0  
        
    if tecla_acionada1 and ind_punch == len(punch) -1:
        tecla_acionada1 = False  
        stance = stand   

#FROG
    if control[pygame.K_SPACE] and not tecla_acionada2:
        tecla_acionada2 = True
        stance2 = frog
        ind_standleft = 0  
        
    if tecla_acionada2 and ind_frog == len(frog) -1:
        tecla_acionada2 = False  
        stance2 = standleft

#INDEX  
    ind_frog = (ind_frog + 1) % len(stance2)
    ind_hit = (ind_hit + 1) % len(stance)    
    ind_hit0 = (ind_hit0 + 1) % len(stance2)
    ind_kick = (ind_kick + 1) % len(stance)      
    ind_punch = (ind_punch + 1) % len(stance)  
    ind_duck = (ind_duck + 1) % len(stance) 
    ind_jump = (ind_jump + 1) % len(stance)
    ind_jump0 = (ind_jump0 + 1) % len(stance2)
    ind_standleft = (ind_standleft + 1) % len(stance2) 
    ind_stand = (ind_stand + 1) % len(stance)   
    
#BLIT
    if not gameover and not pause:
        hpbarrect1 = pygame.draw.rect(tela, (255,0,0), (20,20,200 - hpBar1,10))
        hpbarrect2 = pygame.draw.rect(tela, (255,0,0), (580,20,200 - hpBar2,10))
        tela.blit(msgFormat1, (20, 40))
        tela.blit(msgFormat2, (700, 40))
        naruto = pygame.Rect(tela.blit(stance[ind_stand], (x_sprite, y_sprite)))
        jiraya = pygame.Rect(tela.blit(stance2[ind_standleft], (x_sprite2, y_sprite2)))

    if naruto.colliderect(jiraya) and control[pygame.K_RIGHT]:
        x_sprite2 += 40
        stance2 = hit0
        velocidade.tick(5)
        points2 = points2 + 1
        hpBar2 = hpBar2 + 20
        if hpBar2 == 200:
            gameover = True                     
    if ind_hit0 == len(hit0) - 1:
        ind_hit0 = 0
        stance2 = standleft

    if jiraya.colliderect(naruto) and control[pygame.K_a]:
        x_sprite -= 40
        stance = hit
        velocidade.tick(5)
        points1 = points1 + 1
        hpBar1 = hpBar1 + 20
        if hpBar1 == 200:
            gameover = True            
    if ind_hit == len(hit) - 1:
        ind_hit = 0
        stance = stand
    pygame.display.update()
    