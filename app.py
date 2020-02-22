from flask import Flask
from flask_cors import cross_origin
app = Flask(__name__)
CORS(app,resorces={r'/*': {"origins": '*'}})
@app.route('/')
def index():
    return "Success"

if __name__ == '__main__':
   app.run(debug=True)
