from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
#from flask_bcrypt import Bcrypt


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///app.db"
db=SQLAlchemy(app)
#1
migrate=Migrate(app,db)
CORS(app, origins=["http://localhost:3000"])
