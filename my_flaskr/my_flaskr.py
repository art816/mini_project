#!/usr/bin/env python3

from flask import Flask
from my_flaskr import views

print('flask')
app = Flask(__name__)
app.config.from_object('my_flaskr.config')
views.route(app)

