from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    return 'Hello world'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/formtest')
def formtest():
    return render_template('formtest.html')

if __name__ == '__main__':
    app.run(port = 80)

#app.run(debug=True, host='0.0.0.0')  #원격 컴퓨터에서 접속 가능한 설정 시작
#app.debug = True
#app.run(host='0.0.0.0', port = 80)

