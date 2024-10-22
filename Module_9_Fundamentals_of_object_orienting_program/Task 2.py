class Car():
    def __init__(self, registration_num : str, max_speed : float):
        self.registration_num = registration_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self,speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def __str__(self):
        return (f"Registration number: {self.registration_num}\n"
                f"Maximum speed: {self.max_speed} km/h \n"
                f"Current speed: {self.current_speed} km/h \n"
                f"Travelled distance: {self.travelled_distance} km")

car = Car ("ABC-123", 142)

#Accelerate +30, +70 then +50 km/h
print("Let's start a race with lightning speed, we increase the speed by 30,70 and finally 50 km/h")
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(f"Now, the speed is: {car.current_speed}\n")

#Emergency brake -200km/h
car.accelerate(-200)
print(f"Oh no, danger! Emergency brake")
print(f"Finally, the speed is: {car.current_speed}")


