# -*- coding=UTF-8 -*-
import os
import time
def process(path,name):
    print 'it start at %s' %path
    t1=time.time()
    loopmulu(path)
    t2=time.time()
    print 'it has done %s' %path
    last=(t2-t1)/60.0
    print 'it cast %.2f m' %last
def findnaem(child,muth):
    try:
        flag=muth.index(child)
        flagt=1
    except:
        flagt=-1
    return flagt
def loopmulu(path):
    try:
        os.chdir(path)
    except:
        return
    mu=os.getcwd()
    try:
        list1 = os.listdir('.')
    except:
        return
    for i in list1:
        path=mu+'\\'+i
        if os.path.isfile(path):
            try:
                filename=os.path.basename(path).decode('gbk').encode('utf-8')
            except:
                filename=os.path.basename(path)
            if flagisall=='1':
                if name==filename:
                    print path
            else:
                if findnaem(name,filename)==1:
                    print path
        elif os.path.isdir(path):
            loopmulu(path)
     
    
name=raw_input("what you want to find :\n")
flagisall=raw_input("are you want to find what you input without like 1: yes\n")
if os.path.exists('C:\\'):
    path='C:\\'
    process(path,name)
if os.path.exists('D:\\'):
    path='D:\\'
    process(path,name)
if os.path.exists('E:\\'):
    path='E:\\'
    process(path,name)
if os.path.exists('F:\\'):
    path='F:\\'
    process(path,name)

    
    
    
