import board
import busio
import adafruit_si7021 as si
import adafruit_mpl115a2 as mpl
import time
from datetime import datetime
import csv

# Initializes I2C
i2c = busio.I2C(board.SCL, board.SDA) # Identifies the GPIO pins

# Initializing sensors
humidity_sensor = si.SI7021(i2c)
pressure_sensor = mpl.MPL115A2(i2c)

# Open CSV file
with open("combined_atmospheric_data.csv", "a", newline="") as file:

    # Initialize CSV writer
    writer = csv.writer(file)

    # Sets header
    if file.tell() == 0:
        writer.writerow(["timestamp", "temperature_si_c", "humidity_percent", "pressure_hpa", "temperature_mpl_c"])

    # Display both temperature, humidity and pressure values every two seconds
    while True:
        temp_si = humidity_sensor.temperature	                 # Holds value for temperature (SI7021)
        humid = humidity_sensor.relative_humidity                # Holds value for humidity
        pres = pressure_sensor.pressure                          # Holds value for pressure 
        temp_mpl = pressure_sensor.temperature                   # Holds value for temperature (MPL115A2)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Holds value for time
        print(timestamp)
        print(f"Temperature (SI7021): {temp_si:.2f} C")
        print(f"Humidity: {humid:.2f} %")
        print(f"Pressure: {pres:.2f} hPa")
        print(f"Temperature (MPL115A2): {temp_mpl:.2f} C")
        writer.writerow([timestamp, temp_si, humid, pres, temp_mpl]) # Writes new data to CSV file
        file.flush()                                                 # Flushes buffered data
        time.sleep(2)
