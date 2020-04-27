import serial
from sys import platform
init_times = 5

port_path = None
if platform == "win32":
    port_path = "COM7"
elif platform == "linux":
    port_path = "/dev/ttyUSB0"
else:
    print("os detécté inconnu ou non-supporté")
    exit(0)


class serial_interface:
    pass
    # Initializer / Instance Attributes

    def __init__(self):
        self.rs232 = serial.Serial(
            port=port_path,
            timeout=1,
            baudrate=4800,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS)
        print("Serial Created")

    def __del__(self):
        self.rs232.close()
        print('Serial closed')

    def write_msg(self, message):
        self.rs232.write((message+"\r\n").encode())

    def read_msg(self):
        return (self.rs232.readline()).decode()

    def clearBuffer(self):
        self.rs232.reset_input_buffer()
