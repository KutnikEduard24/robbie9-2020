from car.car import Car
from service.car_thread import CarThread
from service.image_analysis import ImageAnalysisService


class CarService:
    def __init__(self, car: Car, image_analysis_service: ImageAnalysisService):
        self._car = car
        self._imageAnalysisService = image_analysis_service
        self._thread = None

    def run(self):
        if self._thread:
            return

        self._thread = CarThread(car=self._car, image_analysis_service=self._imageAnalysisService)
        self._thread.start()

    def stop(self):
        if self._thread:
            self._thread.stop()
            self._thread.join()
            self._thread = None
