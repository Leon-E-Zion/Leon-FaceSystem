from leon_pre import *
import os
import json
from flask import jsonify
import io

from flask import Flask, request
import numpy as np
import os
from PIL import Image
app = Flask(__name__)

# app.debug = True
# 安卓端访问此处后端，后端通过requests请求获取注册传递数据
# 访问请求 {'name':'Leon','img':img_file}
@app.route('/register', methods=["POST"])
def register_insert():
    # 获取用户姓名
    upload_file = request.files['file']
    byte_stream = io.BytesIO(upload_file.read())  
    img = Image.open(byte_stream) 
    name = request.values.get("name")
    num =  request.values.get("num")
    print(num)
    # 文件存储 - 此处注意传输过程中图像选用流式传输，基于二进制形式实现
    try:
        os.mkdirs(os.path.join(os.getcwd(),'face_dataset'))
    except:
        pass
    img.save(os.path.join(os.getcwd(),'face_dataset','{}_{}.jpg'.format(name,num)))
    respose = {
        "opt_return": 'image saved'
    }
    return respose
    
def embedding():
    path = os.path.join(os.getcwd(),'encoding.py')
    os.system('python {}'.format(path))
    
    
@app.route('/embedding')
def embedding_in():
    embedding()
    respose = {
        "opt_return": 'embedded'
    }
    return respose
    
import base64
from flask import request
from flask import Flask,jsonify
import os

net = get_model()
# 定义路由
@app.route("/a", methods=['POST'])
def get_frame():
    # 接收图片
    upload_file = request.files['file']
    img = upload_file.read()
    byte_stream = io.BytesIO(img)  
    img = Image.open(byte_stream) 
    img.save(os.path.join(os.getcwd(),'tmp_1.jpg'))
    # 检测用户
    output = get_role(net,os.path.join(os.getcwd(),'tmp_1.jpg'))
    respose = {
        "urls": str(output['output_name'])
    }
    return jsonify(respose)

from flask import jsonify
@app.route('/e', methods=['POST'])
def eg():
    respose = {
        "code": 200,
        "urls": 1234
    }
    return jsonify(respose)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')