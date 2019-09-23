from flask import Flask, render_template, request, redirect, url_for
import os, pymysql
import mariadb_func as db

#전체 데이터 조회
def show_all_books(srchKey):
    conn=db.conn_db()
    c=conn.cursor()

    sql="SELECT * FROM books "
    if srchKey != "":
        sql += "WHERE title like '%%%s%%' or publisher like '%%%s%%'"%(srchKey,srchKey)

    print(sql)

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

    #print(new_data)
    db.insert_record(new_data)
    #books=show_all_books()

    #print(books)

    #return render_template("book_list.html", books=books)
    #return redirect('/bookList')
    return redirect(url_for('showBooks')) #함수이름

@app.route('/bookList', methods=['GET','POST'])
def showBooks():
    if request.method=='POST':
        srchKey=request.form['srchKey']
        print("srchKey", srchKey)
        books=show_all_books(srchKey)
    else:
        books=show_all_books("")

    return render_template("book_list.html", books=books)

@app.route('/content/<title>')
def showContent(title):
    #print("title",title)
    book = db.show_Book(title)
    return render_template('content.html',book=book)

@app.route('/update', methods=["POST"])
def updateContent():
    title=request.form['title']
    bookDate=request.form['bookDate']
    publisher=request.form['publisher']
    pages=request.form['pages']
    recommend=request.form['recomm']

    db.update_book(title, bookDate, publisher, pages, recommend)
    return redirect(url_for('showBooks')) #함수이름

@app.route('/delete/<title>')
def deleteContent(title):
    db.delete_book(title)
    return redirect(url_for('showBooks')) #함수이름


if __name__ == '__main__':
    app.run(debug=True, #연관된 다른 파일을 수정해도 재실행 안해도 됨
    host='0.0.0.0',  #ip를 통해서 접속할 수 있도록
    port=80)

