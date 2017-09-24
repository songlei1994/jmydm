# -*- coding:utf-8 -*-
import re
import urllib2
import sys
import os
import time
import threading
import Queue
import PyV8
import shutil
class jmydm(object):
    def get_chap(self):
        html=urllib2.urlopen('http://www.jmydm.com/manhua-YuanJunWuYu/')
        chap_list=re.findall(r'/comicdir(.*?)\/a\>',html.read())
        #href="/comicdir/262762/">盾之勇者成名录 番外篇02</a>
        chap=[]
        for i in chap_list:
            chapurl=re.findall(r'/(.*?)/',i)[0]
            chapname=re.findall(r'>(.*?)<',i)[0].replace(' ','_')
	    if chapurl[0]=="3":
		chap.append({'title':chapname.decode('utf8'),'href':chapurl})
        return chap
    def get_img(self,chap):
	url='http://www.jmydm.com/comicdir/'+chap['href']+'/'
	mhpath=urllib2.urlopen(url).read()
	#title=re.findall(r'keywords(.*?)meta name',mhpath.decode('utf8'))
	#print title[0]
	#sdir=re.findall(r'\d+',title[0])[0]
	sdir=chap['title']
	print sdir
	try:
	    shutil.rmtree(r'D:/jmydm/'+sdir)
	except:
	    pass
	finally:
	    os.makedirs(r'D:/jmydm/'+sdir)
	spath=re.findall(r'<script>(.*?)</script>',mhpath)[0]
	sFiles=re.findall(r'"(.*?)"',spath)
	spath=sFiles[1]
	sFiles=sFiles[0]
	sk="kxnelimwzsb"
	#这里演示了如何利用v8引擎调用js文件中的函数
	ctxt = PyV8.JSContext()       
	ctxt.enter()
	code=open(r"unsuan.js").read()
	func=ctxt.eval("("+code+")")
	dpath=func(sFiles,sk).split("|")
	#print dpath
	req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
         'Accept':'text/html;q=0.9,*/*;q=0.8',
         'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
         'Accept-Encoding':'gzip',
         'Connection':'close',
         'Referer':'http://www.jmydm.com'
         }
			
	# 使用Queue来线程通信，因为队列是线程安全的（就是默认这个队列已经有锁）
	q = Queue.Queue()
	for url in dpath:
	    q.put(url)
	start = time.time()
	def fetch_img_func(q):
	    while True:
		try:
		    # 不阻塞的读取队列数据
		    url = q.get_nowait()
		    i = q.qsize()
		    print url,i
		except Exception, e:
		    return 0
		#print 'handle %s pic... pic url %s ' % (i, url)
		req = urllib2.Request('http://comic.jmydm.com:8080/'+spath+"/"+url,None,req_header)
		try:
		    resp = urllib2.urlopen(req,None,timeout=30)
		    html = resp.read()
		    resp.close()
		except:
		    pass
		try:
		    f=file(r'D:/jmydm/'+sdir+'/'+url,'wb')
		    f.write(html)
		    f.close()
		    print url+' 下载完成'.decode('utf-8')
		except:
		    pass
		
	t1 = threading.Thread(target=fetch_img_func, args=(q, ), name="child_thread_1")
	t2 = threading.Thread(target=fetch_img_func, args=(q, ), name="child_thread_2")
	t3 = threading.Thread(target=fetch_img_func, args=(q, ), name="child_thread_3")
	t4 = threading.Thread(target=fetch_img_func, args=(q, ), name="child_thread_4")
	t1.start()
	t2.start()
	t3.start()
	t4.start()
	t1.join()
	t2.join()
	t3.join()
	t4.join()        
if __name__ == '__main__':       
	h=jmydm()
	#h.get_img(h.get_chap()[1])
	#chap={'href': '154580', 'title': u'Vol_03'}
	for row in h.get_chap()[0:20]:
		h.get_img(row)