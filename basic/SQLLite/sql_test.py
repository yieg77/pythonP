import sqlite3

#print(sqlite3.version)
#print(sqlite3.sqlite_version)

conn = sqlite3.connect('D:/ai/pythonP/basic/SQLLite/example.db')
c = conn.cursor()

#Create Table
'''
c.execute("""CREATE TABLE if not exists stocks
(date text, trans text, symbol text, qty real, price real)""")
'''

#Insert a row of data
'''
c.execute("""
INSERT INTO stocks (date, trans, symbol, qty, price) 
VALUES ('2006-02-05','BUY','RHAT',50,35.89)
""")
'''

#Save the changes
#conn.commit()

t=('RHAT',)
sql = 'SELECT * FROM stocks WHERE symbol=?'
c.execute(sql,t)

#print(c.fetchone())
print(c.fetchall())

for i in range(c.rowcount):
    print(c.fetchone(), '\n')

conn.close()
