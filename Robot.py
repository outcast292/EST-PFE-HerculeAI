import Communicator as cm
import time


class robot:
    nextPickUpPoints = ["L", "B+289:30", "E-511:30",
                        "C+156:30", "R+007:30", "T-316:30"]
    standBy = ["L", "B+285:30", "E+035:30",
               "C-303:30", "R+1:30", "T-286:30"]  # standby
    pausePoints = ["L", "B+120:30", "E+035:30",
                   "C-303:30", "R+1:30", "T-286:30"]  # standby
    drop_points = {
        "banane": ["L", "B-004:30", "E-304:30", "C-097:30", "T-349:30", "R+007:30"],
        "apple":  ["L", "B-160:30", "C-160:30", "E-160:30", "T-160:30"],
        "orange": ["L", "B-160:30", "C-160:30", "E-160:30", "T-160:30"], "cell phone": ["L", "B-160:30", "C-160:30", "E-160:30", "T-160:30"]
    }

    zero_points = ["L", "B0:30", "C0:30", "E0:30", "T0:30"]

    def __init__(self):  # creates the serial interface and go to pickup Location
        self.controller = cm.serial_interface()
        self.goToPickUp()

    def __del__(self):
        self.goToPickUp()

    def goToZero(self):
        self.controller.write_msg("".join(self.zero_points))
        print("going to 0 location")
        time.sleep(3)

    def openHook(self):
        self.controller.write_msg("LP-160:30")
        print("opened hook")
        time.sleep(1)

    def closeHook(self):
        self.controller.write_msg("LP+160:30")
        print("closed hook")
        time.sleep(2)

    def goToPickUp(self):
        self.controller.write_msg("".join(self.standBy))
        print("going to pick location")
        time.sleep(1)
        self.openHook()

    def goToDropPoint(self, objectType):  # Exemple : goToDropPoint("Orange")
        self.closeHook()
        self.controller.write_msg("".join(self.standBy))
        time.sleep(2)
        self.controller.write_msg("".join(self.pausePoints))
        time.sleep(1)
        self.controller.write_msg("".join(self.drop_points.get(objectType)))
        time.sleep(2)
        print("went to drop points of " + objectType)
        self.openHook()

    def goToPoints(self):
        self.controller.write_msg("".join(self.nextPickUpPoints))
        time.sleep(2)
