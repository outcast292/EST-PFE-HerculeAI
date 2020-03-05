#import object_detection
#list = object_detection.launch_detector()
#print(list)

import Robot
"""
#first test is working
serial = serial_interface()

serial.write_msg(b"$")

print(serial.read_msg().decode())"""
""" 
#second test
Creating Shell
"""
rb = Robot.robot()
while True:
    inpt = input("exit pour quitter\nentrez votre commande : ")
    if inpt == "exit":
        break
    elif inpt == "$":
        rb.controller.write_msg("$")
        print(rb.controller.read_msg())
    else:
        rb.goToDropPoint(inpt)
        
