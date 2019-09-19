from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username): #위에서 전달받은 <username>의 값이 인자로 넘어감
    return 'UserName : %s'%username

@app.route('/user/<username>/<int:age>')
def show_user_age(username, age): #위에서 전달받은 <username>의 값이 인자로 넘어감
    return 'UserName : %s Age: %d'% (username, age)

@app.route('/form_input')
def show_login():
    return render_template('/form_input.html')

@app.route('/method/', methods=['GET','POST']) #default는 GET
def login():
    if request.method=='POST':
        #1
        name=request.form['username']
        pw=request.form['password']

        """
        #2
        result = request.form
        return render_template('form_result.html',result=result)
        """
    else:
        name=request.args.get('username')       
        pw=request.args.get('password')

    return render_template('form_result.html', name=name, pw=pw)

if __name__ == '__main__': # __main__(스스로 실행) / app_get (다른 파일에서 import)
    app.run(port = 80)

