from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    datejoined = db.Column(db.DateTime, nullable=False)
    favorites = db.relationship('Favorite', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "datejoined": self.datejoined.isoformat()
        }

class Species(db.Model):
    __tablename__ = 'species'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    characters = db.relationship('Character', backref='species', lazy=True)

    def __repr__(self):
        return'<Species %r>' %self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'))
    planet = db.relationship('Planet', backref='characters')
    favorites = db.relationship('Favorite', backref='character', lazy=True)

    def __repr__(self):
        return'<Character %r>' %self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "planet_id": self.planet_id,
            "species_id": self.species_id
        }

class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    climate = db.Column(db.String(50), nullable=False)
    terrain = db.Column(db.String(50), nullable=False)
    favorites = db.relationship('Favorite', backref='planet', lazy=True)

    def __repr__(self):
        return'<Planet %r>' %self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "climate": self.climate,
            "terrain": self.terrain
        }

class Favorite(db.Model):
    __tablename__ = 'favorite'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=True)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=True)

    def __repr__(self):
        return'<Favorite %r>' %self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id
        }
