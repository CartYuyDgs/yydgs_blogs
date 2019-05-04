from exts import db
import shortuuid
import enum,datetime
from werkzeug.security import generate_password_hash,check_password_hash

class BoardModel(db.Model):
    __tablename__ = 'board'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20),nullable=True)


class ContextModel(db.Model):
    __tablename__ = 'context'
    id = db.Column(db.String(100),primary_key=True,default=shortuuid.uuid)
    title = db.Column(db.String(50),nullable=True)
    context = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.datetime.now)
    praise = db.Column(db.Boolean,default=False)
    board_id = db.Column(db.Integer,db.ForeignKey('board.id'))

    board = db.relationship('BoardModel',backref='context')

class Crawl_poem(db.Model):
    __tablename__ = 'poem'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50),nullable=True)
    author = db.Column(db.String(20),nullable=True)
    context = db.Column(db.Text,nullable=False)

