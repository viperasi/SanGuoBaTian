#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      Administrator
#
# Created:     09-03-2011
# Copyright:   (c) Administrator 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import SqliteManager

class TablesDAO:

    dbPath = ''
    sm = None

    def __init__(self,dp):
        self.dbPath = dp
        self.sm = SqliteManager.SqliteManager(self.dbPath)

    def selTables(self):
        return self.sm.sel(tableName='sqlite_master',clumns=['name','tbl_name'],where='where name like "tbl_%"')
