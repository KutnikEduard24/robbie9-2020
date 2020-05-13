from datetime import time
from threading import Thread, Lock
from car.car import Car
import time

from service.image_analysis import ImageAnalysisService


class CarThread(Thread):
    def __init__(self, car: Car, image_analysis_service: ImageAnalysisService):
        super(CarThread, self).__init__()
        self._car: Car = car
        self._imageAnalysisService: ImageAnalysisService = image_analysis_service
        self._running = True
        self._lock = Lock()


    def run(self) -> None:
        while self._running:
            image_taken = 'img.png'
            self._car.take_picture(image_taken)
            self._imageAnalysisService.upload_image(image_taken)
            self._imageAnalysisService.detect_traffic_light(image_taken)
            self._car.move_forward()
            time.sleep(1)
        self._car.stop()

    def stop(self):
        self._lock.acquire()
        self._running = False
        self._lock.release()
