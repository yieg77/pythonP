from flask import Flask,render_template


app=Flask(__name__)
@app.route('/index')
def index():
    return 'hello world!'

@app.route('/')
def home():
    return render_template('homeblock.html')

@app.route('/formtest')
def formtest():
    return render_template('formtest1.html')

if __name__=='__main__':
   app.run(debug=True,port=80) 