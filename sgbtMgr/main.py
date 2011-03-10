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
import TablesDAO

root = Tkinter.Tk()
dbPath = ''

def main():
    init()

def init():
    root.option_add("*Font", "宋体")
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
        dotIndex = filePath.rfind('.')
        if dotIndex!=-1:
            ext = filePath.rsplit('.',1)
            if ext[1]=='db':
                loadTable(filePath)
            else:
                SimpleDialog.SimpleDialog(root,text='请选择sqlite数据库(*.db)文件,\n选择的文件无效.',buttons=['确定']).go()

def loadTable(dbPath):
    tablesFrame = Tkinter.Frame(width=100)
    tablesList = Tkinter.Listbox(tablesFrame)
    tablesList.insert(Tkinter.END,'表格')
    tdao = TablesDAO.TablesDAO(dbPath)
    tables = tdao.selTables()
    for t in tables:
        tablesList.insert(Tkinter.END,t)
    tablesList.bind('<Double-Button-1>',lambda x:tablesListListener(tablesList.get(tablesList.curselection()),dbPath))
    tablesList.pack()
    tablesFrame.place(x = 0,y = 0,anchor = Tkinter.NW)

def tablesListListener(tableName,dbPath):
    print "dbPath--->"+dbPath
    dataList = Tkinter.Frame()
    tdao = TablesDAO.TablesDAO(dbPath)
    clumns = tdao.selTableClumns(tableName[0])
    cLists = []
    i = 0
    for c in clumns:
        print c
        cList = Tkinter.Listbox(dataList)
        cList.insert(Tkinter.END,c[1])
        cList.pack()
        cLists.append(cList)
        i=i+1

    dataList.place(x = 110,y=0,anchor=Tkinter.CENTER)

def dbMenuExit():
    root.destroy()

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


