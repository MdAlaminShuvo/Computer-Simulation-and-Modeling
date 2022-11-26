import numpy as np
import pygame

X=900
Y=900
N=100
et=900
ct=100
t=N

xb=np.random.randint(0,X,size=N)
yb=np.random.randint(0,Y,size=N)

xf=[]
yf=[]
xf.append(300)
yf.append(100)

vf=500
isCaught=False

for i in range(0,N):
    dist=np.sqrt((xf[i]-xb[i])**2+(yf[i]-yb[i])**2)

    if dist<=ct:
        isCaught=True
        t=i
        break
    elif dist>=et:
        t=i
        break
    sin=(yb[i]-yf[i])/dist
    cos=(xb[i]-xf[i])/dist
    xf.append(xf[i]+vf*cos)
    yf.append(yf[i]+vf*sin)

pygame.init()

pygame.display.set_caption("persuit")

screensize=(800,600)
screen=pygame.display.set_mode(screensize)
font=pygame.font.SysFont("arial",32)

text1=font.render("B_caught",True,(255,255,255),(0,0,0))
text2=font.render("B_escapped",True,(255,255,255),(0,0,0))

textrec1=text1.get_rect()
textrec2=text2.get_rect()

textposition=(X/2,Y/2)
textrec1.center=textposition
textrec2.center=textposition

running = True

while running:
    screen.fill((0,0,0))
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            for i in range(0,t):
                pygame.draw.line(screen,(255,0,0),(xf[i],yf[i]),(xf[i+1],yf[i+1]),4)
                pygame.draw.circle(screen,(255,0,0),(xf[i+1],yf[i+1]),4)

                pygame.draw.line(screen,(0,255,0),(xb[i],yb[i]),(xb[i+1],yb[i+1]),4)
                pygame.draw.circle(screen,(255,0,0),(xb[i+1],yb[i+1]),4)

                pygame.time.delay(500)
                pygame.display.update()


if isCaught:
    screen.blit(text1,textrec1)
    pygame.draw.line(screen,(0,0,255),(xf[t],yf[t]),(xb[t],yb[t]),4)
else:
    screen.blit(text2,textrec2)
pygame.display.update()
pygame.time.delay(2000)
pygame.quit()