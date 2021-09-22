import os
from datetime import datetime

import filetype
import csv
from xlrd import xldate_as_tuple

ali_title = ['交易号', '商家订单号', '交易创建时间',
             '付款时间',
             '最近修改时间',
             '交易来源地',
             '类型',
             '交易对方',
             '商品名称',
             '金额（元）',
             '收/支',
             '交易状态',
             '服务费（元）',
             '成功退款（元）',
             '备注',
             '资金状态']

tables = []
alipay = "./alipay_bill"
for root, dirs, files in os.walk(alipay):
    for file in files:
        print(os.path.join(alipay, file))
        wechat_workbook = csv.reader(open(os.path.join(alipay, file), encoding="gbk"))
        for rown in wechat_workbook:
            try:
                date = datetime.strptime(rown[2].strip(), '%Y-%m-%d %H:%M:%S')
            except:
                continue
            array = []
            # 交易号
            array.append(rown[0])
            # 商家订单号
            array.append(rown[1])
            # 交易创建时间
            array.append(rown[2])
            # 付款时间
            array.append(rown[3])
            # 最近修改时间
            array.append(date)
            # 交易来源地
            array.append(rown[5])
            # 类型
            array.append(rown[6])
            # 交易对方
            array.append(rown[7])
            # 商品名称
            array.append(rown[8])
            # 金额（元）
            array.append(rown[9])
            # 收/支
            array.append(rown[10])
            # 交易状态
            array.append(rown[11])
            # 服务费（元）
            array.append(rown[12])
            # 成功退款（元）
            array.append(rown[13])
            remark = rown[14].strip()
            if float(rown[13]) > 0:
                remark = remark + ",退款:" + rown[13]
            # 备注
            array.append(remark)
            # 资金状态
            array.append(rown[15])
            tables.append(array)

f = open('支付宝账单.csv', 'w', encoding="GB2312", errors='ignore')

csv_writer = csv.writer(f)
csv_writer.writerow(['支付宝交易记录明细查询'])
csv_writer.writerow(['账号:[252088829@qq.com]'])
csv_writer.writerow(['起始日期:[2020-01-01 00:00:00]    终止日期:[2021-01-01 00:00:00]'])
csv_writer.writerow(['---------------------------------交易记录明细列表------------------------------------'])
csv_writer.writerow(ali_title)

# 数据表格偏移
# 添加数据
for i in tables:
    try:
        csv_writer.writerow(i)
    except:
        print(i, end=' ')
# 存储退出
f.close()
