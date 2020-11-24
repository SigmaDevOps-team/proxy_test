# -*- encoding: utf-8 -*-
# """
# Python Aplication Template
# Licence: GPLv3
# """

# from flask import Flask
# from flask.ext.bootstrap import Bootstrap
# from flask.ext.sqlalchemy import SQLAlchemy
# from flask.ext.pymongo import PyMongo
# from flask.ext.login import LoginManager

# app = Flask(__name__)

# #Configuration of application, see configuration.py, choose one and uncomment.
# #app.config.from_object('configuration.ProductionConfig')
# app.config.from_object('app.configuration.DevelopmentConfig')
# #app.config.from_object('configuration.TestingConfig')

# bs = Bootstrap(app) #flask-bootstrap
# db = SQLAlchemy(app) #flask-sqlalchemy

# lm = LoginManager()
# lm.setup_app(app)
# lm.login_view = 'login'

# from app import views, models


from flask import Flask
from requests import get

app = Flask('__main__')
SITE_NAME = 'https://core-u.sigmadevops.ir/'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
  return get(f'{SITE_NAME}{path}').content

app.run(host='0.0.0.0', port=8080)
