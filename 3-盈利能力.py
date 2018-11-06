import tushare as ts
import time

# 3、 盈利能力数据下载
'''
code,代码
name,名称
roe,净资产收益率(%)
net_profit_ratio,净利率(%)
gross_profit_rate,毛利率(%)
net_profits,净利润(万元)
esp,每股收益
business_income,营业收入(百万元)
bips,每股主营业务收入(元)
'''
df = ts.get_profit_data(2017, 4)
df.rename(columns={'name': '名称', 'net_profit_ratio': '净利率(%)', 'gross_profit_rate': '毛利率(%)', 'roe': '净资产收益率(%)',
                   'esp': '每股收益', 'net_profits': '净利润(万元)', 'business_income': '营业收入(百万元)', 'bips': '每股主营业务收入(元)'}, inplace=True)
# 生成形如：3-201805-盈利能力.xlsx 的表格
df.sort_values(by=['code']).to_excel('./数据-下载/3-' + time.strftime("%Y%m", time.localtime()) + '-盈利能力.xlsx')
