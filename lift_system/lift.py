import time


class Lift:
    def __init__(self, current_floor=0):
        self._current_floor = current_floor
        self.time_to_come = 0
        self.is_travelling = False
        self.counter = 0

    @staticmethod
    def is_floor_valid(floor):
        return isinstance(int(floor), int) and int(floor) in range(0, 6)

    @property
    def current_floor(self):
        return self._current_floor

    @current_floor.setter
    def current_floor(self, value):
        if self.is_floor_valid(value):
            self._current_floor = value

    def go_to_floor(self, floor_to_go):
        self.is_travelling = True
        self.time_to_come = 0
        step = 1
        if self.current_floor > floor_to_go:
            step = -1
        for floor in range(self.current_floor, floor_to_go, step):
            self.time_to_come += 1
        print(f"Going to floor {floor_to_go} takes {self.time_to_come} seconds.")
        self.current_floor = floor_to_go
        self.counter += 1
        self.is_travelling = False

    def call_lift(self):
        while self.counter <= 20:
            floor_to_go = None
            floor = input("Enter the floor you want to go: ")
            while not self.is_floor_valid(floor):
                print("The building has floors 0 to 5, please enter a valid floor.")
                floor = input("Enter the floor you want to go: ")
            floor_to_go = int(floor)
            self.go_to_floor(floor_to_go)
            time.sleep(self.time_to_come)
            if self.is_travelling:
                time.sleep(self.time_to_come)
            else:
                self.go_to_floor(0)
                time.sleep(self.time_to_come)

        print("The building is closed, please come back tomorrow.")



