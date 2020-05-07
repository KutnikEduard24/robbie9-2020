import time
from car.car import Car
from flask import Flask, render_template, jsonify


class CarController:
    def __init__(self, car: Car):
        self._car = car
        self._flaskObject = Flask(__name__)

    def run(self):
        for i in range(5):
            self._car.move_forward()
            self._car.stop()
            self._car.take_picture('img_' + str(i) + '.png')
            time.sleep(1)


def get_status():
    return "car is running" if (status == 1) else "car is stopped"
