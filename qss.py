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
url='http://www.733dm.net/mh/12071/'
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
print index()
h=open('qss2.html','w')
h.write(index())
h.close()