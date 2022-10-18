import pyg,random
pg = pyg.Pg(400,400)

a=10
b=28
c=-8/3

class P:
    xclip=20
    yclip=20
    zclip=20
    def __init__(self):
        self.x = random.uniform(-P.xclip,P.xclip)
        self.y = random.uniform(-P.yclip,P.yclip)
        self.z = random.uniform(-P.zclip,P.zclip)
    def move(self):
        self.x+=a*(self.y-self.x)
        self.y+=(self.x*(b-self.z))-self.y
        self.z+=(self.x*self.y)+(c*self.z)
    def draw(self):
        if self.z<-P.zclip:self.z=-P.zclip
        elif self.z>P.zclip:self.z=P.zclip
        # print(pg.clip_col(self.z,-P.zclip,P.zclip))
        # print((self.x,self.y))
        print((((self.x+P.xclip)/(2*P.xclip))*pg.width,((self.y+P.yclip)/(2*P.yclip))*pg.height))
        pg.cir(1,(((self.x+P.xclip)/(2*P.xclip))*pg.width,((self.y+P.yclip)/(2*P.yclip))*pg.height),3)

ps=[P() for _ in range(100)]
while pg.run(trace=False):
    for p in ps:
        p.move()
        p.draw()