import tushare as ts
import time

# 7、 现金流量数据下载
'''
code,代码
name,名称
cf_sales,经营现金净流量对销售收入比率
rateofreturn,资产的经营现金流量回报率
cf_nm,经营现金净流量与净利润的比率
cf_liabilities,经营现金净流量对负债比率
cashflowratio,现金流量比率
'''
df = ts.get_cashflow_data(2017, 4)
df.rename(
    columns={'name': '名称', 'cf_sales': '经营现金净流量对销售收入比率', 'rateofreturn': '资产的经营现金流量回报率', 'cf_nm': '经营现金净流量与净利润的比率',
             'cf_liabilities': '经营现金净流量对负债比率', 'cashflowratio': '现金流量比率'}, inplace=True)
#df.sort_values(by=['code'])

# 生成形如：7-201805-现金流量.xlsx的表格
df.sort_values(by=['code']).to_excel('./数据-下载/7-' + time.strftime("%Y%m", time.localtime()) + '-现金流量.xlsx')
