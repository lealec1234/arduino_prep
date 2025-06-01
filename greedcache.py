import serial
import time
import cv2
import numpy as np
import mss
import sys




def attackuptp():
    ser.write(b'attackuptp\n')
    time.sleep(0.1)

def attackteleleft():
    ser.write(b'attackteleleft\n')
    time.sleep(0.1)

def attackteleright():
    ser.write(b'attackteleright\n')
    time.sleep(0.1)

def attackdowntp():
    ser.write(b'attackdowntp\n')
    time.sleep(0.1)
def safe_open_serial(port, baudrate=9600, timeout=1):
    try:
        ser = serial.Serial(port, baudrate, timeout=timeout)
        time.sleep(2)  # Let Arduino reset
        print(f"[✓] Opened {port}")
        return ser
    except serial.SerialException as e:
        print(f"[ERROR] Could not open port {port}: {e}")
        sys.exit(1)

#python "C:/Users/Alec/Desktop/Maplestoryscript/greedcache.py"

ser = None

try:
    ser = safe_open_serial('COM14')
    time.sleep(2)

    ser.write(b'start\n')
    print("Bot started.")

    # Wait until Arduino says "ready"
    while True:
        try:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                print(f"Arduino says: {line}")
        except serial.SerialException as e:
            print(f"[ERROR] Could not open port: {e}")
            sys.exit(1)

    ser.write(b'stop\n')
    print("Bot stopped.")

except KeyboardInterrupt:
    print("\n[!] Ctrl+C detected. Exiting safely...")
    ser.write(b'stop\n')
    #safe_close_serial(ser)
    #hard_reset_arduino('COM8')
    print("[✓] Sent stop command to Arduino.")
finally:
    ser.write(b'stop\n')
    #safe_close_serial(ser)
    #hard_reset_arduino('COM8')









