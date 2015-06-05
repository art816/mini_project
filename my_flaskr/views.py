#rom app import app
from flask import render_template

import sys
sys.path.append('../../NMS')
sys.path.append('app/templates')

from nms.core.context import ContextCreator

def route(app):
    print('views')
    @app.route('/')
    @app.route('/index')
    def index():
        user = { 'nickname': 'Miguel' } # выдуманный пользователь
        posts = [ # список выдуманных постов
            { 
                'author': { 'nickname': 'John' }, 
                'body': 'Beautiful day in Portland!' 
            },
            { 
                'author': { 'nickname': 'Susan' }, 
                'body': 'The Avengers movie was so cool!' 
            }
        ]
        context_creator = ContextCreator('buer')
        context = context_creator.from_file()
        #assert False
        return render_template("index.html",
                               title='Home', 
                               user=user,
                               posts=posts,
                               devices=context.devices)


