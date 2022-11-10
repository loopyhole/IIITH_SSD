from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import (LoginManager, login_manager, login_user, logout_user, login_required, UserMixin)

app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config ['SECRET_KEY'] = 'mysecretkey'

db = SQLAlchemy (app)

class User (db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column (db.String (80), nullable = False)
    email = db.Column (db.String (80), unique = True, nullable = False)
    password = db.Column (db.String (80), nullable = False)

with app.app_context ():
    db.create_all ()

login_manager = LoginManager ()

login_manager.init_app (app)

@app.route ("/hello")
def getHello ():
    return "Hello World"

@app.route ("/user/signup", methods = ["POST"])
def handle_signup ():
    req = request.get_json ()
    name = req ['name']
    email = req ['email']
    password = req ['password']
    res = {}

    find_user = User.query.filter_by (email = email).first ()

    if (find_user is None):
        user = User (name = name, email = email, password = password)
        db.session.add (user)
        db.session.commit ()
        res["message"] = "User created"
        return res, 200
    else:
        res["errorMessage"] = "User already exists"
        return res, 500

@app.route ("/user/signin", methods = ['POST'])
def handle_signin ():
    req = request.get_json ()
    name = req ['name']
    email = req ['email']
    password = req ['password']
    res = {}

    find_user = User.query.filter_by (email = email).first ()

    if (find_user is None):
        res["errorMessage"] = "User doesn't exist"
        return res, 500
    else:
        if password != find_user.password:
            res ["errorMessage"] = "Invalid Password"
            return res, 500
        else:
            login_user (find_user)
            res["message"] = "Logged in successfully"
            return res, 200

@app.route ("/user/signout", methods = ['GET'])
@login_required
def handle_logout ():
    res = {}
    res ["message"] = "Signed out"
    return res, 200

# @app.route ("/seats/book", methods = ['POST'])
# @login_required
# def handle_booking ():


@login_manager.user_loader
def load_user(id):
    return User.query.get (int(id))

if "__main__" == __name__:
    app.run (host = "127.0.0.1", port = "3000", debug = True)