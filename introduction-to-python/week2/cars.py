import csv
import os
import sys


class BaseCar:
    def __init__(self, car_type=None, photo_file_name=None, brand=None, carrying=None):
        self.car_type = car_type
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[-1]


class Car(BaseCar):
    def __init__(self, passenger_seats_count=None):
        super().__init__()
        self.passenger_seats_count = passenger_seats_count


class Truck(BaseCar):
    def __init__(self, body_length=0.0, body_width=0.0, body_height=0.0):
        super().__init__()
        self.body_length = body_length
        self.body_width = body_width
        self.body_height = body_height

    def get_body_volume(self):
        """возвращающий объем кузова в метрах кубических"""
        return self.body_height * self.body_length * self.body_width


class SpecMachine(BaseCar):
    def __init__(self, extra=None):
        super().__init__()
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            try:
                car_type, brand, passenger_seats_count, photo_file_name, body_whl, carrying, extra = row
            except ValueError:
                continue
            # print(row)
            if 'car' in car_type:
                passenger_seats_count = int(passenger_seats_count)
                obj = Car(passenger_seats_count=passenger_seats_count)
            elif 'truck' in car_type:
                try:
                    body_length, body_width, body_height = map(float, body_whl.split('x'))
                    obj = Truck(body_length=body_length, body_width=body_width, body_height=body_height)
                except ValueError:
                    obj = Truck()
            elif 'spec_machine' in car_type:
                obj = SpecMachine(extra=extra)
            obj.car_type = car_type
            obj.photo_file_name = photo_file_name
            obj.brand = brand
            carrying = float(carrying)
            obj.carrying = carrying
            car_list.append(obj)

    return car_list


if __name__ == '__main__':
    csv_filename = sys.argv[1]
    print(get_car_list(csv_filename))
