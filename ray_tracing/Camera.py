import numpy as np,math as M
def dis2(p1,p2):return M.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2)+((p1[2]-p2[2])**2))

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
        for y in range(self.resolution[1]):
            for x in range(self.resolution[0]):
                for obj in screen.objects:
                    colition_point = obj.Colision(self.pos,self.ray_vectors[x][y])
                    if colition_point.any():
                        if obj.is_light_source:
                            self.front_buffer[x][y][0]=obj.col[0]
                            self.front_buffer[x][y][1]=obj.col[1]
                            self.front_buffer[x][y][2]=obj.col[2]
                            break
                        nv=obj.normal(colition_point)
                        dots=[]
                        for light in screen.objects:
                            if light.is_light_source == True:
                                light_ray = (light.pos-obj.pos)/dis2(light.pos,obj.pos)
                            
                                # dot = np.dot(nv,lv)            # ^^^^^^
                                # dot = (np.dot(nv,lv)/2)+0.5    # /\/\/\/\
                                dot = max(np.dot(nv,light_ray),0)       # ^_^_^_
                            
                                dots.append(dot)
                        dot = min(dots)
                        col = abs(dot * obj.col)
                        print(col)
                        self.front_buffer[x][y][0]=col[0]
                        self.front_buffer[x][y][1]=col[1] 
                        self.front_buffer[x][y][2]=col[2]
                    else:pass
                        # self.front_buffer[x][y][0]=10
                        # self.front_buffer[x][y][1]=50
                        # self.front_buffer[x][y][2]=90
        
