import Robot

rb = Robot.robot()
drop_points = rb.drop_points

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
            rb.goToDropPoint(eachObject['name'])
        else:
            print("cannot sort " + eachObject['name'])

