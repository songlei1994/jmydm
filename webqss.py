# -*- coding:utf-8 -*-
import web
from jinja2 import Template
import os
import sys
reload(sys)
#使用utf8编码
sys.setdefaultencoding('utf-8')
# 导入MySQL驱动:
import pymysql
import json
import urllib2
import re
urls = (
  '/search/(.*)', 'search',
  '/mh/([\d,/]*)','result',
  '/test','index',
  '/mh/(\d*)/(.*)','comic'
)
class result:
    def GET(self,name):
        url='http://www.733dm.net/mh/'+name
        html=urllib2.urlopen(url).read()
        #print html
        data=re.findall(r'<div id="mhContent">([\s\S]*)<div class="tagWarp">',html.decode('gbk'))[0]
        #print data
        #为了jinja2渲染时能直接写入中文
        y=json.dumps(data).decode("unicode-escape")
        #print y
        def index():
            f = open('qss.html')
            result = f.read()
            template = Template(result)
            data = template.render(comic=y)
            template.render()
            return data.decode('utf8')
        return index()
class search:
    def GET(self,name):
        rawurl = name.decode('utf8').encode('gbk')
        url = urllib2.quote(rawurl)
        req_header={
            'searchget':'1',
            'show':'title',
            'keyboard':url}
        #733搜索api接口
        req = urllib2.Request('http://www.733dm.net/e/search/?searchget=1&show=title&keyboard='+url)
        resp = urllib2.urlopen(req,None,timeout=30)
        return resp.read().replace('/skin/dh/dhb.css','http://www.733dm.net/skin/dh/dhb.css').replace('/skin/dh/i.css','http://www.733dm.net/skin/dh/i.css')        
class comic:
    def GET(self,title,chap):
        return title,chap
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()