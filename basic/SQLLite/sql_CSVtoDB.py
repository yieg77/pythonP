import csv, sqlite3

input_file='./basic/SQLLite/input.csv'

conn = sqlite3.connect('./basic/SQLLite/suppliers.db')
c = conn.cursor()

sql = """
create table if not exists suppliers(
    supplier_name varchar(20),
    invoice_number varchar(20),
    par_number varchar (20),
    cost float,
    purchase_date date
)
"""
c.execute(sql)

#for row in c.execute('SELECT * FROM suppliers'): print(row)


#Table 내용 삭제
sql='delete from suppliers'
c.execute(sql)

#for row in c.execute('SELECT * FROM suppliers'): print(row)

conn.commit()

#for row in c.execute('SELECT * FROM suppliers'): print(row)

# csv 파일에서 데이터를 읽어서 테이블에 insert 
# file_reader=csv.reader(open(input_file,'r',encoding='utf-8'),delimiter=',')
file_reader=csv.reader(open(input_file,'r'),delimiter=',',quotechar='"')
print(file_reader)

# 첫 라인을 읽음(제목행)
header=next(file_reader,None)
print('header',header)

# header 이후의 2번째 행부터 끝까지 읽어 들이며 insert
for row in file_reader:
    data=[] 
    # idx에는 0~4가 입력됨
    for idx in range(5):#len(header)): 
        data.append(row[idx])    
    c.execute('insert into suppliers values(?,?,?,?,?)',data)

conn.commit()

output=c.execute('select * from suppliers')
rows=output.fetchall()
print('행의 갯수:',len(rows))
for row in rows: 
    print('필드의 갯수:',len(row)) 
    output=[]
    for column_index in range(len(row)): 
        output.append(str(row[column_index])) 
    print(output)

c.close()
