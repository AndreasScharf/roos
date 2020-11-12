import os, time
import serial

orders = [
    'AT',
    'ATH',
    'ATE1',
    'AT+CSQ',
    'AT*MCGDEFCONT="IP","iot.1nce.net","",0,0'
]

# Enable Serial Communication
port = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=1)
#port.write(b'AT\r\n')
#port.write(b'AT+CGDCONT=1, "IP", "iot.1nce.net", "", 0, 0 \r\n')
for order in orders:
    port.write(order + ' \r\n')
    rcv = port.read(100)
    print(len(rcv))
    print(rcv)

#port.write('AT*MCGDEFCONT="IP","iot.1nce.net","",0,0 \r\n')
