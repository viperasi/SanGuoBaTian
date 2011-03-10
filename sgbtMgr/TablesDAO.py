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
        return self.sm.query('select name from sqlite_master where type=\'table\' and name like \'tbl_%\'')

    def selTableClumns(self,tableName):
        return self.sm.query('PRAGMA  table_info('+tableName+')')


#module test
def main():
    td = TablesDAO('D:\\nb65_workspace\\SanGuoBaTian\\db\\sgbt.db')
    clumns = td.selTableClumns('tbl_cities')
    print clumns

if __name__=='__main__':
    main()
