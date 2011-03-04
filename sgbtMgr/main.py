#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      Administrator
#
# Created:     03-03-2011
# Copyright:   (c) Administrator 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from Tkinter import *

def main():
    init()

def init():
    root = Tk()
    initMenu(root)
    root.mainloop()

def initMenu(r):
    mb = Menu(r)

    dbMenu = Menu(mb,tearoff=0)
    for item in ['打开数据文件(*.db)','退出']:
        dbMenu.add_command(label=item,command=menuController)

    scriptMenu = Menu(mb,tearoff=0)
    for item in ['创建剧本','查看剧本']:
        scriptMenu.add_command(label=item,command=menuController)

    heroMenu = Menu(mb.tearoff=0)
    for item in ['创建人物','查看人物']:
        heroMenu.add_command(label=item,command=menuController)

    mb.add_cascade(label='数据',menu=dbMenu)
    mb.add_cascade(label='剧本',menu=scriptMenu)
    mb.add_cascade(label='人物',menu=heroMenu)
    r['menu'] = mb

def menuController():
    print 'hello world'

if __name__ == '__main__':
    main()


