#-*- coding: utf8 -*-
import urllib
import urllib2
import sys
import json
import MySQLdb
reload(sys)
sys.setdefaultencoding('utf-8')

# Test Item：当地购API测试
# Creater：Kim
# Date：2016-8-16

userId = 514
token = 'DYfff3f213280a47d884ce983d8ed67a87'

def con_SQL():
    connection = MySQLdb.connect(
        host='hellodfsro.mysql.rds.aliyuncs.com',  # 主机地址
        port=3306,  # 端口号
        user='hellodfsro',  # 用户名
        passwd='91nuanyou',  # 密码
        db='hellodfs20',  # 数据库名
    )

    query1 = "select brandid from sfg_brand_rank"
    query2 = "select id from sfg_goods"
    query4 = "select id from sfg_virtual_cat"
    query6 = "select id from sfg_product"
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor4 = connection.cursor()
    cursor6 = connection.cursor()
    count1 = cursor1.execute(query1)
    count2 = cursor2.execute(query2)
    count4 = cursor4.execute(query4)
    count6 = cursor6.execute(query6)
    brandid = []
    id = []
    goodsid = []
    for i in range(0, count1):
        ListOfTuple = cursor1.fetchmany()[0]
        brandid.append(ListOfTuple[0])

    for j in range(0, count2):
        ListOfTuple = cursor2.fetchmany()[0]
        id.append(ListOfTuple[0])

    for k in range(0, count4):
        ListOfTuple = cursor4.fetchmany()[0]
        id.append(ListOfTuple[0])

    for ii in range(0, count6):
        ListOfTuple = cursor6.fetchmany()[0]
        goodsid.append(ListOfTuple[0])

    cursor1.close()
    cursor2.close()
    cursor4.close()
    cursor6.close()
    connection.commit()