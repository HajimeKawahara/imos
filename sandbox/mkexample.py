import numpy as np
import matplotlib.pyplot as plt
N = 100
x = np.random.randn(N)
a = 1.0
b = 1.0
yobs = a * np.sin(x) + b*x 

a = 1.3
b = 0.8
yth = a * np.sin(x) + b*x 

#plt.hist(x,bins=100, alpha=0.4)
plt.hist(yobs,bins=100, alpha=0.5)
plt.hist(yth,bins=100, alpha=0.5)
plt.show()

#The Question is how to optimized a and b in yth using yobs and yth
