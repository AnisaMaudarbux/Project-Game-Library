from application import app, db
from application.models import Item
from application.forms import AddItem, EditItem
from flask import request, render_template, redirect, url_for

@app.route('/')
def home():
    items = Item.query.all()
    return render_template('home.html', tasks=items)

@app.route('/add', methods = ['GET', 'POST'])
def add():
    form = AddItem()
    if request.method == 'POST':
        name = form.name.data
        publ = form.publ.data
        genre = form.genre.data
        hours = form.hours.data
        if form.validate_on_submit():
            newitem = Item(name=name, publ=publ, genre=genre, hours=hours)
            db.session.add(newitem)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)

@app.route('/update/<int:tid>', methods = ['GET', 'POST'])
def update(tid):
    form = EditItem()
    item = Item.query.get(tid)
    if request.method == 'POST' and form.validate_on_submit():
        item.name = form.name.data
        item.publ = form.dpubl.data
        item.hours = form.hours.data
        item.genre = form.genre.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('update.html', form=form, game=item)

@app.route('/delete/<int:tid>')
def delete(tid):
    item = Item.query.get(tid)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('home'))