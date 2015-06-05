#!/usr/bin/env python3

#from app import app

from flask import Flask
import views

print('flask')
app = Flask(__name__)
app.config.from_object('config')
views.route(app)

if __name__=='__main__':
    app.run(debug = True)
