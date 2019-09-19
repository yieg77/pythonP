import sqlite3

#conn = sqlite3.connect('./SQLLite/example.db')
conn = sqlite3.connect('D:/ai/pythonP/basic/SQLLite/example.db')
c = conn.cursor()

'''
#비추-------------------------------
symbol = input('심볼을 입력하세요(RHAT, SSS...): ')
c.execute("SELECT * FROM stocks WHERE symbol = '%s'" %symbol)
#-----------------------------------
'''

#추천-------------------------------
symbol=input('심볼을 입력하세요(RHAT, SSS...): ')
symbol=(symbol,)
sql = "SELECT * FROM stocks WHERE symbol=?"
c.execute(sql,symbol)
#-----------------------------------

#print(symbol)

#print(c.fetchone())
#print(c.fetchone())
#print(c.fetchmany())

rows=c.fetchall()
print(rows)
for row in rows:
    print(row)

conn.close()
