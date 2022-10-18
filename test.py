# import pyg, numpy as np,random
# pg=pyg.Pg(600,600)
# width,height=(20,20)

# class Grid:
#     def __init__(self):
#         self.grid=np.array([[0 for i in range(height)] for j in range(width)])

# class Ant(Grid):
#     def __init__(self):
#         self.pos=random.randint(1,)

# def pi():
#     q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
#     while True:
#         if 4 * q + r - t < n * t:
#             yield n
#             nr = 10 * (r - n * t)
#             n = ((10 * (3 * q + r)) // t) - 10 * n
#             q *= 10
#             r = nr
#         else:
#             nr = (2 * q + r) * l
#             nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
#             q *= k
#             t *= l
#             l += 2
#             k += 1
#             n = nn
#             r = nr

# digits = pi()
# pi_list = []
# for i in range(100):
    # pi_list.append(next(digits))

# print(pi_list)

# import numpy as np
# import matplotlib.pyplot as plt

# class NeuralNetwork:
#     def __init__(self,x,y):
#         self.input = x
#         self.weights1 = np.random.rand(self.input.shape[1],4)
#         self.weights2 = np.random.rand(4,1)
#         self.y = y
#         self.output = np.zeros(self.y.shape)
#         self.cost = []
#     def feedforward(self):
#         self.layer1 = self.sigmoid(np.dot(self.input,self.weights1))
#         self.output = self.sigmoid(np.dot(self.layer1,self.weights2))
#     def backprop(self):
#         #application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
#         d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * self.sigmoid_derivative(self.output)))
#         d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * self.sigmoid_derivative(self.output), self.weights2.T) * self.sigmoid_derivative(self.layer1)))

#         # update the weights with the derivative (slope) of the loss function
#         self.weights1 += d_weights1
#         self.weights2 += d_weights2
#     def sigmoid(self,x):
#         return 1/(1+np.exp(-x))
#     def sigmoid_derivative(self,x):
#         return x*(1-x)
#     def train(self,X,y):
#         self.output = self.feedforward()
#         self.backprop()
#     def cost_function(self):
#         self.cost.append(np.mean(np.square(self.y - self.output)))

# X = np.array([[0,0,1],
#               [0,1,1],
#               [1,0,1],
             
#               [1,1,1]])
# y = np.array([[0],[1],[1],[0]])
# nn = NeuralNetwork(X,y)
# for i in range(1500):
#     nn.feedforward()
#     nn.backprop()
#     nn.cost_function()
# plt.plot(nn.cost)
# plt.show()



