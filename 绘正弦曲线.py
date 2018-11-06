import numpy as np
import matplotlib.pyplot as plt
import Chinese as ch


x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x ** 2)

plt.figure(figsize=(8, 4))
plt.plot(x, y, label="sin(x)", color="red", linewidth=2)
plt.plot(x, z, "b--", label="cos(x^2)")
ch.set_ch('ST',12)
plt.xlabel(u"X轴-Time(s)")
plt.ylabel(u"Y轴-Volt")
ch.set_ch('FS',20)
plt.title(u"中国电建一二•五联合体")
plt.ylim(-1.2, 1.2)
plt.legend()
plt.show()