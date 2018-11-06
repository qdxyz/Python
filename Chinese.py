#-*-coding:utf-8-*-
#文件名: Chinese.py
def set_ch(fnt,fntSize):
    from pylab import mpl
    if fnt=='HT':
        mpl.rcParams['font.sans-serif'] = ['SimHei'] # 黑体
    elif fnt=='YH':
        mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 微软雅黑
    elif fnt=='ST':
        mpl.rcParams['font.sans-serif'] = ['STSong']  # 宋体
    elif fnt=='KT':
        mpl.rcParams['font.sans-serif'] = ['KaiTi']  # 楷体
    elif fnt=='FS':
        mpl.rcParams['font.sans-serif'] = ['STFangsong']  # 华文仿宋
    else :
        mpl.rcParams['font.sans-serif'] = ['FangSong']  # 防宋体
    mpl.rcParams['font.size'] = fntSize
    mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

#黑体    SimHei
#微软雅黑    Microsoft    YaHei
#宋体    STSong
#仿宋    FangSong
#楷体    KaiTi
#华文仿宋 STFangsong
