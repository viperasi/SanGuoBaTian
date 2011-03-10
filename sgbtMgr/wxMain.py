#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      Administrator
#
# Created:     10-03-2011
# Copyright:   (c) Administrator 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import wx

def init():
    app = wx.App()
    frame=wx.Frame(None,title="三国霸天传管理工具")
    frame.Show()
    app.MainLoop()

def main():
    init()

if __name__=='__main__':
    main()
