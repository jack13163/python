#!/usr/bin/python
#coding: utf-8
#对象与引用

def showList(list):
    for i in list:
        print i

shoplist = ['apple', 'mango', 'carrot', 'banana']
reflist = shoplist

#删除引用列表中的元素
del reflist[0]

print '原列表'
showList(shoplist)
print '引用列表'
showList(reflist)
#原列表和引用列表的值都发生改变

copylist = shoplist[:]
del copylist[0]
print '原列表'
showList(shoplist)
print '复制列表'
showList(copylist)
