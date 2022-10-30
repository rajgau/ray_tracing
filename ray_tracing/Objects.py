import numpy as np,math as M
def dis2(p1,p2):return M.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2)+((p1[2]-p2[2])**2))

class Sphere:
    def __init__(self,pos,r,is_light=False,col=(255,255,255)):
        self.pos = np.array(pos)
        self.col = np.array(col)
        self.r = r
        self.is_light_source = is_light
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