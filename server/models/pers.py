from ..app import db
import uuid

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.String(32), primary_key = True)
    username = db.Column(db.String(64), unique = True)
    password = db.Column(db.String(64), nullable = False)
    role = db.Column(db.String(1), nullable = False)
    def __init__(self, username, password, role = '0'):
        self.id = uuid.uuid1().hex
        self.username = username
        self.password = password
        self.role = '0'

    def __repr__(self):
        return str({
            "id": str(self.id),
            "username": str(self.username),
            "password": str(self.password)
        })


    def __str__(self):
        return str({
            "id": str(self.id),
            "username": str(self.username),
            "password": str(self.password)
        })

class Record(db.Model):
    __tablename__ = 'records'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.String(32), primary_key = True)

    def __repr__(self):
        return '<User %r>' % self.username

class Image(db.Model):
    __tablename__ = 'images'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.String(32), primary_key = True)
    name = db.Column(db.String(32))
    state = db.Column(db.String(1))
    def __init__(self, name):
        self.id = uuid.uuid1().hex
        self.name = name
        self.state = "0"

    def __repr__(self):
        return str({
            "id": self.id,
            "name": self.name,
            "state": self.state
        })

    def __str__(self):
        return str({
            "id": self.id,
            "name": self.name,
            "state": self.state
        })

class Repo(db.Model):
    __tablename__ = 'repos'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.String(32), primary_key = True)
    author = db.Column(db.String(32), db.ForeignKey(User.id))
    name = db.Column(db.String(60))
    max = db.Column(db.Integer)
    cur = db.Column(db.Integer)
    status = db.Column(db.String(1))

    def __init__(self, author, name, max = 0):
        self.id = uuid.uuid1().hex
        self.author = author
        self.name = name
        self.max = max
        self.cur = 0
        self.status = "0"

    def __str__(self):
        return str({
            "id": self.id,
            "author": self.author,
            "name": self.name,
            "max": self.max,
            "cur": self.cur,
            "state": self.status
         })

repo_images = db.Table('repo_imgs',
    db.Column('repo_id', db.String(32), db.ForeignKey(Repo.id)),
    db.Column('img_id', db.String(32), db.ForeignKey(Image.id))
)


class Videos(db.Model):
    __tablename__ = 'videos'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.String(32), primary_key = True)
    name = db.Column(db.String(32))
    state = db.Column(db.String(1))
    def __init__(self, name):
        self.id = uuid.uuid1().hex
        self.name = name
        self.state = "0"

    def __repr__(self):
        return str({
            "id": self.id,
            "name": self.name,
            "state": self.state
        })

    def __str__(self):
        return str({
            "id": self.id,
            "name": self.name,
            "state": self.state
        })

class Job(db.Model):
    __tablename__ = 'jobs'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.String(32), primary_key = True)
    video_id = db.Column(db.String(32), db.ForeignKey("videos.id"))
    state = db.Column(db.String(1))
    def __repr__(self):
        return '<User %r>' % self.username