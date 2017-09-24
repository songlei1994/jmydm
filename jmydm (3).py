import PyV8
import urllib2
import re
url='http://www.jmydm.com/comicdir/301010/'
mhpath=urllib2.urlopen(url).read()
spath=re.findall(r'<script>(.*?)</script>',mhpath)[0]
sFiles=re.findall(r'"(.*?)"',spath)[0]
sk="kxnelimwzsb"
ctxt = PyV8.JSContext()       
ctxt.enter()
code=open(r"unsuan.js").read()
func = ctxt.eval("("+code+")")
print func(sFiles,sk).split("|")