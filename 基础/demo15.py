#!/usr/bin/python
#coding: utf-8
#字符串其他的操作
name = 'scoty'

if name.startswith('sc'):
    print '名称以sc开头'

if 'c' in name:
    print '名称中包含有字母c'

if name.find('co') != -1:
    print '名称中包含有co'

#使用指定的分隔符号连接列表中的元素
delimiter = '***'
mylist = ['fdag','tew','df']
print delimiter.join(mylist)

