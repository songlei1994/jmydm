# -*- coding:utf-8 -*-
import os
import time
import threading
import Queue
import guoman
#将down_class绑定不同的网站
down_class=guoman.guoman()
# 使用Queue来线程通信，因为队列是线程安全的（就是默认这个队列已经有锁）
q = Queue.Queue()
#队列中装的是title,herf,chap有参数
for chap in down_class.get_chap():
	q.put(chap)
def chap_func(q):
	#使用线程局部变量
	data=threading.local()
	while True:
		try:
			# 不阻塞的读取队列数据
			data.chap = q.get_nowait()
			i = q.qsize()
		except Exception, e:
			print e
			break
		#不同的网站具有不同的解析方式
		threading.local()
		down_class.get_img(data.chap)
#线程控制器
i=10
threading_list=[]
for i in range(0,i):
	threading_list.append(threading.Thread(target=chap_func, args=(q, ), name="child_thread_"+str(i)))
for thread in threading_list:
	thread.start()
	thread.join()
print threading_list