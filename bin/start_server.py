#!/usr/bin/env python3
import sys
sys.path.append('.')
from my_flaskr import my_flaskr

if __name__=='__main__':
    my_flaskr.app.run(debug = True)
