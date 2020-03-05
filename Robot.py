import Communicator as cm
import time


class robot:
    pick_up_points = ["L", "B-160:30", "C-160:30", "E-160:30", "T-160:30"]
    drop_points = {"Banana": ["L", "B-160:30", "C-160:30", "E-160:30", "T-160:30"], "Apple": ["L", "B-160:30","C-160:30", "E-160:30", "T-160:30"], "Orange": ["L", "B-160:30", "C-160:30", "E-160:30", "T-160:30"]}
    zero_points = ["L", "B0:30", "C0:30", "E0:30", "T0:30"]
    pass

    def __init__(self):  # creates the serial interface and go to pickup Location
        self.controller = cm.serial_interface()
        self.goToZero()

    def __del__(self):
        self.goToPickUp()

    def goToZero(self):
        self.controller.write_msg("".join(self.zero_points))

    def openHook(self):
        self.controller.write_msg("LP-160:30")

    def closeHook(self):
        self.controller.write_msg("LP+160:30")

    def goToPickUp(self):
        self.controller.write_msg("".join(self.pick_up_points))
        self.openHook()

    def goToDropPoint(self, objectType):  # Exemple : goToDropPoint("Orange")
        self.closeHook()
        self.controller.write_msg("".join(self.drop_points.get(objectType)))
        time.sleep(3)
        self.openHook()
