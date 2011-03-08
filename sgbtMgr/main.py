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

import Tkinter
import SimpleDialog
import FileDialog

import SqliteManager

root = Tkinter.Tk()

def main():
    init()

def init():
    root.title('三国霸天传数据编辑工具')
    root.geometry('800x600+100+100')
    initMenu()
    root.mainloop()

def initMenu():
    mb = Tkinter.Menu()

    mb.add_cascade(label='数据',menu=createDbMenu(mb))
    mb.add_cascade(label='剧本',menu=createScriptMenu(mb))
    mb.add_cascade(label='人物',menu=createHeroMenu(mb))
    mb.add_cascade(label='物品',menu=createGoodsMenu(mb))
    mb.add_cascade(label='技能',menu=createSkillsMenu(mb))
    mb.add_command(label='关于',command=aboutMenu)

    root['menu'] = mb

def aboutMenu():
    dlg = SimpleDialog.SimpleDialog(root,text='    三国霸天传数据编辑工具\nprogrammer:viperasi\nweb-site:http://www.xu81.com',buttons=['确定'])
    dlg.go()

def closeAbout(tl):
    tl.destroy()

def createDbMenu(rootMenu):
    dbMenu = Tkinter.Menu(rootMenu,tearoff=0)
    dbMenu.add_command(label='打开数据文件(*.db)',command=dbMenuOpenFile)
    dbMenu.add_command(label='退出',command=dbMenuExit)
    return dbMenu

def dbMenuOpenFile():
    fd = FileDialog.LoadFileDialog(root)
    filePath = fd.go()
    if filePath!=None:
        sm = SqliteManager.SqliteManager(filePath)
        sm.getConnect()
    else:
        print 'file path is none'


def dbMenuExit():
    print 'exit'

def createScriptMenu(rootMenu):
    scriptMenu = Tkinter.Menu(rootMenu,tearoff=0)
    scriptMenu.add_command(label='创建剧本',command=scriptMenuCreateScript)
    scriptMenu.add_command(label='查看剧本',command=scriptMenuViewScript)
    return scriptMenu

def scriptMenuCreateScript():
    print 'create script'

def scriptMenuViewScript():
    print 'view script'

def createHeroMenu(rootMenu):
    heroMenu = Tkinter.Menu(rootMenu,tearoff=0)
    heroMenu.add_command(label='创建人物',command=heroMenuCreateHero)
    heroMenu.add_command(label='查看人物',command=heroMenuViewHero)
    return heroMenu

def heroMenuCreateHero():
    print 'create hero'

def heroMenuViewHero():
    print 'view hero'

def createGoodsMenu(rootMenu):
    goodsMenu = Tkinter.Menu(rootMenu,tearoff=0)
    goodsMenu.add_command(label='创建物品',command=goodsMenuCreateGoods)
    goodsMenu.add_command(label='查看物品',command=goodsMenuViewGoods)
    return goodsMenu

def goodsMenuCreateGoods():
    print 'create goods'

def goodsMenuViewGoods():
    print 'view goods'

def createSkillsMenu(rootMenu):
    skillsMenu = Tkinter.Menu(rootMenu,tearoff=0)
    skillsMenu.add_command(label='创建技能',command=skillsMenuCreateSkills)
    skillsMenu.add_command(label='查看技能',command=skillsMenuViewSkills)
    return skillsMenu

def skillsMenuCreateSkills():
    print 'create skills'

def skillsMenuViewSkills():
    print 'view skills'

if __name__ == '__main__':
    main()


