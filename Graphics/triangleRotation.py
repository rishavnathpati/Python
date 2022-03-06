
import numpy as np
import matplotlib.pyplot as plt
import math
print("Enter 1st points: ")
ax=int(input())
ay=int(input())

print("Enter 2nd points: ")
bx=int(input())
by=int(input())

print("Enter 3rd points: ")
cx=int(input())
cy=int(input())


m=-ax
n=-ay

T=np.array([[1,0,0],[0,1,0],[m,n,1]])

sint=1#math.sin(math.radians(90))
cost=0#math.cos(math.radians(90))
R=np.array([[cost,sint,0],[-sint,cost,0],[0,0,1]])
Tt=np.array([[1,0,0],[0,1,0],[-m,-n,1]])

n1=np.matmul(T,R)
N=np.matmul(n1,Tt)

Arr=np.array([[ax,ay,1],[bx,by,1],[cx,cy,1]])

print(R)
print(T)
print(np.matmul(Arr,N))      