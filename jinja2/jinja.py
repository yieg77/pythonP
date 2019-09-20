from flask import Flask, render_template, request
import os, pymysql

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
    create_table()

    conn=conn_db()
    c=conn.cursor()

    sql="INSERT INTO books VALUES (%s,%s,%s,%s,%s)"
    c.execute(sql, new_data)
    conn.commit()
    conn.close()

#전체 데이터 조회
def show_all_books():
    conn=conn_db()
    c=conn.cursor()

    sql="SELECT * FROM books"

    c.execute(sql)

    rows=c.fetchall()

    conn.close()

    return rows


app=Flask(__name__) #외부파일에서 호출하는 경우 그 파일의 이름이 넘어옴

@app.route('/')
def main():
    return render_template('home_block.html')

@app.route('/jinja/')
def upload():
    return render_template('home_block.html')

@app.route('/formtest/')
def formtest():
    return render_template('form_block.html')

@app.route('/insertBook', methods=["POST"])
def insertBook():
    bookName=request.form['bookName']
    bookDate=str(request.form['bookDate'])
    publisher=request.form['publisher']
    pages=int(request.form['pages'])
    recomm=int(request.form['recomm'])

    new_data=[bookName, bookDate, publisher, pages, recomm]

    print(new_data)
    insert_record(new_data)
    result=show_all_books()

    print(result)

    return render_template("show_Books.html", result=result)

@app.route('/showBooks')
def showBooks():
    result=show_all_books()
    return render_template("show_Books.html", result=result)


if __name__ == '__main__':
    app.run(debug=True, #연관된 다른 파일을 수정해도 재실행 안해도 됨
    host='0.0.0.0',  #ip를 통해서 접속할 수 있도록
    port=80)

