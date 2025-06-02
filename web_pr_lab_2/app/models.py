from .database import db

class Manufacturer(db.Model):
    __tablename__ = 'manufacturers'

    manufacturer_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False, unique=True)

    cars = db.relationship('Car', backref='manufacturer', lazy=True)


class Car(db.Model):
    __tablename__ = 'cars'

    car_id = db.Column(db.Integer, primary_key=True)
    car_model = db.Column(db.String(100), nullable=False)
    production_year = db.Column(db.Integer, nullable=False)
    paint_color = db.Column(db.String(50), nullable=False)

    manufacturer_ref = db.Column(
        db.Integer,
        db.ForeignKey('manufacturers.manufacturer_id'),
        nullable=False
    )