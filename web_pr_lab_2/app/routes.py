from flask import Blueprint, render_template, request, redirect, url_for, flash
from .services import get_all_cars, get_car_by_id, create_car, update_car, delete_car
from .models import Manufacturer
from .database import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    cars = get_all_cars()
    return render_template('vehicle_list.html', cars=cars)


@main.route('/vehicle/add', methods=['GET', 'POST'])
def add_car():
    if request.method == 'POST':
        try:
            model = request.form['car_model']
            year = int(request.form['production_year'])
            if year < 2000 or year > 2025:
                flash('Рік випуску має бути між 2000 і 2025')
                return redirect(url_for('main.add_car'))

            color = request.form['paint_color']
            manufacturer_id = int(request.form['manufacturer_ref'])

            create_car(model, year, color, manufacturer_id)
            return redirect(url_for('main.index'))
        except Exception:
            flash('Помилка при створенні авто')
            return redirect(url_for('main.add_car'))

    manufacturers = Manufacturer.query.all()
    return render_template('vehicle_form.html', manufacturers=manufacturers)


@main.route('/vehicle/<int:car_id>/edit', methods=['GET', 'POST'])
def edit_car(car_id):
    car = get_car_by_id(car_id)

    if request.method == 'POST':
        try:
            model = request.form['car_model']
            year = int(request.form['production_year'])
            if year < 2000 or year > 2025:
                flash('Рік випуску має бути між 2000 і 2025')
                return redirect(url_for('main.edit_car', car_id=car_id))
            color = request.form['paint_color']
            manufacturer_id = int(request.form['manufacturer_ref'])

            update_car(car_id, model, year, color, manufacturer_id)
            return redirect(url_for('main.index'))
        except Exception:
            flash('Помилка при оновленні авто')
            return redirect(url_for('main.edit_car', car_id=car_id))

    manufacturers = Manufacturer.query.all()
    return render_template('vehicle_form.html', car=car, manufacturers=manufacturers)


@main.route('/vehicle/<int:car_id>/delete')
def delete_car_route(car_id):
    try:
        delete_car(car_id)
    except Exception:
        flash('Помилка при видаленні авто')
    return redirect(url_for('main.index'))
