from sqlalchemy.sql.schema import ForeignKey
from application import app, db
from application.models import Game, Engine
from application.forms import AddItem, EditItem
from flask import request, render_template, redirect, url_for
from wtforms.validators import DataRequired

@app.route('/')
def home():
    items = Game.query.all()
    return render_template('home.html', game=items)

@app.route('/add', methods = ['GET', 'POST'])
def add():
    form = AddItem()
    if request.method == 'POST':
        name = form.name.data
        dev = form.dev.data
        genre = form.genre.data
        hours = form.hours.data
        if form.validate_on_submit():
            newgame = Game(name=name, dev=dev, genre=genre, hours=hours)
            db.session.add(newgame)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)

@app.route('/update/<int:tid>', methods = ['GET', 'POST'])
def update(tid):
    form = EditItem()
    item = Game.query.get(tid)
    if request.method == 'POST' and form.validate_on_submit():
        item.name = form.name.data
        item.dev = form.dev.data
        item.hours = form.hours.data
        item.genre = form.genre.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('update.html', form=form, game=item)

@app.route('/delete/<int:tid>')
def delete(tid):
    item = Game.query.get(tid)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('home'))