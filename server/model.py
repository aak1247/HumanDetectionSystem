from .app import db

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key = True)
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

class Record(db.Model):
    __tablename__ = 'records'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key = True)
    def __repr__(self):
        return '<User %r>' % self.username

class Picture(db.Model):
    __tablename__ = 'pictures'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key = True)
    def __repr__(self):
        return '<User %r>' % self.username

class Job(db.Model):
    __tablename__ = 'jobs'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key = True)
    def __repr__(self):
        return '<User %r>' % self.username

class Resource(db.Model):
    __tablename__ = 'resources'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique = True)
    password = db.Column(db.String(32), nullable = False)

    def __repr__(self):
        return '<User %r>' % self.username
