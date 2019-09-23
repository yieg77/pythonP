from flask import Flask,render_template,request,redirect,url_for

import mariadbfunc as db
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('homeblock.html')

@app.route('/formtest')
def formtest():
    return render_template('formtestblock.html')

@app.route('/insertbook',methods=['POST'])
def insertbook():
    data=(request.form['title'],request.form['date'],request.form['publisher'],request.form['pages'],request.form['recommend'])
    db.create_table()
    db.insert_books(data)
    return redirect(url_for('booklist'))

@app.route('/booklist')
def booklist():
    books=db.all_books()
    print(books)
    return render_template('booklist.html',books=books)

if __name__=='__main__':
    app.run(debug=True,port=80)