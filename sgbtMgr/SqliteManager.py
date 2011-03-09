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

import sqlite3

class SqliteManager:
    filePath = ''

    def __init__(self,fp):
        self.filePath = fp

    def setFilePath(self,fp):
        self.filePath = fp

    def inert(self,tableName,data={}):
        conn = sqlite3.connect(self.filePath)
        cur = conn.cursor()
        cur.execute('insert into ?(?) values(?)',(tableName,','.join(data.keys()),','.join(data.values())))
        conn.commit()
        cur.close()

    def update(self,tableName,data={},where=''):
        conn = sqlite3.connect(self.filePath)
        cur = conn.cursor()
        str = 'update ? set '
        for k,v in data:
            str = str+' '+k+'='+v

        str = str+' ?'
        cur.execute(str,(tableName,where))
        conn.commit()
        cur.close()

    def delete(self,tableName,where):
        conn = sqlite3.connect(self.filePath)
        cur = conn.cursor()
        cur.execute('delete from ? ?',(tableName,where))
        conn.commit()
        cur.close()

    def sel(self,tableName,clumns=[],where='1=1'):
        conn = sqlite3.connect(self.filePath)
        cur = conn.cursor()
        ##cur.execute('select name from sqlite_master where name like \'tbl_%\' and type=\'table\' order by name')
        cur.execute('select ? from ? ?',(','.join(clumns),tableName,where))
        s = cur.fetchall()
        return s


#module test

def main():
    conn = sqlite3.connect('D:\\nb65_workspace\\SanGuoBaTian\\db\\sgbt.db')
    cur = conn.cursor()
    cur.execute('select name from sqlite_master where name like \'tbl_%\' and type=\'table\' order by name')
    s = cur.fetchall()
    print s


if __name__ == '__main__':
    main()

