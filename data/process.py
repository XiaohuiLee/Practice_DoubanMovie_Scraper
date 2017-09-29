#!/usr/bin/env python
# coding:utf8


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import MySQLdb
import MySQLdb.cursors



mydb = MySQLdb.connect(host = 'localhost', user = 'aukuno', passwd = 'sql123',db = 'douban', charset = 'utf8')
mydb.autocommit(True)
cursor = mydb.cursor()

#CREATE
# count = 0
# fr = open('douban_movie_clean.txt','r')
# for line in fr:
#     count += 1
#     print count
#     if count == 1 :
#         continue
#     line = line.strip().split("^")
#
#     cursor.execute('insert into movie(name, url, rate, description, length) values(%s, %s, %s, %s, %s)',
#                    [line[1], line[2], line[4], line[-1], line[-3]])
# fr.close()

#UPDATE
# cursor.execute('update movie set name = %s, length = %s where id = 2',['李晓辉','2048'])

#READ
# cursor.execute('select * from movie where id = 35')
# movies = cursor.fetchall()

#DELETE
# sql = 'delete from movie where id = 1'
# cursor.execute(sql)

cursor.close()