# -*- coding:utf-8 -*-
import urllib2
import traceback
import base64
#js代码执行所需库
import execjs 
import chardet
import re
import os
import time
from cookielib import CookieJar
import sys
reload(sys)
#使用utf8编码
sys.setdefaultencoding('utf-8')
#viewname = "177.期待你的答案"
class guoman(object):
    def __init__(self,name='haha'):
        guoman.name=name    
    def get_chap(self,comicid='2945'):
        idurl='http://www.guoman8.net/manhua/'+comicid+'/'
        cookie = CookieJar()
        handler=urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(handler)
        req=urllib2.Request(idurl)
        picture=opener.open(req)
        time.sleep(10)
        html=opener.open(req)       
        html=html.read()
        opener.close()
        #print html.decode('gbk')
        classblock=re.findall(r'<body>([\S\s]*?)appid', html)[0]
        #<li><a href="/mh/28221/379372.html" title="179.我要去美国了">179.我要去美国了</a></li>
        classgroup=re.findall(r'<li><a href="(.*?)" title="(.*?)" class="status0" target="_blank">',classblock)
        #print classblock
        chap=[]
        #保存每一话的地址,名字
        for group in classgroup:
            chap.append({'title':group[1].decode('utf8'),'href':group[0]})
        return chap[1:]        
    def get_img(self,chap):
        try:
            os.makedirs('d:/python/'+self.name+'/'+chap['title'])
            idurl='http://www.ikanman.com/'+chap['href']
            cookie = CookieJar()
            handler=urllib2.HTTPCookieProcessor(cookie)
            opener = urllib2.build_opener(handler)
            req=urllib2.Request(idurl)		
            picture=opener.open(req)
            time.sleep(2)
            html=opener.open(req)       
            html=html.read()
            #print html
            code=re.findall(r'window\["\\x65\\x76\\x61\\x6c"\](.*?)</script>',html)
            print code
            y=execjs.eval(code[0])
            #urllist=eval(y)['fs']
            urllist=[]
            print (chap['title']+':共 '+str(len(urllist)-2)+'话').decode('utf8')
            urlhead='http://images.720rs.com'
            header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
            for i in range(0,len(urllist)-2):
                req=urllib2.Request(urlhead+urllist[i],None,header)
                picture=urllib2.urlopen(req)
                f=file('d:/python/'+self.name+'/'+chap['title']+'/'+str(i).zfill(3)+'.jpg','wb')
                f.write(picture.read())
                f.close()
                picture.close()
            print chap['title']+' has downloaded!'
        except Exception, e:
            print e
            f=open('eroor.txt','a')
            f.write(str(chap))
            f.close()
            #print chap['title']+'has existed!'
h=guoman()
chap_list={'href': '/comic/24669/312417.html', 'title': u'016.\u5929\u7a7a\u4e0b\u7740\u6c99\uff08\u4e0a\uff09'}
h.get_img(chap_list)
