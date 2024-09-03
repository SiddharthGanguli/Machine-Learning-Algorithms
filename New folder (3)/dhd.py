import serial
import csv
import time

# Establish serial connection with Arduino
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with the port your Arduino is connected to
time.sleep(2)  # Allow some time for the serial connection to initialize

# Open CSV file for writing
with open('data.csv', 'w', newline='') as csvfile:
    fieldnames = ['value', 'label']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    start_time = time.time()
    current_time = start_time

    while True:
        # Read line from serial port
        line = ser.readline().decode().strip()
        
        # Split the line into value and label
        value, label, timestamp, duration = line.split('\t')

        # Write data to CSV file
        writer.writerow({'value': value, 'label': label})

        # Check if 10 seconds have elapsed
        current_time = time.time()
        if current_time - start_time >= 10:
            start_time = current_time
            csvfile.flush()  # Flush the buffer to ensure data is written immediately
