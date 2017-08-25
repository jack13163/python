#!/usr/bin/python
#coding:utf-8
#控制流
#输入
num = int(raw_input('请输入一个数字：'))
if num == 3:
    print '恭喜，你猜对了'

str1 = 'fsdagsad'
i = 0
#while语句
while i < len(str1):
    i+=1
    print 'while循环',i
#for语句,rang(函数产生整数)
for i in range(1,5):
    print 'for循环',i

