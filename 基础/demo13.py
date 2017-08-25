#!/usr/bin/python
#coding: utf-8
#python数据类型

#列表
def showList(list):
    for i in list:
        print i
        
shoplist = ['apple', 'mango', 'carrot', 'banana']
print '购物清单中共',len(shoplist),'件商品'
print '旧的购物列表'
showList(shoplist)

#追加商品
shoplist.append('rice')
print '购物清单中共',len(shoplist),'件商品'
print '新的购物列表'
showList(shoplist)

#商品排序
shoplist.sort()
print '排序后的购物列表'
showList(shoplist)

#移除商品
od = shoplist[0]
print '我已购买',od
del shoplist[0]
print '还需要购买'
showList(shoplist)

#元组，和字符串一样是不可变的
def showYZ(yz):
    for i in yz:
        if len(i)>1:
            showYZ(i)
        else:
            print i


zoo = ('wolf', 'elephant', 'pengo')
new_zoo = ('monkey','duck',zoo)
#显示旧动物园中的动物
print '旧动物园的动物们'
print zoo
#showYZ(zoo)
#显示新动物园中的动物
print '新动物园的动物们'
#showYZ(new_zoo)
print new_zoo

#元组用于字符串的格式化输出
age = 22
name = 'Jack'
print 'My name is %s, and i am %d' %(name, age)

#数据类型三：字典
exam = {
    'Jack':90,
    'Mary':78,
    'Lock':67
}
print '学生成绩:%s' %exam
print 'Jack成绩:%s' %exam['Jack']
#添加新的字典项
exam['Holly'] = 39
print '添加后的学生成绩:%s' %exam

#删除学生成绩
del exam['Holly']
print '删除后的学生成绩：%s' %exam

#输出所有的字典项
for name, result in exam.items():
    print '姓名：%s  成绩：%d' %(name, result)

if 'Jack' in exam:
    print 'Jack的成绩存在，%d' %exam['Jack']
if exam.has_key('Jack'):
    print 'Jack的成绩存在，%d' %exam['Jack']


#列表、元组和字符串都是序列，他们都可以进行索引操作和切片操作
#逆序访问，索引操作
print shoplist[-1]
#切片操作
#从第二个元素开始，到第三个元素
print shoplist[1:3]
#从第三个元素开始，知道最后
print shoplist[2:]
print shoplist[1:-1]
