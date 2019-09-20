from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    return 'Username : %s'%username

@app.route('/forminput')
def forminput():
    return render_template('form_input.html')


@app.route('/method',methods=['GET','POST'])
def login():
    if request.method=='POST':
        name=request.form['name']
        password=request.form['pass']
    else:
        name=request.args.get('name')
        password=request.args.get('pass')
    return render_template('form_result.html',name=name,password=password) 

if __name__=='__main__':
    app.run(port=80,debug=True)