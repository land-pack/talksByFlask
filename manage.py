#!/usr/bin/env python
# Flask-Script is an extension that adds command line options
# to Flask.
# pip install flask-script
import os
from app import create_app
from flask.ext.script import Manager

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

if __name__ == '__main__':
    manager.run()

    # python manage.py runserver
