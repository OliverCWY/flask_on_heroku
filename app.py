from flask import Flask
from flask_cors import cross_origin
app = Flask(__name__)

@app.route('/')
@cross_origin(origins="*")
def index():
    return "Success"

if __name__ == '__main__':
   app.run(debug=True)
