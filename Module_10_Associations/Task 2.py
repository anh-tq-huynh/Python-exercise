class Elevator:
    def __init__(self,top_floor: int,ele_id,bot_floor = 1):
        self.top_floor = top_floor
        self.all_floors = self.top_floor
        self.bot_floor = bot_floor
        self.ele_id = ele_id

    def floor_up(self):
        self.bot_floor += 1
        self.top_floor -= 1

    def floor_down(self):
        self.bot_floor -= 1
        self.top_floor += 1

class Building:
    def __init__(self,top_floor: int, total_ele: int, bot_floor = 1):
        self.top_floor = top_floor
        self.total_ele = total_ele
        self.bot_floor = bot_floor
        self.ele_list = []
        #create elevators
        for i in range(0, total_ele):
            self.ele_list.append(Elevator(top_floor, i + 1, bot_floor))

    def run_elevator(self, ele_num, desired_floor):
        selected_ele = self.ele_list[ele_num + 1]
        print(f"Elevator {ele_num} going to floor {desired_floor}")
        current_floor = selected_ele.top_floor
        while current_floor != desired_floor:
            if current_floor < desired_floor:
                selected_ele.floor_up()
            else:
                selected_ele.floor_down()
            current_floor = selected_ele.all_floors - selected_ele.top_floor + 1
            print(f"You're at {current_floor} floor")
        print(f"You've arrive the your desired floor: {desired_floor}")

build = Building(12,5)
print(f"The building has a total of {build.total_ele} elevators and {build.top_floor} floors")
build.run_elevator(2,7)