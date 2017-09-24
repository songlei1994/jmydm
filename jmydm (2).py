# -*- coding:utf-8 -*-
import re
import urllib
import urllib2
import sys
import os
url='http://www.jmydm.com/comicdir/'+sys.argv[1]+'/'
mhpath=urllib.urlopen(url).read()
title=re.findall(r'keywords(.*?)meta name',mhpath.decode('utf8'))
print title[0]
sdir=re.findall(r'\d+',title[0])[0]
os.makedirs('d:/jmydm/'+sdir)
spath=re.findall(r'var sPath="(.*?)";',mhpath)[0]
if mhpath.find('xnnbxnnbsi')>0:
	firstname='zz_'
	mhpath=re.findall(r'xnnbxnnbsi(.*?)blmbwlbzkbwx',mhpath)
else :
	mhpath=re.findall(r'xkmbxksbxnxbxkkbxks(.*?)blmbwlbzkbwx', mhpath)
	firstname='jmydm'
def f(x):
	 x=x.replace('blz','0')
	 x=x.replace('bls','1')
	 x=x.replace('bik','2')
	 x=x.replace('bix','3')
	 x=x.replace('bin','4')
	 x=x.replace('bie','5')
	 x=x.replace('bil','6')
	 x=x.replace('bii','7')
	 x=x.replace('bim','8')
	 x=x.replace('biw','9')
	 x=x.replace('bli','-')
	 x=x.replace('bsi','_')
	 return x
req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
 'Accept':'text/html;q=0.9,*/*;q=0.8',
 'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
 'Accept-Encoding':'gzip',
 'Connection':'close',
 'Referer':'http://www.jmydm.com'
 }
dpath=map(f,mhpath)
def download(surl):
	req = urllib2.Request('http://comic.jmydm.com:8080/'+spath+firstname+surl+".jpg",None,req_header)
	resp = urllib2.urlopen(req,None,5)
	html = resp.read()
	f=file('d:/jmydm/'+sdir+'/'+surl+'.jpg','wb')
	f.write(html)
	f.close()
	print surl+'.jpg'+' 下载完成'.decode('utf-8')
map(download,dpath)