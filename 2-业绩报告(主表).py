import tushare as ts
import time

# 2、 业绩报告（主表）数据下载
'''
code,代码
name,名称
esp,每股收益
eps_yoy,每股收益同比(%)
bvps,每股净资产
roe,净资产收益率(%)
epcf,每股现金流量(元)
net_profits,净利润(万元)
profits_yoy,净利润同比(%)
distrib,分配方案
report_date,发布日期
'''
df = ts.get_report_data(2017, 4)
df.rename(columns={'name': '名称', 'eps_yoy': '每股收益同比(%)', 'bvps': '每股净资产', 'roe': '净资产收益率(%)',
                   'epcf': '每股现金流量(元)', 'net_profits': '净利润(万元)', 'profits_yoy': '净利润同比(%)', 'distrib': '分配方案',
                   'report_date': '发布日期'}, inplace=True)
# 生成形如：2-201805-业绩报告(主表).xlsx 的表格
df.sort_values(by=['code']).to_excel('./数据-下载/2-' + time.strftime("%Y%m", time.localtime()) + '-业绩报告(主表).xlsx')
