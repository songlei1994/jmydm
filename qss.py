from jinja2 import Template
import os
import sys
reload(sys)
#ʹ��utf8����
sys.setdefaultencoding('utf-8')
# ����MySQL����:
import pymysql
import json
import urllib2
import re
url='http://www.733dm.net/mh/12071/'
html=urllib2.urlopen(url).read()
#print html
data=re.findall(r'<div id="mhContent">([\s\S]*)<div class="tagWarp">',html.decode('gbk'))[0]
#print data
#Ϊ��jinja2��Ⱦʱ��ֱ��д������
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