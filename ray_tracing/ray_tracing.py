import pygame as pg,numpy as np,math as M
from Objects import *
from Camera import *
width,height=400,400
window=pg.display.set_mode((width,height))
pg.display.set_caption("ray_tracing")
def update(trace=True):
    pg.display.update()
    if not trace:window.fill((0,0,0))
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            return False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                return False
    return True

def maper(v,In,Im,On,Om):
    try:val=(((v-In)/(Im-In))*(Om-On))+On
    except:return 0
    if val<On:val=On
    elif val>Om:val=Om
    return val
def dis(x1,y1,z1,x2,y2,y3):return M.sqrt(((x2-x1)**2)+((y2-y1)**2)+((z2-z1)**2))
def dis2(p1,p2):return M.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2)+((p1[2]-p2[2])**2))
                    
class Screen:
    def __init__(self,x,y):
        self.resolution=(x,y)
        self.objects=[]
    def set_pixels(self,mainCamera):
        side_x=width/self.resolution[0]
        side_y=height/self.resolution[1]
        for y in range(self.resolution[1]):
            for x in range(self.resolution[0]):
                try:pg.draw.rect(window,mainCamera.front_buffer[x][y],(x*side_x,y*side_y,side_x,side_y))
                except:print("Invalid_col_as_input ==>",mainCamera.front_buffer[x][y])
        mainCamera.front_buffer = np.ones(shape=(self.resolution[0],self.resolution[1],3))

screen=Screen(100,100) #-----1
mainCamera = MainCamera(screen)#------2

screen.objects.append(Sphere((0,0,19),6))#-----3

screen.objects.append(Sphere((-7,-7,19),1,is_light=True))
screen.objects.append(Sphere((-7,7,19),1,is_light=True))

###################

mainCamera.cast_rays(screen)#-------4
screen.set_pixels(mainCamera)#-------5

a=0
while update():
    # m=maper(M.sin(a),-1,1,-20,20)
    # n=maper(M.sin(a+(3.1415/2)),-1,1,-20,20)
    
    # screen.objects[0].col[1]=(m+20)*4
    # screen.objects[0].col[0]=(n+20)*4
    # mainCamera.cast_rays(screen)#-------4
    # screen.set_pixels(mainCamera)#-------5
    a+=0.09
    # print(m)
    
    
    