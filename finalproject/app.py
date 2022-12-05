from flask import Flask, render_template
import os

def return_img_stream(img_local_path):
    import base64
    img_stream=''
    with open(img_local_path,'rb') as img_f:
        img_stream=img_f.read()
        img_stream=base64.b64encode(img_stream).decode()
    return img_stream
app = Flask(__name__)
@app.route('/')
def crawler():
    img_path=r'C:\Users\Alan\Desktop\pl_class\final_project\hw4.png'
    img_stream=return_img_stream(img_path)
    return render_template('index.html',img_stream=img_stream)
if __name__ == '__main__':
    app.run(debug=True,port=5000)
    