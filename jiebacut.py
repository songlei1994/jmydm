# -*- coding:utf-8 -*-
import os
import fileinput
import jieba
for line in fileinput.input("1.txt"):
    seg_list = jieba.cut(line,cut_all=True)  
    print "Full Mode:", "/ ".join(seg_list)	