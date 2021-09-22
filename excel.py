import os
from datetime import datetime

import csv

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
wechat_bill = "./wechat_bill"
alipay = "./alipay_bill"
for root,dirs,files in os.walk(wechat_bill):
    for file in files:
        print(os.path.join(wechat_bill, file))
        wechat_workbook = csv.reader(open(os.path.join(wechat_bill, file)))
        for rown in wechat_workbook:
            try:
                date = datetime.strptime(rown[0],'%Y-%m-%d %H:%M:%S')
            except:
                continue
            # 交易类型
            type = rown[1]
            # 交易对方
            target = rown[2]
            # 商品
            goods = rown[3]
            # 收支
            outIn = rown[4]
            # 价格
            price = rown[5]
            # 支付方式
            method = rown[6]
            # 状态
            status = rown[7]
            # 交易编号
            no = rown[8]
            # 商户号
            targetNo = rown[9]
            # 备注
            remark = rown[10]


            array = []
            # 交易号
            array.append(no)
            # 商家订单号
            array.append(targetNo)
            # 交易创建时间
            array.append(date)
            # 付款时间
            array.append(date)
            # 最近修改时间
            array.append(date)
            # 交易来源地
            array.append(target)
            # 类型
            array.append(type)
            # 交易对方
            array.append(target)
            # 商品名称
            array.append(goods)
            # 金额（元）
            array.append(price)
            # 收/支
            array.append(outIn)
            # 交易状态
            array.append(status)
            # 服务费（元）
            array.append(0)
            # 成功退款（元）
            array.append(0)
            # 备注
            array.append(status + remark)
            # 资金状态
            array.append(status)
            tables.append(array)

f = open('微信账单.csv', 'w', encoding="GB2312", errors='ignore')

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
