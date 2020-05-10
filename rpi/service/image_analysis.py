from time import sleep


class ImageAnalysisService:


    def upload_image(self, image_filename):
        print("Uploading file: {image_filename}...")
        sleep(0.25)


    def detect_trafficLight(self, image_file)->bool:
        print("detecting trafic light in {image_filename}...")
        sleep(0.25)
        return False





