import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://caro:Sd6zxSm3mly13QlSZKAxrF1B2HBtPuUf@dpg-cfmc9f4gqg469ktjhrlg-a.oregon-postgres.render.com/db_render_06f7'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

# postgres://caro:Sd6zxSm3mly13QlSZKAxrF1B2HBtPuUf@dpg-cfmc9f4gqg469ktjhrlg-a.oregon-postgres.render.com/db_render_06f7

db = SQLAlchemy(app)

class Favquotes2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))


@app.route('/')
def index():
    result = Favquotes2.query.all()
    return render_template('index.html', result=result)


@app.route('/quotes')
def quotes():
    return render_template('quotes.html')


@app.route('/process', methods=['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Favquotes2(author=author, quote=quote)
    db.session.add(quotedata)
    db.session.commit()
    
    return redirect(url_for('index'))
