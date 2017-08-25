#!/usr/bin/python
#coding: utf-8
#快速打开百度地图
#引入命名空间
import webbrowser

#打开指定的链接

#百度地图Place API： http://api.map.baidu.com/place/v2/search?q=饭店&region=北京&output=json&ak=0jZwqzlbKOOVugscWayjXvEIns2dWi6k
#出现服务被禁用,原因是web API未开放，应用程序类型为浏览器端
#webbrowser.open('http://api.map.baidu.com/place/v2/search?q=饭店&region=北京&output=json&ak=0jZwqzlbKOOVugscWayjXvEIns2dWi6k')
#服务端应用程序
#查询北京区域的所有银行
webbrowser.open('http://api.map.baidu.com/place/v2/search?query=银行&page_size=10&page_num=0&scope=1&region=北京&output=json&ak=w07HLPYnqKDGvSRy35T2lD4QRKz1wXNr');

#web api文档的url：http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-placeapi

