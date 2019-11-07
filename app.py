import requests
from urllib.parse import urlencode
def get_response(msg):
    key={
        "key":"free",
        "appid":0,
        "msg":"你好"
    }
    response=requests.get("http://api.qingyunke.com/api.php?"+urlencode(key)).json()
    return None if response["result"] else response["content"]

from flask import Flask,render_template,request,make_response
from flask_cors import cross_origin
import requests
app = Flask(__name__)

@app.route('/qyk')
@cross_origin(origins="*")
def qyk():
    inp=list(request.args)[0]
    return get_response(inp)

@app.route('/cors')
@cross_origin(origins="*")
def cors():
    inp=list(request.args)[0]
    return requests.get(inp).text

@app.route('/')
@cross_origin(origins="*")
def index():
    return "deployed"

if __name__ == '__main__':
   app.run()
