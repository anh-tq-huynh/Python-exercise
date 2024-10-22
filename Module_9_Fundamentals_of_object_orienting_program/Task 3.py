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

    def drive(self, time : int):
        self.travelled_distance = self.travelled_distance + time * self.current_speed
        return self.travelled_distance

    def __str__(self):
        return (f"Registration number: {self.registration_num}\n"
                f"Maximum speed: {self.max_speed} km/h \n"
                f"Current speed: {self.current_speed} km/h \n"
                f"Travelled distance: {self.travelled_distance} km")

car = Car ("ABC-123", 142)
#Accelerate +30, +70 then +50 km/h
car.accelerate(30)
time_drive = 2.5
print(f"After this speed change, you are going at {car.current_speed} km/h\n"
      f"After, {time_drive} hour(s), you have travelled for {car.drive(time_drive)} km\n")

car.accelerate(70)
time_drive = 3.5
print(f"After this speed change, you are going at {car.current_speed} km/h\n"
      f"After, {time_drive} hour(s), you have travelled for {car.drive(time_drive)} km\n")

car.accelerate(50)
time_drive = 1.5
print(f"After this speed change, you are going at {car.current_speed} km/h\n"
      f"After, {time_drive} hour(s), you have travelled for {car.drive(time_drive)} km\n")

car.accelerate(-200)
print(f"After this speed change, you are going at {car.current_speed} km/h\n"
      f"You have travelled for a total of {car.drive(time_drive)} km\n")



