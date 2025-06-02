from .models import Car
from .database import db


def get_all_cars():
    return Car.query.all()


def get_car_by_id(car_id):
    return Car.query.get(car_id)


def create_car(car_model, production_year, paint_color, manufacturer_ref):
    new_car = Car(
        car_model=car_model,
        production_year=production_year,
        paint_color=paint_color,
        manufacturer_ref=manufacturer_ref
    )
    db.session.add(new_car)
    db.session.commit()


def update_car(car_id, car_model, production_year, paint_color, manufacturer_ref):
    car = get_car_by_id(car_id)
    if car:
        car.car_model = car_model
        car.production_year = production_year
        car.paint_color = paint_color
        car.manufacturer_ref = manufacturer_ref
        db.session.commit()


def delete_car(car_id):
    car = get_car_by_id(car_id)
    if car:
        db.session.delete(car)
        db.session.commit()
