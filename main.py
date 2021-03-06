import threading
import socket
import time
import Communicator as cm
import object_detection
import multiprocessing
from sys import platform
multiprocessing.allow_connection_pickling()


class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        self.wait = 5

        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))

    def __del__(self):
        print("connexion perdue")
        print("del called")

    def run(self):
        serial = None
        mode = 0
        obj_det = None
        while True:
            response = self.clientsocket.recv(255)
            if len(response) != 0:
                response = response.decode().replace("\r", "")
                response = response.replace("\n", "")
                if "$" == response:
                    if(mode == 1):
                        serial.write_msg("$")
                        msg = serial.read_msg()
                        value = msg.split("B")
                        if(len(value) == 0):
                            self.clientsocket.sendall(
                                ("B" + value[0]).encode())
                        else:
                            self.clientsocket.sendall(("B" + value[1]).encode())
                        # self.clientsocket.sendall("B-100:29E-103:29C-086:29R+047:29T+090:90\r\n".encode())
                elif "setmode 1" == response:
                    mode = 1
                    if(obj_det != None):
                        obj_det.terminate()
                        obj_det.join()
                        obj_det = None
                    if(serial == None):
                        serial = cm.serial_interface()
                    print("%s:%s changed mode to 1  " % (self.ip, self.port,))
                    self.clientsocket.sendall(b'changed mode to 1\r\n')
                    pass
                elif "setmode 2" == response:
                    serial = None
                    mode = 2
                    print("%s:%s  changed mode to 2 " % (self.ip, self.port, ))
                    obj_det = multiprocessing.Process(
                        target=object_detection.launch_detector, args=(self.clientsocket,))
                    obj_det.start()
                    self.clientsocket.sendall(b'changed mode to 2\r\n')

                else:
                    if(mode == 1):
                        serial.write_msg(response)
                    print("%s:%s sent: %s " % (self.ip, self.port, response,))
            else:
                if self.wait == 0:
                    self.__del__()
                    break
                print("reconnexion N {} dans une seconde : ".format((self.wait-1)))
                time.sleep(1)
                self.wait = self.wait-1


if __name__ == '__main__':
    tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpsock.bind(("", 8888))
    if(platform == "win32"):
        print("os det??ct?? : windows")
    elif(platform == "linux"):
        print("os det??ct?? : linux")
    else:
        print("os det??ct?? inconnu ou non-support??")
        exit(0)

    while True:
        tcpsock.listen(0)
        print("En ??coute...")
        (clientsocket, (ip, port)) = tcpsock.accept()
        newthread = ClientThread(ip, port, clientsocket)
        newthread.start()
