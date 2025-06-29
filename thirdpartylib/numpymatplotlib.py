import numpy as np
from matplotlib import pyplot as plt

x=np.linspace(-5,5,200)

fig0=plt.figure(figsize=(10, 5))
print("type(fig0):", type(fig0))
ax=fig0.add_subplot(221)
print("type(ax):", type(ax))
ax.plot(x,np.sin(x), c='r')
ax.set_title('Sine Function-20245007')

ax=fig0.add_subplot(222)
ax.plot(x,np.cos(x), c='g')
ax.set_title('Cosine Function')

ax=plt.subplot(245)
ax.plot(x,x, c='b')
ax.set_title('x')

ax=plt.subplot(246)
ax.plot(x,x**2,c='purple')
ax.set_title("$x^2$")

ax=plt.subplot(247)
ax.plot(x,-4*x**3+5*x+12, c='orange')
ax.set_title("$-4x^3 + 5x + 12$")

ax=plt.subplot(248)
ax.plot(x,np.cos(6*x)*np.exp(-x), c='black')
ax.set_title("$\cos(6x)e^{-x}$")
fig0.subplots_adjust(0.05,0.05,0.95,0.95,wspace=0.1,hspace=0.25)
print("len of fig0.axes",len(fig0.axes))

print("type of fig0.axes:", type(fig0.axes))
plt.show()