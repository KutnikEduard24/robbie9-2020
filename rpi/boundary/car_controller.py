from time import sleep

from flask import Flask, jsonify
from service.image_analysis import ImageAnalysisService
from car.car import Car


class CarController:
    def __init__(self, car: Car, flask_app: Flask, image_analysis:ImageAnalysisService):
        self._car = car
        self._flaskApp = flask_app
        self._image_analysis = image_analysis
        self._flaskApp.route("/status", methods=['GET'])(self.status)
        self._flaskApp.route("/Run", methods=["PUT"])(self.run())

    def status(self):
        return jsonify(status=str(self._car.status.name))

    def run(self):
        for i in range(5):
            image = 'img_' + str(i) + '.png'
            self._car.take_picture(image)
            self._image_analysis.upload_image(image)
            self._image_analysis.detect_trafficLight(image)
            self._car.move_forward()
            sleep(1)
            self._car.stop()

