import numpy as np
import pylab as pl

f1 = pl.figure(1)
pl.subplot(221)
pl.subplot(222)
pl.subplot(212)

#当绘图对象中有多个轴的时候，可以通过工具栏中的Configure Subplots按钮，
# 交互式地调节轴之间的间距和轴与边框之间的距离。如果希望在程序中调节的话，
# 可以调用subplots_adjust函数，它有left, right, bottom, top, wspace, hspace
# 等几个关键字参数，这些参数的值都是0到1之间的小数，它们是以绘图区域的宽高为1
# 进行正规化之后的坐标或者长度。
pl.subplots_adjust(left=0.08, right=0.95, wspace=0.25, hspace=0.45)
pl.show()