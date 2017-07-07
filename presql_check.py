#!/usr/bin/python
import psycopg2
import datetime

class dbFuntion:
    '''
    def createTable():
        conn = psycopg2.connect(database = "postgres", user = "postgres", password = "123456", host = "192.168.10.101", port = "5432")
        cur = conn.cursor()
        cur.execute(CREATE TABLE GIT_Automate(USERNAME TEXT PRIMARY KEY,branchName TEXT,typeOfBinary TEXT,timeOfBuild CHAR(50),status TEXT);)
        conn.commit()
        conn.close()
    '''
    def currentDateTime(self):
        now = datetime.datetime.now()
        return  str(now.date()) +' ' + str(now.hour) +':'+ str(now.minute)
    def addValues(self, Username,branchName,typeOfBinary,timeOfBuild,status):
        conn = psycopg2.connect(database = "postgres", user = "postgres", password = "123456", host = "192.168.10.101", port = "5432")
        cur = conn.cursor()
        cur.execute("""INSERT INTO GIT_Automate VALUES (%s,%s,%s,%s,%s )""",(Username,branchName,typeOfBinary,timeOfBuild,status));
        conn.commit()
        print "Records created successfully"
        conn.close()


    def deleteRows(self, userName):
        conn = psycopg2.connect(database = "postgres", user = "postgres", password = "123456", host = "192.168.10.101", port = "5432")
        print "Opened database successfully"

        cur = conn.cursor()

        cur.execute("DELETE from COMPANY where ID=%d;",userName)

        print "Total number of rows deleted :", cur.rowcount

        cur.execute("SELECT id, name, address, salary  from COMPANY")
        rows = cur.fetchall()
        for row in rows:
           print "ID = ", row[0]
           print "NAME = ", row[1]
           print "ADDRESS = ", row[2]
           print "SALARY = ", row[3], "\n"

        print "Operation done successfully";
        conn.commit
        conn.close


    def readRows(self):
        conn = psycopg2.connect(database = "postgres", user = "postgres", password = "123456", host = "192.168.10.101", port = "5432")
        print "Opened database successfully"

        cur = conn.cursor()

        cur.execute("SELECT USERNAME,branchName,typeOfBinary,timeOfBuild,status from GIT_Automate")
        rows = cur.fetchall()
        '''
        for row in rows:
           print "Username= ", row[0]
           print "Branch_NAME = ", row[1]
           print "type Of Binary= ", row[2]
           print "time Of Build = ", row[3],
           print "status=",row[4],"\n"
        '''
        print "Operation done successfully";
        return rows
        conn.close()

'''
if __name__ == '__main__':
    dbF = dbFuntion()
    print 'calling addValue'

    #dbF.addValues('abiprakaf','KT_REMIX','PRODCAK_UP','12-01-1985','Not-started')
    print 'read records'
    data = dbF.readRows()

    for d in data:
        print d

    print 'Time : ' + dbF.currentDateTime()

'''
