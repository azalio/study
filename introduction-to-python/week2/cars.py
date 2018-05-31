class BaseCar:
    def __init__(self, car_type, photo_file_name):
        self.car_type = car_type
        self.photo_file_name = photo_file_name

    def get_photo_file_ext(self):
        # os.path.splitext
        pass


class Car(BaseCar):
    pass


class Truck(BaseCar):
    def __init__(self, car_type, photo_file_name, body_length=0, body_width=0, body_height=0):
        super().__init__(car_type, photo_file_name)
        self.body_length = body_length
        self.body_width = body_width
        self.body_height = body_height

    def get_body_volume(self):
        """возвращающий объем кузова в метрах кубических"""


class SpecMachine(BaseCar):
    pass
