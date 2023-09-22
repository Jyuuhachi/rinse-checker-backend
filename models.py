from config import db
from sqlalchemy_serializer import SerializerMixin


class DJ(db.Model, SerializerMixin):
    __tablename__='djs'
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username=db.Column(db.String,nullable=False,unique=True)
    password=db.Column(db.String, nullable = False)

    sets = db.relationship('Set', back_populates='dj')

    serialize_rules=('-set.dj', '-password', '-tracks.dj', '-shows.dj', '-sets')
    
class Track(db.Model, SerializerMixin):
    __tablename__='tracks'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    artist=db.Column(db.String, nullable=False)

    sets = db.relationship('Set', back_populates='tracks')

    serialize_rules=('-set.tracks', '-sets')

class Set_Name(db.Model, SerializerMixin):
    __tablename__='set_names'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)

    sets = db.relationship('Set', back_populates='set_name')

    serialize_rules=('-set.set_name', '-sets')

class Set(db.Model, SerializerMixin):
    __tablename__='sets'
    id=db.Column(db.Integer, primary_key=True)
    dj_id = db.Column(db.Integer, db.ForeignKey('djs.id'))
    track_id = db.Column(db.Integer, db.ForeignKey('tracks.id'))
    set_name_id = db.Column(db.Integer, db.ForeignKey('set_names.id'))
    show_id = db.Column(db.Integer, db.ForeignKey('shows.id'))

    dj = db.relationship('DJ', back_populates='sets')
    tracks = db.relationship('Track', back_populates='sets')
    set_name = db.relationship('Set_Name', back_populates='sets')
    show = db.relationship('Show', back_populates='sets')

    serialize_rules=('-dj', '-set_name', '-show', '-tracks')


class Show(db.Model, SerializerMixin):
    __tablename__='shows'
    id=db.Column(db.Integer, primary_key=True)
    date=db.Column(db.DateTime, default=db.func.now())
    name=db.Column(db.String, nullable=False)

    sets = db.relationship('Set', back_populates='show')

    serialize_rules=('-set.show', '-sets')





