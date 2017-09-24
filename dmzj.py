# -*- coding:utf-8 -*-
import re
import urllib2
from cookielib import CookieJar
import os
import execjs
class dmzj(object):
    def __init__(self,name='kuangduzhiyuan'):
        dmzj.name=name
    #解析出每话title与地址,title使用unicode
    def get_chap(self,comicid=dmzj.name):
        idurl='http://manhua.dmzj.com/'+comicid
        html = urllib2.urlopen(idurl)
        html=html.read()
        #保存每一话的地址
        classname=re.findall(r'<!--photo_part-->([\S\s]*?)<!--', html)[0]
        #保存每一话的名字
        chapurl=re.findall(r'href\=\"(.*?)\"',classname)
        chapname=re.findall(r'<a title=\"(.*?)\"',classname)
        chap=[]
        for i in range(0,min(len(chapurl),len(chapname))):
            chap.append({'title':chapname[i].decode('utf8'),'href':chapurl[i]})
        return chap
    #传入每一话的地址与名字进行下载,这是漫画之家的处理逻辑
    def get_img(self,chap):
        try:
            os.makedirs('d:/python/'+self.name+'/'+chap['title'])        
            html=urllib2.urlopen('http://manhua.dmzj.com'+chap['href'])
            codes=re.findall(r'eval\((.*?)\)\n',html.read())[0]
            list=re.findall(r'\"(.*?)\"',execjs.eval(codes).replace('\\',''))
            cookie = CookieJar()
            handler=urllib2.HTTPCookieProcessor(cookie)
            opener = urllib2.build_opener(handler)
            response = opener.open('http://manhua.dmzj.com/kuangduzhiyuan/29159.shtml')
            url='http://images.dmzj.com/'
            postdata={
            'Accept':'image/webp,image/*,*/*;q=0.8',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Connection':'keep-alive',
            'Host':'images.dmzj.com',
            'Referer':'http://manhua.dmzj.com/kuangduzhiyuan/29159.shtml',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
              
            for i in range(0,len(list)):
                req=urllib2.Request(url+str(list[i]),None,postdata)		
                picture=opener.open(req)
                f=file('D:/python/'+self.name+'/'+chap['title']+'/'+str(i).zfill(3)+'.jpg','wb')
                f.write(picture.read())
                f.close()
                picture.close()
            print chap['title']+' has downded!'
            opener.close()
        #自动检测是否已下载,用文件夹来标识
        except:
            print chap['title']+'has existed!'         
#h=dmzj()
#y=h.get_chap()

