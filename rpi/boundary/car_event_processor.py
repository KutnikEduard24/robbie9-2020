from pydispatch import dispatcher
import threading
import time
from car.car_status import CarStatus
from service.car_thread import RUNNING_SENDER,RUNNING_SIGNAL,STOPPED_SENDER,STOPPED_SIGNAL,TAKE_PICTURE_SENDER,TAKE_PICTURE_SIGNAL,UPLOAD_IMAGE_SENDER,UPLOAD_IMAGE_SIGNAL,DETECT_TRAFFIC_LIGHT_SIGNAL,DETECT_TRAFFIC_LIGHT_SENDER,IMAGE_UPLOADED_SENDER,IMAGE_UPLOADED_SIGNAL


class CarEventProcessor:

    def __init__(self):
       # dispatcher.connect(event_dispatcher_receive, signal=BOB_SIGNAL, sender=BOB_SENDER)
        dispatcher.connect(self.running_dispatcher_receive, signal=RUNNING_SIGNAL, sender=RUNNING_SENDER)
        dispatcher.connect(self.stopped_dispatcher_receive,signal=STOPPED_SIGNAL,sender=STOPPED_SENDER)
        dispatcher.connect(self.taking_picture_dispatcher_receive,signal=TAKE_PICTURE_SIGNAL,sender=TAKE_PICTURE_SENDER)
        dispatcher.connect(self.uploading_picture_dispatcher_receive,signal=UPLOAD_IMAGE_SIGNAL,sender=UPLOAD_IMAGE_SENDER)
        dispatcher.connect(self.image_uploaded_dispatcher_receive, signal=IMAGE_UPLOADED_SIGNAL, sender=IMAGE_UPLOADED_SENDER)

    def running_dispatcher_receive(self):
        print('running')

    def stopped_dispatcher_receive(self):
        print('stoppe')

    def taking_picture_dispatcher_receive(self):
        print('taking picture')

    def uploading_picture_dispatcher_receive(self):
        print('uploading pic...')

    def image_uploaded_dispatcher_receive(self):
        print('img uploaded...')


