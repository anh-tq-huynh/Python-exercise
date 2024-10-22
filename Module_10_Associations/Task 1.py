class Elevator:
    def __init__(self,top_floor: int,bot_floor = 1):
        self.top_floor = top_floor
        self.all_floors = self.top_floor
        self.bot_floor = bot_floor

    def floor_up(self):
        self.bot_floor += 1
        self.top_floor -= 1

    def floor_down(self):
        self.bot_floor -= 1
        self.top_floor += 1

    def go_to_floor(self, desired_floor):
        current_floor = self.all_floors - self.top_floor +1
        while current_floor != desired_floor:
            if current_floor < desired_floor:
                self.floor_up()
                current_floor = self.all_floors - self.top_floor + 1
                print(f"You're at {current_floor} floor")
            else:
                self.floor_down()
                current_floor = self.all_floors - self.top_floor + 1
                print(f"You're at {current_floor} floor")
        print(f"You've arrive the your desired floor: {desired_floor}")

h = int(input("How many floors does your building have in total?"))
elevator_h = Elevator(h)

input_floor = input("You're at floor 1, which floor do you want to go to? ")
elevator_h.go_to_floor(int(input_floor))

print("\nGreat, let's go back to the ground floor!")
elevator_h.go_to_floor(1)