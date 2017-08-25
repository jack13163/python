#!/usr/bin/python
#coding: utf-8
#处理百度地图产生的json数据
#引入命名空间
import json

#获取文件对象
jsonfile = open('search.json')

#读取文件的内容,返回文件中的所有内容所组成的字符串
#jsonfile.readlines()会返回文件中所有的行构成的列表
jsoncontent = jsonfile.read()

#将json字符串转换为字典对象
result = json.loads(jsoncontent)

#打印json字符串
print jsoncontent

#打印字典对象
for i in result.items():
    print i