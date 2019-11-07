from flask import Flask,render_template,request,make_response
from flask_cors import cross_origin
app = Flask(__name__)

@app.route('/')
@cross_origin(origins="*")
def index():
    return "deployed"

if __name__ == '__main__':
   app.run()
