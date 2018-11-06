import tushare as ts
import time

# 6、 偿债能力数据下载
'''
code,代码
name,名称
currentratio,流动比率
quickratio,速动比率
cashratio,现金比率
icratio,利息支付倍数
sheqratio,股东权益比率
adratio,股东权益增长率
'''
df = ts.get_debtpaying_data(2017, 4)
df.rename(columns={'name': '名称', 'currentratio': '流动比率', 'quickratio': '速动比率', 'cashratio': '现金比率', 'icratio': '利息支付倍数',
                   'sheqratio': '股东权益比率', 'adratio': '股东权益增长率'}, inplace=True)
# 生成形如：6-201805-偿债能力.xlsx的表格
df.sort_values(by=['code']).to_excel('./数据-下载/6-' + time.strftime("%Y%m", time.localtime()) + '-偿债能力.xlsx')
