from flask_testing import TestCase
from application import app, db
from application.models import Item
from flask import url_for
from datetime import date

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
        SECRET_KEY = 'test_secret_key',
        DEBUG=True,
        WTF_CSRF_ENABLED = False)
        return app
    
    def setUp(self):
        db.create_all()
        sample = Item(name='Sample Item', desc='This is a sample item', due=date(2022, 1, 1), status='todo')
        db.session.add(sample)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_get_home(self):
        response = self.client.get(url_for('home'))
        self.assert200
        self.assertIn(b'Sample Item', response.data)

class TestAdd(TestBase):
    def test_post_add(self):
        response = self.client.post(url_for('add'),
        data = dict(name='Sample Item 2', desc='Test adding an item', due=date(2021, 12, 25), status='todo'),
        follow_redirects=True)
        self.assert200
        self.assertIn(b'Sample Item 2', response.data)

class TestUpdate(TestBase):
    def test_post_update(self):
        response = self.client.post(url_for('update', tid=1),
        data = dict(name='Updated Sample Item', desc='Test updating an item', due=date(2022, 1, 1), status='done'),
        follow_redirects=True)
        self.assert200
        self.assertIn(b'Updated Sample Item', response.data)

class TestDel(TestBase):
    def test_get_delete(self):
        response = self.client.get(url_for('delete', tid=1))
        self.assert200
        self.assertNotIn(b'Sample Item', response.data)

class TestAddView(TestBase):
    def test_get_add(self):
        response = self.client.get(url_for('add'))
        self.assert200
        self.assertIn(b'Add an Item', response.data)

class TestUpdateView(TestBase):
    def test_get_update(self):
        response = self.client.get(url_for('update', tid=1))
        self.assert200
        self.assertIn(b'Update', response.data)