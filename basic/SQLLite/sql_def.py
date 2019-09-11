import sqlite3

#DB연결
def connect_db():
    conn = sqlite3.connect('./basic/SQLLite/myBooks.db')
    return conn

#Table생성
def create_table():
    conn = connect_db()
    c = conn.cursor()

    c.execute("""create table if not exists books(
        title text,
        published_date text,
        publisher text,
        pages integer,
        recommend integer
    )""")
    conn.commit()
    conn.close()

#Record추가
def insert_books():
    conn = connect_db()
    c = conn.cursor()

    c.execute("delete from books")

    c.execute("insert into books values ('Java','2019-05-20','길벗',500,10)")

    sql="insert into books values(?,?,?,?,?)"
    c.execute(sql,('Python','2010-10-01','한빛',584,20))

    bookList=[
        ('빅데이터','2014-07-02','삼성',296,11),
        ('안드로이드','2010-02-02','삼성',526,20),
        ('spring','2013-12-02','삼성',248,15)   
    ]

    c.executemany(sql,bookList)
    conn.commit()
    conn.close()

#모든 책 보여주기
def all_books():
    conn = connect_db()
    c=conn.cursor()

    c.execute("select * from books")
    print('[1] 전체 데이터 출력하기')
    books=c.fetchall()
    print(type(books))
    print(len(books))

    for book in books:
        for i in book:
            print(i, end=" ")
        print()
    
    conn.close()

#원하는 갯수만 보여주기
def some_books(number):
    conn=connect_db()
    c=conn.cursor()

    c.execute("select * from books")
    books = c.fetchmany(number)

    for book in books:
        for i in book:
            print(i, end=" ")
        print()
    
    conn.close()

#한권만 보여주기
def one_book():
    conn=connect_db()
    c=conn.cursor()
    c.execute("select * from books")
    book = c.fetchone()
    print(book)
    conn.close()

#페이지수가 많은 책 보여주기
def big_books():
    conn=connect_db()
    c=conn.cursor()
    c.execute("select title, pages from books where pages>300 order by pages desc")
    books=c.fetchall()

    for book in books:
        for i in book:
            print(i, end=" ")
        print()

    conn.close()

#===main===
create_table()
insert_books()

#all_books()
#some_books(3)
#one_book()
big_books()
