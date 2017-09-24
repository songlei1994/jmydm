# -*- coding:utf-8 -*-
from Tkinter import *   #引入Tkinter工具包
from guoman import guoman
def hello():  
    print('hello world!')  
def about():  
    h=guoman()
    for row in h.get_chap()[0:10]:
        v = StringVar()  
        btn = Button(win, textvariable=v, command=hello)
        v.set(row['title'])
        print row
        btn.pack()    
win = Tk()  #定义一个窗体  
win.title('Hello World')    #定义窗体标题  
win.geometry('400x200')     #定义窗体的大小，是400X200像素  
#创建下拉菜单  
menubar = Menu(win)  
#创建下拉菜单File，然后将其加入到顶级的菜单栏中  
filemenu = Menu(menubar,tearoff=0)  
filemenu.add_command(label="Open", command=hello)  
filemenu.add_command(label="Save", command=hello)  
filemenu.add_separator()  
filemenu.add_command(label="Exit", command=win.quit)  
menubar.add_cascade(label="File", menu=filemenu)  
  
#创建另一个下拉菜单Edit  
editmenu = Menu(menubar, tearoff=0)  
editmenu.add_command(label="Cut", command=hello)  
editmenu.add_command(label="Copy", command=hello)  
editmenu.add_command(label="Paste", command=hello)  
menubar.add_cascade(label="Edit",menu=editmenu)  
#创建下拉菜单Help  
helpmenu = Menu(menubar, tearoff=0)  
helpmenu.add_command(label="About", command=about)  
menubar.add_cascade(label="Help", menu=helpmenu)  
  
#显示菜单  
win.config(menu=menubar)  
  
mainloop() #进入主循环，程序运行  