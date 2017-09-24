# -*- coding:utf-8 -*-
import os
import time
import multiprocessing
import Queue
import qssdm
#将down_class绑定不同的网站
down_class=qssdm.qssdm()
# 使用Queue来线程通信，因为队列是线程安全的（就是默认这个队列已经有锁）
q = Queue.Queue()
#队列中装的是title,herf
for chap in down_class.get_chap():
	q.put(chap)
def chap_func(q):
	while True:
		try:
			# 不阻塞的读取队列数据
			chap = q.get_nowait()
			i = q.qsize()
		except Exception, e:
			print e
			break
		#不同的网站具有不同的解析方式
		qssdm.qssdm().get_img(chap)
#线程控制器
pool = multiprocessing.Pool()
for i in range(8):
	pool.apply_async(chap_func, args=(q,))
	pool.close()
	pool.join()
