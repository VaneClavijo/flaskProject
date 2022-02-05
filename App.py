from flask import Flask, session,config
from flask_session import Session  # https://pythonhosted.org/Flask-Session
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

app = Flask(__name__)
app.config.update(SECRET_KEY=os.urandom(24))
app.config['SESSION_TYPE'] = 'filesystem'
bootstrap = Bootstrap(app)
login_manager=LoginManager()

Session(app)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:admin@localhost/mvc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

from werkzeug.middleware.proxy_fix import ProxyFix
from controllers.infoController import*
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

if __name__=='__main__':
    app.run(debug=True, host= '192.168.100.83',port=220)
    app.secret_key = '684651454165416'
    app.config['SESSION_TYPE'] = 'filesystem'

    session.init_app(app)
