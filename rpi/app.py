from flask import Flask, render_template

from boundary.car_controller import CarController
from car.car import Car

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    car = Car(17, 18, 22, 23, 5, 6, 12, 13, 1920, 1080, 270)
    carController = CarController(car=car, flask_app=app)
    app.run()