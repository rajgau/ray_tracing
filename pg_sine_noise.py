import matplotlib.pyplot as plt
import math
maper = lambda variable,min_inp,max_inp,min_out,max_out:(((variable-min_inp)/(max_inp-min_inp))*(max_out-min_out))+min_out
class Noise:
	def __init__(self):
		from random import uniform as uni
		pi=3.14159265359
		self.octaves=10
		self.c=[uni(-pi,pi) for i in range(self.octaves)]
		self.f=[uni(-0.15*(i+1),0.15*(i+1)) for i in range(self.octaves)]
		self.t=[uni(-pi,pi) for i in range(self.octaves)]
		self.c1=[uni(-pi,pi) for i in range(self.octaves)]
		self.f1=[uni(-0.15*(i+1),0.15*(i+1)) for i in range(self.octaves)]
		self.t1=[uni(-pi,pi) for i in range(self.octaves)]
	def one(self,x):
		sumer=0
		for i in range(self.octaves):
			sumer+=self.c[i]*math.sin(self.f[i]*x+self.t[i])
		return sumer
	def two(self,x,y):
		sumer=0
		for i in range(self.octaves):sumer+=self.c[i]*math.sin(self.f[i]*x+self.t[i])+self.c1[i]*math.cos(self.f1[i]*y+self.t1[i])
		return sumer
p=Noise()
# x=[i for i in range(400)]
# y=[p.one(i) for i in x]
# plt.plot(x,y)
# plt.show()
import pygame as pg
width,height = 600,600
window = pg.display.set_mode((width, height))
C_BWRGBYCM = ((0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),(255,0,255))
def update_pg():
	pg.display.update()
	for event in pg.event.get():
		if event.type==pg.QUIT:exit()
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_ESCAPE:quit()
	return
maxi=5
mini=-5
pixel=pg.PixelArray(window)
for i in range(width):
	for j in range(height):
		col=abs(int((p.two(i,j)+mini)/maxi)*255)
		if col<mini:mini=col
		elif col>maxi:maxi=col
		pixel[i][j]=(col,col,col)
while 1:
	update_pg()