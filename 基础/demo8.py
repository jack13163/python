#!/usr/bin/python
#coding: utf-8
#模块
#导入标准模块库
import sys

if(sys.argv.__len__() > 0):
    print '有',sys.argv.__len__(),'参数'
else: 
    print '无参数'
    
print '命令行参数'
for i in sys.argv:
    print i

print '当前路径', sys.path