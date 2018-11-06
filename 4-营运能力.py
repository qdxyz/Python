import tushare as ts
import time

# 4、 营运能力数据下载
'''
code,代码
name,名称
arturnover,应收账款周转率(次)
arturndays,应收账款周转天数(天)
inventory_turnover,存货周转率(次)
inventory_days,存货周转天数(天)
currentasset_turnover,流动资产周转率(次)
currentasset_days,流动资产周转天数(天)
'''
df = ts.get_operation_data(2017, 4)
df.rename(
    columns={'name': '名称', 'arturnover': '应收账款周转率(次)', 'arturndays': '应收账款周转天数(天)', 'inventory_turnover': '存货周转率(次)',
             'inventory_days': '存货周转天数(天)', 'currentasset_turnover': '流动资产周转率(次)', 'currentasset_days': '流动资产周转天数(天)'},
    inplace=True)
# 生成形如：4-201805-营运能力.xlsx 的表格
df.sort_values(by=['code']).to_excel('./数据-下载/4-' + time.strftime("%Y%m", time.localtime()) + '-营运能力.xlsx')