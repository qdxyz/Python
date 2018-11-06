import tushare as ts
import time

# 5、 成长能力数据下载
'''
code,代码
name,名称
mbrg,主营业务收入增长率(%)
nprg,净利润增长率(%)
nav,净资产增长率
targ,总资产增长率
epsg,每股收益增长率
seg,股东权益增长率
'''
df = ts.get_growth_data(2017, 4)
df.rename(columns={'name': '名称', 'mbrg': '主营业务收入增长率(%)', 'nprg': '净利润增长率(%)', 'nav': '净资产增长率', 'targ': '总资产增长率',
                   'epsg': '每股收益增长率', 'seg': '股东权益增长率'}, inplace=True)
# 生成形如：5-201805-成长能力.xlsx 的表格
df.sort_values(by=['code']).to_excel('./数据-下载/5-' + time.strftime("%Y%m", time.localtime()) + '-成长能力.xlsx')
