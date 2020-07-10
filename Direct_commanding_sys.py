import serial
rs232 = serial.Serial(
    port="COM5",
    timeout=1,
    baudrate=4800,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS)
print("Serial Created")


while True:
    x = input(">>")
    rs232.write((x+"\r\n").encode())
    msg = rs232.readall().decode()

    value =  msg.split("B")
    if(x=="$"):
        print(value[1])

