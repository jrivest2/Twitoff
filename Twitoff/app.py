"""Main app/routing file for Twitoff"""
from os import getenv
from flask import Flask, render_template, request
from .models import DB, User
from .twitter import add_or_update_user
# h


def create_app():
    """Creating and configuring an instance of the Flask"""
    app = Flask(__name__)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    DB.init_app(app)

    @app.route('/')
    def root():
        # renders base.html template and passes down title and users
        return render_template('base.html',title="Home", users=User.query.all())
    @app.route('/update')  # http://127.0.0.1:5000/update
    def update():
        reset()
        insert_example_users()
        return render_template('base.html', title="Home", users=User.query.all())

    @app.route('/reset')  # http://127.0.0.1:5000/reset
    def reset():
        # we must create the database
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title="Home")
    
    @app.route('/add',methods=["POST"])
    def add_user():
        if request.method == "POST":
            username = request.form['text']
            add_or_update_user(username)
        return render_template('base.html',title="Home")
    return app

def insert_example_users():
    add_or_update_user('elonmusk')
    add_or_update_user('nasa')