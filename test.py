#import object_detection
#list = object_detection.launch_detector()
#print(list)

from Communicator import serial_interface
"""
#first test is working
serial = serial_interface()

serial.write_msg(b"$")

print(serial.read_msg().decode())"""
""" 
#second test
Creating Shell
"""
serial = serial_interface()
while True:
    inpt = input("exit pour quitter\nentrez votre commande : ")
    if inpt == "exit":
        break
    elif inpt == "$":
        serial.write_msg(b"$")
        print(serial.read_msg().decode())
    else:
        serial.write_msg(inpt.encode())
        
