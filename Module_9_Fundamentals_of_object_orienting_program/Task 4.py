import random

class Car():
    def __init__(self, registration_num : str):
        self.registration_num = registration_num
        self.max_speed = float(f"{random.uniform(100.00,200.00):.2f}")
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self,speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0
        return self.current_speed

    def drive(self, time : float):
        self.travelled_distance = self.travelled_distance + time * self.current_speed
        return self.travelled_distance

    def __str__(self):
        return (f"Registration number: {self.registration_num}\n"
                f"Maximum speed: {self.max_speed} km/h \n"
                f"Current speed: {self.current_speed} km/h \n"
                f"Travelled distance: {self.travelled_distance} km")

cars = []
for i in range(10):
    cars.append(Car(f"ABC - {i+1}"))

total_distance = 0
while total_distance <= 10_000:
    for i in cars:
        i.accelerate(random.uniform(-10,15))
        i.drive(1.0)
        total_distance = max(i.travelled_distance, total_distance)

from prettytable import PrettyTable
t = PrettyTable(["Car","Max Speed","Travelled Distance"])
for i in cars:
    t.add_row([i.registration_num, f"{i.max_speed:.2f}", f"{i.travelled_distance:.2f}"])
print(t)









