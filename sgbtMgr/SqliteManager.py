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

    def update(self,sql):
        conn = sqlite3.connect(self.filePath)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()

    def query(self,sql):
        conn = sqlite3.connect(self.filePath)
        cur = conn.cursor()
        cur.execute(sql)
        s = cur.fetchall()
        return s


#module test

def main():
    conn = sqlite3.connect('D:\\nb65_workspace\\SanGuoBaTian\\db\\sgbt.db')
    cur = conn.cursor()
    cur.execute('PRAGMA  table_info(tbl_cities)')
    s = cur.fetchall()
    print s


if __name__ == '__main__':
    main()

