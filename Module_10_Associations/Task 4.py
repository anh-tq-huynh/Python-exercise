import random
from prettytable import PrettyTable

class Car():
    def __init__(self, registration_num : str):
        self.registration_num = registration_num
        self.max_speed = float(f"{random.uniform(100.00,200.00):.2f}")
        self.current_speed = 0
        self.travelled_distance = 0
        self.winner = ""

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

class Race:
    def __init__(self,race_name : str, race_length: float):
        self.race_name = race_name
        self.race_length = race_length
        self.car_list = []
        for i in range(10):
            self.car_list.append(Car(f"ABC - {i + 1}"))

    def hour_pass(self):
        for i in self.car_list:
            i.accelerate(random.uniform(-10, 15))
            i.drive(1.0)



    def print_status(self):
        t = PrettyTable(["Car", "Max Speed","Current Speed", "Travelled Distance", "Winner"])
        for i in self.car_list:
            t.add_row([i.registration_num, f"{i.max_speed:.2f}", f"{i.current_speed:.2f}", f"{i.travelled_distance:.2f}", f"{i.winner}"])
        print(t)

    def race_finish(self):
        total_distance = 0
        for i in self.car_list:
            total_distance = max(i.travelled_distance, total_distance)
        if total_distance >= self.race_length:
            return True

    def winner(self):
        winner_distance = 0
        for i in self.car_list:
            winner_distance = max(i.travelled_distance, winner_distance)
        for i in self.car_list:
            if i.travelled_distance == winner_distance:
                i.winner = "True"


print("Welcome to the Grand Demolition Derby!")
print("Let's begin the 8000km race!")

race = Race("Grand Demolition Derby", 8000)

hour = 0
while not race.race_finish():
    for i in range(10):
        race.hour_pass()
    hour += 1
    print(f"Result after {hour} hours")
    race.print_status()

print(f"We found the winner after {hour} hours! Well done")
race.winner()
race.print_status()










