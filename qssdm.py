# -*- coding:utf-8 -*-
import urllib2
import base64
#js代码执行所需库
from execjs import eval 
import re
import os
#viewname = "177.期待你的答案"
class qssdm(object):
    def __init__(self,name='nvhanzi'):
        qssdm.name=name 
    def search(self,keyword='mama'):
        url = urllib2.quote(name.decode('utf8').encode('gbk'))
        #733搜索api接口
        req = urllib2.Request('http://www.733dm.net/e/search/?searchget=1&show=title&keyboard='+url)        
    def get_chap(self,comicid='28221'):
        idurl='http://www.733dm.net/mh/'+comicid
        html = urllib2.urlopen(idurl)
        html=html.read()
        classblock=re.findall(r'<div id="section">([\S\s]*?)<!--', html)[0]
        #<li><a href="/mh/28221/379372.html" title="179.我要去美国了">179.我要去美国了</a></li>
        classgroup=re.findall(r'<li><a href="(.*?)" title="(.*?)">',classblock)
        #print classgroup
        chap=[]
        #保存每一话的地址,名字
        for group in classgroup:
            chap.append({'title':group[1].decode('gbk'),'href':group[0]})
        return chap        
    def get_img(self,chap):
        try:
            os.makedirs('d:/python/'+self.name+'/'+chap['title'])
            html=urllib2.urlopen('http://www.733dm.net/'+chap['href'])
            packed=re.findall(r'packed\=\"(.*?)\"',html.read())[0]
            html.close()
            jpgurl=base64.b64decode(packed)[4:]
            #print url
            list=re.findall(r'\]=\"(.*?)\"',eval(jpgurl))
            urlhead='http://733.taduo.net/' 
            print (chap['title']+':共 '+str(len(urllist)-2)+'话').decode('utf8')
            for i in range(0,len(list)):
                picture=urllib2.urlopen(urlhead+str(list[i]))
                f=file('d:/python/'+self.name+'/'+chap['title']+'/'+str(i).zfill(3)+'.jpg','wb')
                f.write(picture.read())
                f.close()
                picture.close()
            print chap['title']+' has downloaded!'
        except:
            print chap['title']+'has existed!'
