import board
import busio
import adafruit_si7021 as si
import time
from datetime import datetime
import csv

# Initializes I2C
i2c = busio.I2C(board.SCL, board.SDA) # Identifies the GPIO pins

# Initializes sensor
sensor = si.SI7021(i2c)

# Open CSV file
with open("atmospheric_data.csv", "a", newline="") as file:

    # Initialize CSV writer
    writer = csv.writer(file)

    # Sets header
    if file.tell() == 0:
        writer.writerow(["timestamp", "temperature_c", "humidity_percent"])

    # Display temp and humid values every two seconds
    while True:
        temp = sensor.temperature	                         # Holds value for temperature
        humid = sensor.relative_humidity                         # Holds value for humidity
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Holds value for time
        print(timestamp)
        print(f"Temperature: {temp:.2f} C")
        print(f"Humidity: {humid:.2f} %")
        writer.writerow([timestamp, temp, humid])                # Writes new data to CSV file
        file.flush()                                             # Flushes buffered data
        time.sleep(2)
