from flask import Flask
from flask_sqlalchemy sqlalchemy



app = FLask(__name__)
app.config['SQLALCHEMY_DATABSE_URI'] = 'sqlite://db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# alternative for bigger projects to setup app with db
# db.init_app(app)

