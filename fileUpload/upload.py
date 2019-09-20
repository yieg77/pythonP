from flask import Flask, render_template, request
import os

app=Flask(__name__) #외부파일에서 호출하는 경우 그 파일의 이름이 넘어옴

@app.route('/upload/')
def upload():
    return render_template('upload.html')

@app.route('/fileUpload', methods=["POST"])
def upload_file():
    if request.method == 'POST': 
        f=request.files['file']
        dirname=os.path.dirname(__file__)+'/uploads/'+f.filename
        print(dirname)
        f.save(dirname)

    return 'upload 성공'


if __name__ == '__main__':
    app.run(debug=True, #연관된 다른 파일을 수정해도 재실행 안해도 됨
    host='0.0.0.0',  #ip를 통해서 접속할 수 있도록
    port=80)

