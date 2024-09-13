# coding=utf-8
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '你好，阿里云！'.decode('utf-8').encode('utf-8')

app.run(host='0.0.0.0')