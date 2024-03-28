import serial
import requests
import time

# Set the COM port according to your Arduino connection
arduino_port = 'COM3'  # Change this to your Arduino port

# ThingSpeak API Key and URL
api_key = 'YA8V02RS615W3KVT'
thingspeak_url = f'https://api.thingspeak.com/update?api_key={api_key}'

# Open serial connection to Arduino
ser = serial.Serial(arduino_port, 9600)

try:
    while True:
        # Read data from Arduino
        arduino_data = ser.readline().decode().strip()

        # Send data to ThingSpeak
        if arduino_data:
            try:
                requests.get(f'{thingspeak_url}&field1={arduino_data}')
                print(f'Data sent to ThingSpeak: {arduino_data}')
            except requests.RequestException as e:
                print(f'Error sending data to ThingSpeak: {e}')

        # Wait for a while before reading again
        time.sleep(15)

except KeyboardInterrupt:
    # Close the serial connection on Ctrl+C
    ser.close()
    print('Serial connection closed.')