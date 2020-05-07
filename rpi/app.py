from flask import Flask, render_template, jsonify

from boundary.car_controller import CarController
from car.car import Car

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/status", methods=['GET'])
def status():
    return jsonify(status="STOPPED")


if __name__ == '__main__':
    # carController = CarController(car=Car(17, 18, 22, 23, 5, 6, 12, 13, 1920, 1080, 270))
    # carController.run()
    app.run()
