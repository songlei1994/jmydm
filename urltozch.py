# -*- coding:utf-8 -*-
import urllib
rawurl = '妈妈'.decode('utf8').encode('gbk')
url = urllib.quote('www.733dm.net/e/search/?searchget=1&show=title&keyboard='+rawurl)
print url
html=urllib.urlopen(url).read()
print html