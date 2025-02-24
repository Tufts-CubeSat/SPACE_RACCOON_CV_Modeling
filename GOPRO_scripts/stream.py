import socket
import cv2
import numpy as np


UDP_IP = "172.23.168.51"
UDP_PORT = 8556

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
s = ""
while True:
    for i in range(20):
        data,addr = sock.recvfrom(46080)
        s = s + data
    #data, addr = sock.recvfrom(46080)
    #s = s+data
    frame = np.fromstring(s, dtype='uint8')
    frame = frame.reshape(480, 640, 3)
    #cv2.imwrite('frame.png',frame)
    cv2.imshow('server', frame)
    s=""
    '''
    if len(data) == 921600:
        frame = np.fromstring(s, dtype='uint8')
        frame = frame.reshape(480, 640, 3)
        cv2.imshow('frame', frame)
        s = ""
    '''
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break