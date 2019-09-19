import pymysql

conn = pymysql.connect(host='localhost',user='root',password='qwer1234',db='test')

c=conn.cursor()
symbol=input('심볼을 입력하세요 : ')

"""
sql="SELECT * FROM stocks WHERE symbol='%s'"%symbol
c.execute(sql)
"""

sql="SELECT * FROM stocks WHERE symbol=%s"
c.execute(sql,[symbol])  #리스트타입
#c.execute(sql,(symbol,))  #튜플타입

print(c.fetchall())
print()

c.close()
