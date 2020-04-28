import Robot
rb = None
drop_points = None
socket = None

def setup_handler(tsock):
    global rb
    global drop_points
    global socket
    socket= tsock
    rb = Robot.robot()
    drop_points = rb.drop_points
    socket.sendall(b"handler created \r\n")


def getKey(objectType):
    for key in drop_points.items():
        if key[0] == objectType:
            return key[0]
    return "key doesn't exist"


def sortObject(detected_objects):
    print("sorting")
    for eachObject in detected_objects:
        if eachObject['name'] == getKey(eachObject['name']):
            print("picking up " + eachObject['name'])
            socket.sendall(("picking up " + eachObject['name'] + "\r\n").encode())
            rb.goToPoints()
            # rb.goToPickUp()
            rb.goToDropPoint(eachObject['name'])
            rb.goToPickUp()
        else:
            print("cannot sort " + eachObject['name'])
            socket.sendall(('cannot sort ' + eachObject['name'] + "\r\n").encode())
