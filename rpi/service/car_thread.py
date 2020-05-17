import time
from threading import Thread
from pydispatch import dispatcher

from car.car_status import CarStatus
from car.car import Car
from service.image_analysis import ImageAnalysisService

TAKE_PICTURE_SIGNAL = 'image_taken_signal'
TAKE_PICTURE_SENDER = 'image_taken_sender'
UPLOAD_IMAGE_SIGNAL = 'upload_image_signal'
UPLOAD_IMAGE_SENDER = 'upload_image_sender'
IMAGE_UPLOADED_SIGNAL = 'image_uploaded_signal'
IMAGE_UPLOADED_SENDER = 'image_uploaded_sender'
IMAGE_ANALYZE_SIGNAL = 'image_analyze_signal'
IMAGE_ANALYZE_SENDER = 'image_analyze_sender'
DETECT_TRAFFIC_LIGHT_SIGNAL = 'detect_traffic_light_signal'
DETECT_TRAFFIC_LIGHT_SENDER = 'detect_traffic_light sender'
MOVE_FORWARD_SIGNAL = 'move_forward_signal'
MOVE_FORWARD_SENDER = 'move_forward_sender'
NO_TRAFFIC_LIGHT_DETECTED_SIGNAL = 'no_traffic_light_detected_signal'
NO_TRAFFIC_LIGHT_DETECTED_SENDER = 'no_traffic_light_detected_sender'
RUNNING_SIGNAL = 'running_signal'
RUNNING_SENDER = 'running_sender'
STOPPED_SIGNAL = 'stopped_signal'
STOPPED_SENDER = 'stopped_sender'


class CarThread(Thread):
    def __init__(self, car: Car, image_analysis_service: ImageAnalysisService):
        super(CarThread, self).__init__()
        self._car: Car = car
        self._imageAnalysisService: ImageAnalysisService = image_analysis_service
        self._running = True

    def run(self) -> None:
        while self._running:
            image_taken = 'img.png'
            self._car.take_picture(image_taken)
            dispatcher.send(message='TAKING_PICTURE', signal=TAKE_PICTURE_SIGNAL, sender=TAKE_PICTURE_SENDER)
            self._imageAnalysisService.upload_image(image_taken)
            dispatcher.send(message='UPLOADING_PICTURE', signal=UPLOAD_IMAGE_SIGNAL, sender=UPLOAD_IMAGE_SENDER)
            self._imageAnalysisService.detect_traffic_light(image_taken)
            dispatcher.send(message='DETECTING_TRAFFIC_LIGHT', signal=DETECT_TRAFFIC_LIGHT_SIGNAL,
                            sender=DETECT_TRAFFIC_LIGHT_SENDER)
            self._car.move_forward()
            dispatcher.send(message='MOVING_FORWARD', signal=MOVE_FORWARD_SIGNAL,
                            sender=MOVE_FORWARD_SENDER)
            time.sleep(1)
        self._car.stop()

    def stop(self):
        self._running = False
