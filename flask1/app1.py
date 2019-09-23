from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    return render_template('result.html',name=username)

@app.route('/user/<username>/<int:age>')
def show_user_profile_age(username,age):
    return render_template('result.html',name=username,age=age)

@app.route('/user')
def show_user():
    name=request.args.get('name')
    return render_template('result.html',name=name)

@app.route('/user',methods=['POST'])
def show_user_post():
    name=request.form['username']
    result=request.form
    return render_template('result.html',name=name,result=result)

@app.route('/forminput')
def forminput():
    return render_template('form_input.html')

if __name__=='__main__':
    app.run(debug=True,port=80)