class Camera:
    def __init__(self, resolution_x, resolution_y, rotation):
        self._resolution_x = resolution_x
        self._resolution_y = resolution_y
        self._rotation = rotation

    def take_picture(self, image_filename):
        print('Taking a picture. Saving picture to ' + image_filename)
