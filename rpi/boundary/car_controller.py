import time
from car.car import Car


class CarController:
    def __init__(self, car: Car):
        self._car = car

    def run(self):
        for i in range(5):
            self._car.move_forward()
            self._car.stop()
            self._car.take_picture('img_' + str(i) + '.png')
            time.sleep(1)
