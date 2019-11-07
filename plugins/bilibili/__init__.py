from flask import Flask,render_template,request,make_response
from flask_cors import cross_origin
import requests
import .api as api

def bilibiliAPI(app):
    @app.route('/bilibili')
    @cross_origin(origins="*")
    def ___():
        arg=request.args
        return str(arg)
