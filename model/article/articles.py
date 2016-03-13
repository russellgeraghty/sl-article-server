from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Article(db.Model):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    headline = Column(String(80))
    story_body = Column(String(4096))

    def __init__(self, headline, story_body):
        self.headline = headline
        self.story_body = story_body

    def __repr__(self):
        return '<Article %d: %r>' % (self.id, self.headline)
