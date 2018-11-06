import numpy as np
import matplotlib.pyplot as plt

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2 # 0 to 15 point radiuses
color = 2 * np.pi * np.random.rand(N)
plt.scatter(x, y, s=area, c=color, alpha=0.5, cmap=plt.cm.hsv)
plt.show()