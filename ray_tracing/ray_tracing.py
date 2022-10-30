import pygame as pg,numpy as np,math as M
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

Game_light=np.array((-20,10,2))

class MainCamera:  
    def __init__(self,screen):
        self.pos=np.array([0,0,-2])
        self.aprature=2
        self.resolution=screen.resolution
        self.front_buffer=np.ones(shape=(self.resolution[0],self.resolution[1],3))
        self.ray_vectors=None
        MainCamera.update_ray(self)
    def update_ray(self):
        apratureSQR=self.aprature**2
        ray_vectors=np.ones((self.resolution[0],self.resolution[1],3))
        for y in range(self.resolution[1]):
            for x in range(self.resolution[0]):
                # dy,dx=y-(self.resolution[1]/2),x-(self.resolution[0]/2) #============= main =============
                
                dy = (y-(self.resolution[1]/2))/(self.resolution[1]/2)
                dx = (x-(self.resolution[0]/2))/(self.resolution[0]/2)
                
                mag=M.sqrt((dy**2)+(dx**2)+apratureSQR)
                ray_vectors[x][y][0]=dx/mag
                ray_vectors[x][y][1]=dy/mag
                ray_vectors[x][y][2]=self.aprature/mag
        self.ray_vectors=ray_vectors
    def cast_rays(self,screen):
        for obj in screen.objects:
            for y in range(self.resolution[1]):
                for x in range(self.resolution[0]):
                    colition_point = obj.Colision(self.pos,self.ray_vectors[x][y])
                    if colition_point.any():
                        nv=obj.normal(colition_point)
                        lv=(Game_light-obj.pos)/dis2(Game_light,obj.pos)
                        # dot = np.dot(nv,lv)            # ^^^^^^
                        # dot = (np.dot(nv,lv)/2)+0.5    # /\/\/\/\
                        dot = max(np.dot(nv,lv),0)       # ^_^_^_
                        col = abs(dot * obj.col)
                        self.front_buffer[x][y][0]=col[0]
                        self.front_buffer[x][y][1]=col[1] 
                        self.front_buffer[x][y][2]=col[2]
                    
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

class Sphere:
    def __init__(self,x,y,z,r):
        self.pos = np.array((x,y,z))
        self.col = np.array((255,255,255))
        self.r = r
    def Colision(self,cam_pos,ray):
        D=dis2(self.pos,cam_pos)
        camToSelfVec = self.pos-cam_pos
        # camToSelfVecRay = camToSelfVec/D
        dot_ = np.dot(camToSelfVec,ray)
        # theta = M.acos(dot_)
        # ray_mag = dot_
        P = M.sqrt((D**2)-(dot_**2))
        if P<=self.r:
            dv = M.sqrt((self.r**2)-(P**2))
            ray_hit_mag = (dot_+dv)
            ray_pos = ray_hit_mag*ray
            return ray_pos
        return np.array((0,0,0))
    def Colision2(self,cam_pos,ray):
        x1,y1,z1 = cam_pos
        x2,y2,z2 = ray
        a,b,c    = self.pos
        
        Cs = x2*x2+y2*y2+z2*z2+x1*x1+y1*y1+z1*z1-2*(x1*x2+y1*y2+z1*z2)
        Cl = 2*(x1*(x2-x1)-a*(x2-x1)+y1*(y2-y1)-b*(y2-y1)+z1*(z2-z1)-c*(z2-z1))
        Cc = x1*x1+y1*y1+z1*z1+a*a+b*b+c*c-2*(a*x1+b*y1+c*z1)-self.r*self.r
        
        disc = Cl**2-4*Cs*Cc
        if disc >= 0:
            t = (M.sqrt(disc)-Cl)/(2*Cs)
            return np.array((ray*t)+cam_pos)
        return np.array((0,0,0))
    def Colision3(self,cam_pos,ray):
        pointFromT = lambda t:(cam_pos-ray)*t+cam_pos
        tFromPoint = lambda c:(c/(ray-cam_pos))+cam_pos
        disOFSurface = lambda p:(dis2(p,self.pos)-self.r)
        p=None
        d = disOFSurface(cam_pos)
        sumer=d
        while 0.1<d<1000:
            p = pointFromT(d)
            d = disOFSurface(p)
            sumer+=d
        if d<=100:
            return np.array(pointFromT(sumer))
        return np.array((0,0,0))
    def normal(self,p):return (self.pos-p)/dis2(self.pos,p)

screen=Screen(100,100) #-----1
mainCamera = MainCamera(screen)#------2

screen.objects.append(Sphere(-4.5,0,19,6))#-----3
screen.objects.append(Sphere(4.5,0,19,6))#-----3

###################

mainCamera.cast_rays(screen)#-------4
screen.set_pixels(mainCamera)#-------5

a=0
while update():
    m=maper(M.sin(a),-1,1,-20,20)
    n=maper(M.sin(a+(3.1415/2)),-1,1,-20,20)
    
    Game_light=np.array((m,n,2))
    screen.objects[0].col[1]=(m+20)*4
    screen.objects[0].col[0]=(n+20)*4
    mainCamera.cast_rays(screen)#-------4
    screen.set_pixels(mainCamera)#-------5
    a+=0.09
    # print(m)
    
    
    