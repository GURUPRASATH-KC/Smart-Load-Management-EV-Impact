import serial
import time

arduino_port = 'COM3'
baud = 9600
ser = serial.Serial(arduino_port, baud)
time.sleep(2)

try:
    while True:
        voltage = ser.readline().decode('utf-8').strip()
        print(f"Voltage Reading: {voltage} V")
        time.sleep(1)
except KeyboardInterrupt:
    ser.close()
