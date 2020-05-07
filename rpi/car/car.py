from car.camera import Camera
from car.car_status import CarStatus
from car.motor import Motor


class Car:
    """ This car represents the Raspberry-Py car """

    def __init__(self, m1_forward, m1_backward, m2_forward, m2_backward, m3_forward, m3_backward, m4_forward,
                 m4_backward, resolution_x, resolution_y, rotation, status=CarStatus.STOPPED):
        self._camera = Camera(resolution_x, resolution_y, rotation)
        self._motor1 = Motor(m1_forward, m1_backward)
        self._motor2 = Motor(m2_forward, m2_backward)
        self._motor3 = Motor(m3_forward, m3_backward)
        self._motor4 = Motor(m4_forward, m4_backward)
        self.status = status

    def move_forward(self):
        print('Moving the car forward...')
        self.status = CarStatus.RUNNING
        self._motor1.move_forward()
        self._motor2.move_forward()
        self._motor3.move_forward()
        self._motor4.move_forward()

    def move_backward(self):
        print('Moving the car backward...')
        self.status = CarStatus.RUNNING
        self._motor1.move_backward()
        self._motor2.move_backward()
        self._motor3.move_backward()
        self._motor4.move_backward()

    def stop(self):
        print('Stopping the car...')
        self.status = CarStatus.STOPPED
        self._motor1.stop()
        self._motor2.stop()
        self._motor3.stop()
        self._motor4.stop()

    def take_picture(self, image_filename):
        self._camera.take_picture(image_filename)
