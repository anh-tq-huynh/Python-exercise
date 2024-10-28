class Car():
    def __init__(self, registration_num : str, max_speed):
        self.registration_num = registration_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self,speed):
        self.current_speed += speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0
        return self.current_speed

    def drive(self, time : float):
        self.travelled_distance = self.travelled_distance + time * self.current_speed
        print(f"Car {self.registration_num} travelled {self.travelled_distance}")
        return self.travelled_distance

class ElectricCar(Car):
    def __init__(self, registration_num : str, max_speed, battery_capacity):
        super().__init__(registration_num, max_speed)
        self.battery_capacity = battery_capacity

    def accelerate(self, speed):
        super().accelerate(speed)

    def drive(self, time):
        super().drive(time)

class GasolineCar(Car):
    def __init__(self, registration_num : str, max_speed, tank_volume):
        super().__init__(registration_num, max_speed)
        self.tank_volume = tank_volume

    def accelerate(self, speed):
        super().accelerate(speed)

    def drive(self, time):
        super().drive(time)

electric1 = ElectricCar("ABC - 15", 180, 53.5)
gasoline1 = GasolineCar('ACD - 123', 165, 32.3)

electric1.current_speed = 120
gasoline1.current_speed = 150

electric1.drive(3)
gasoline1.drive(3)
