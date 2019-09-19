import pymysql

conn = pymysql.connect(host='localhost',user='root',password='qwer1234',db='test',
cursorclass=pymysql.cursors.DictCursor) #딕셔너리 형태로 데이터 출력

c=conn.cursor()

#다량 데이터 한번에 INSERT
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
 ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
 ('2006-04-06', 'SELL', 'IBM', 500, 53.00), ] 

#c.executemany('INSERT INTO stocks VALUES(%s,%s,%s,%s,%s)',purchases)
#conn.commit()

sql="SELECT * FROM stocks ORDER BY price"
c.execute(sql)

rows = c.fetchall()
for row in rows:
    print(row)

c.close()
