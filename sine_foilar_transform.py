from math import *
import matplotlib.pyplot as plt
def sine(x,n):
	sumer=0
	for i in range(n):
		sumer+=((-1)**i)*((x**(2*i+1))/factorial((2*i+1)))
	return sumer
# ///////////////////////
x=[i/10000 for i in range(-31415*2,31415*2)]
y=[sin(i) for i in x]
plt.plot(x,y)

for j in range(5):
	y1=[y[i]-sine(x[i],j) for i in range(len(x))]
	plt.plot(x,y1)


plt.show()