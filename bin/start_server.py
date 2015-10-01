#!/usr/bin/env python3
import sys
sys.path.append('.')
from my_flaskr import my_flaskr as app
import my_flaskr

if __name__=='__main__':
    if len(sys.argv) == 1:
        app.app.run(debug = True)
    else:
        if sys.argv[1] == '-v':
            print('version: ', my_flaskr.__version__)
            sys.exit(0)
