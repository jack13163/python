#!/usr/bin/python
#coding:utf-8
#定义函数
def sayHello():
    print 'hello jack'

#调用函数
sayHello()

#全局变量
def globalfun():
    #声明x为全局变量，该函数对该全局变量的修改将会影响到函数外部
    global x
    x = 80
    print '局部变量', x

x=70
#调用函数
globalfun()
#打印全局变量，查看是否更改
print  '全局变量',x

#注：一个global可以声明多个全局变量：global a,b,c

#函数默认值
def fun1(message, times=1):
    #打印指定的字符指定次数
    print message*times

#调用函数
fun1('hello')
fun1('world ',9)

#文档字符串
def fun2():
    """
    这是一个文档注释
    """
    print '测试文档注释'


#调用文档注释测试方法
fun2()
print fun2.__doc__