#!/usr/bin/python
#coding: utf-8
#文件备份

#要求：
#1、需要备份的文件和目录由一个列表指定
#2、备份保存在主备份目录中
#3、文件备份成一个zip文件
#4、zip的存档名称是当前的日期和时间
#5、使用标准的zip命令，windows下使用Info-Zip程序，
# 你可以使用任何地存档命令，只要它有命令行界面就可以了
# ，那样的话我们就可以从我们的脚本中传递参数给它

import os
import time
#备份列表
source = ['G:\\regDog\\']
#备份主目录
target_dir = 'G:\\'

#将文件备份成为一个zip文件
#zip文件名
filename = target_dir + time.strftime('%Y%m%d%H%M%S') + '.rar'

#需要配置winrar的环境变量，配置后，重启系统，才能使用
#zip命令
#zip_cmd = "zip -qr %s %s" %(filename, ' '.join(source))
zip_cmd = "WinRAR A %s %s" %(filename, ' '.join(source))
#WinRAR A TOOLS.ZIP @Binaries
#zip_cmd = 'winrar a g:/new.rar g:/regDog/'
#zip_cmd = 'shutdown -t 0'#关机

#运行命令
if os.system(zip_cmd) == 0:
    print '备份成功，备份路径为%s' % target_dir
else:
    print '备份失败'
