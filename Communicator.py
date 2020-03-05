import serial
init_times = 5

class serial_interface:
    pass
    # Initializer / Instance Attributes
    def __init__(self):
        self.rs232 = serial.Serial(
        port='COM4',
        timeout=1,
        baudrate=4800,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS)
        print("Serial Created")
    def __del__(self): 
        self.rs232.close()
        print('Serial closed') 
    def write_msg(self,message):
        self.rs232.write((message+"\r\n").encode())
    def read_msg(self):
        return (self.rs232.readline()).decode()
    def clearBuffer(self):
        self.rs232.reset_input_buffer()

    