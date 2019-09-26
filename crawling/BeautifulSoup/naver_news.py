import urllib.request, pymysql
from bs4 import BeautifulSoup

#DB연결
def conn_db():
    conn = pymysql.connect(host='localhost',user='root',password='qwer1234',db='test',
    charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor) #딕셔너리 형태로 데이터 출력

    return conn

#Table생성
def create_table():
    conn=conn_db()
    c=conn.cursor()

    sql="""CREATE TABLE if not exists articles(
        title longtext,
        url longtext,
        content longtext)"""

    c.execute(sql)
    conn.commit()
    conn.close()


#데이터 입력하기
def insert_record(new_data):
    conn=conn_db()
    c=conn.cursor()

    sql="INSERT INTO articles VALUES (%s,%s,%s)"
    c.execute(sql, new_data)
    conn.commit()
    conn.close()


#데이터 수정하기
def update_book():
    book=input('수정을 원하는 책의 제목을 입력하세요: ')

    conn=conn_db()
    c=conn.cursor()

    sql="SELECT * FROM books WHERE title LIKE '%%%s%%'"%book
    #sql="SELECT * FROM books WHERE title = '%s'"%book
    c.execute(sql)
    rows=(c.fetchall())
    for row in rows:
        print(row)

    try:
        new_recomm=int(input('수정할 추천수를 입력하세요(취소는 0) :'))
    except ValueError:
        new_recomm=0

    if new_recomm:
        #c.execute("UPDATE books SET recommend=300 WHERE title = 'Java'")
        sql="UPDATE books SET recommend=%s WHERE title = %s"
        c.execute(sql, (new_recomm,book,))
        conn.commit()

    conn.close()


#데이터 삭제하기
def delete_book():
    book=input('삭제를 원하는 책의 제목을 입력하세요: ')

    conn=conn_db()
    c=conn.cursor()

    sql="SELECT * FROM books WHERE title = '%s'"%book
    c.execute(sql)
    rows=(c.fetchall())
    for row in rows:
        print(row)

    ok=input('이 데이터를 삭제하시겠습니까? (Y/N) : ')

    if ok == 'Y' :
        sql="DELETE FROM books WHERE title=%s"
        c.execute(sql, (book,))
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

    sql="SELECT * FROM books WHERE title like %%%s%%"

    c.execute(sql, srchKey)

    book=c.fetchone()
    print(book)

    conn.close()

    return book


create_table()

url="https://news.naver.com"
response=urllib.request.urlopen(url)
bs = BeautifulSoup(response, 'html.parser')

"""
#result = bs.select('ul.section_list_ranking  a')
result = bs.find('ul','section_list_ranking').find_all('a')

for i in result:
    print(i.text)
"""


articles=[]
results=bs.select('.section_list_ranking li a')
for result in results:
    #print('제목: ', result.attrs['title'])
    #print('링크: ', result.attrs['href'])
    each_data=[result.attrs['title'], result.attrs['href']]
    
    url2="https://news.naver.com"+result.attrs['href']
    response2=urllib.request.urlopen(url2)
    bs2=BeautifulSoup(response2, 'html.parser')
    #print(bs2)
    
    content_t=bs2.select('title')
    content=bs2.select_one('#articleBodyContents')
    #print(content)
    #print(content.contents)
    #print(content.contents[8:10])

    output=""
    for item in content.contents[8:]:
        stripped = str(item).strip()

        if stripped=="":
            continue
        if stripped[0] not in ['<','/']:
            output+=str(item).strip()

    each_data.append(output)
    #print(each_data)
    articles.append(each_data)

conn=conn_db()
c=conn.cursor()

#print(articles)
c.executemany('INSERT INTO articles VALUES (%s,%s,%s)', articles)

conn.commit()
#conn.close()
