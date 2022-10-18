from re import M
from math import *
from matplotlib.pyplot import sca
import pygame as pg
from random import randint,uniform

width,height = 1200,600
window = pg.display.set_mode((width, height))
C_BWRGBYCM = ((0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),(255,0,255))
line = lambda pos1,pos2,col,fat:pg.draw.line(window,col,pos1,pos2,fat)
poly = lambda pos,col,fill:pg.draw.polygon(window,col,pos,fill)
class Boid:
	def __init__(self):
		self.x=randint(0,width)
		self.y=randint(0,height)
		self.vel_x=uniform(-1,1)
		self.vel_y=uniform(-1,1)
		self.colour=C_BWRGBYCM[randint(1,7)]
	def move(self):
		self.x+=self.vel_x
		self.y+=self.vel_y
	def constrain(self):
		if self.x>width:self.x=0
		elif self.x<0:self.x=width
		if self.y>height:self.y=0
		elif self.y<0:self.x=height
	def draw(self):
		m=((self.vel_x**2)+(self.vel_y**2))**0.5
		vnx=self.vel_x/m
		vny=self.vel_y/m
		scale=8
		off=(2*pi)/2.5
		a=atan2(vnx,vny) 
		#////////////////////////////////////////////////////////////////
		pg.draw.polygon(window,self.colour,[(self.x+(scale*vnx),self.y+(scale*vny)),
		((scale*sin(a+off))+self.x,(scale*cos(a+off))+self.y),
		(self.x,self.y),
		((scale*sin(a-off))+self.x,(scale*cos(a-off))+self.y)],0)
class Boids:
	def __init__(self,n,space_x,space_y):
		self.space_x=space_x
		self.space_y=space_y
		self.dx=width/self.space_x
		self.dy=height/self.space_y
		self.cells=[[[] for j in range(space_y)] for i in range(space_x)]
		for _ in range(n):
			b=Boid()
			X,Y=self.from_pos_to_cell(b)
			self.cells[X][Y].append(b)
	def from_pos_to_cell(self,obj):
		X=Y=0
		for i in range(self.space_x-1):
			X=i
			if self.dx*i<=obj.x<=self.dx*(i+1):break
		for i in range(self.space_y-1):
			Y=i
			if self.dy*i<=obj.y<=self.dy*(i+1):break
		return (X,Y)
	def show_bownd(self):
		for i in range(self.space_x):line((self.dx*i,0),(self.dx*i,height),C_BWRGBYCM[3],1)
		for i in range(self.space_y):line((0,self.dy*i),(width,self.dy*i),C_BWRGBYCM[3],1)
		for i in range(self.space_x):
			for j in range(self.space_y):
				write(str(len(self.cells[i][j])),(self.dx*i,self.dy*j),C_BWRGBYCM[1])
	def alive(self):
		self.show_bownd()
		for x in range(len(self.cells)):
			for y in range(len(self.cells[0])):
				for b in self.cells[x][y]:
					X,Y=self.from_pos_to_cell(b)
					b.draw()
					b.move()
					b.constrain()
					if X!=x or Y!=y:
						self.cells[X][Y].append(b)
						self.cells[x][y].remove(b)
def write(text,pos,col):
	pg.font.init()
	myfont = pg.font.SysFont('Comic Sans MS', 20)
	textsurface = myfont.render(text, False, col)
	window.blit(textsurface,pos)
def update_pg():
	pg.display.update()
	window.fill(C_BWRGBYCM[0])
	for event in pg.event.get():
		if event.type==pg.QUIT:exit()
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_ESCAPE:quit()
	return
boid=Boids(1000,8,4)
while 1:
	update_pg()
	boid.alive()
	# write("hello",(300,300),C_BWRGBYCM[3])
