#1 

class Car:
    def __init__(self, doors, model, year):
        self.doors = doors
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, speed_delta):
        self.speed += speed_delta

    def brake(self, speed_delta):
        if self.speed - speed_delta < 0:
            self.speed = 0
        else :
            self.speed -= speed_delta



