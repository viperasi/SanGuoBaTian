#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      Administrator
#
# Created:     08-03-2011
# Copyright:   (c) Administrator 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

class City:
    properties = {'id':0,'name':'','codeName':'','x':0,'y':0,'ownner':0,'legion':0,'currOwnner':0,'currLegion':0,'isSpecial':0,'released':1}

    def __init__(self,prop={'id':0,'name':'','codeName':'','x':0,'y':0,'ownner':0,'legion':0,'currOwnner':0,'currLegion':0,'isSpecial':0,'released':1}):
        self.properties = prop

    def getProperty(self,key):
        return self.properties[key]

    def setProperty(self,key,value):
        self.properties[key] = value

