#pl.legend((plot1, plot2), (’label1, label2’), loc='best’, numpoints=1)

#第三个参数loc = 表示图例放置的位置:'best’‘upper right’, ‘upper left’, ‘center’, ‘lower left’, ‘lower right’.

#如果在当前figure里plot的时候已经指定了label，如plt.plot(x, z, label="")，直接调用plt.legend()就可以了。

import numpy as np
import matplotlib.pyplot as plt

xData = np.arange(0, 10, 1)
yData1 = xData.__pow__(2.0)
yData2 = np.arange(15, 61, 5)
plt.figure(num=1, figsize=(8, 6))
plt.title('中国电建一二•五联合体测量队', size=14)
plt.xlabel('x-axis', size=14)
plt.ylabel('y-axis', size=14)
plt.plot(xData, yData1, color='b', linestyle='--', marker='o', label='y1 data')
plt.plot(xData, yData2, color='r', linestyle='-', label='y2 data')
plt.legend(loc='upper left')
#plt.show()
plt.savefig('plot1.png', format='png')