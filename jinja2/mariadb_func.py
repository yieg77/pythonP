import pymysql

#DB연결
def conn_db():
    conn = pymysql.connect(host='localhost',user='root',password='qwer1234',db='test',
    charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor) #딕셔너리 형태로 데이터 출력

    return conn

#Table생성
def create_table():
    conn=conn_db()
    c=conn.cursor()

    sql="""CREATE TABLE if not exists books(
        title text,
        published_date text,
        publisher text,
        pages integer,
        recommend integer)"""

    c.execute(sql)
    conn.commit()
    conn.close()


#데이터 입력하기
def insert_record(new_data):
    conn=conn_db()
    c=conn.cursor()

    create_table()

    sql="INSERT INTO books VALUES (%s,%s,%s,%s,%s)"
    c.execute(sql, new_data)
    conn.commit()
    conn.close()


#데이터 수정하기
def update_book(title, published_date, publisher, pages, recommend):
    conn=conn_db()
    c=conn.cursor()

    sql="""UPDATE books
              SET title=%s,
                  published_date=%s,
                  publisher=%s,
                  pages=%s,
                  recommend=%s
            WHERE title = %s"""
    print(sql)

    c.execute(sql, (title,published_date, publisher, pages, recommend, title))

    print(sql)

    conn.commit()

    conn.close()


#데이터 삭제하기
def delete_book(title):
    conn=conn_db()
    c=conn.cursor()

    sql="DELETE FROM books WHERE title=%s"
    c.execute(sql, (title,))
    conn.commit()

    conn.close()


#전체 데이터 조회
def show_all_books():
    conn=conn_db()
    c=conn.cursor()

    sql="SELECT * FROM books"

    c.execute(sql)

    rows=c.fetchall()
    for row in rows:
        print(row)

    conn.close()


#부분 데이터 조회
def show_some_books():
    num=input('몇권의 책을 조회할까요? : ')

    conn=conn_db()
    c=conn.cursor()

    sql="SELECT * FROM books "
    c.execute(sql)

    rows=c.fetchmany(int(num))
    for row in rows:
        print(row)

    conn.close()

#조건으로 데이터 조회
def show_Book(srchKey):
    conn=conn_db()
    c=conn.cursor()

    sql="SELECT * FROM books WHERE title = %s"
    print(sql)

    c.execute(sql, srchKey)

    book=c.fetchone()
    print(book)

    conn.close()

    return book
