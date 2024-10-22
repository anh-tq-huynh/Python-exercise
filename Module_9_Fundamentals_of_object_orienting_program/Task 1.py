class Car():
    def __init__(self, registration_num : str, max_speed : float):
        self.registration_num = registration_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def __str__(self):
        return (f"Registration number: {self.registration_num}\n"
                f"Maximum speed: {self.max_speed} km/h \n"
                f"Current speed: {self.current_speed} km/h \n"
                f"Travelled distance: {self.travelled_distance} km")

car = Car ("ABC-123", 142)
print(car)
