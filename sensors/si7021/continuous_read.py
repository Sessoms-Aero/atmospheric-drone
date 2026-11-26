import board
import busio
import adafruit_si7021 as si
import time

# Initializes I2C
i2c = busio.I2C(board.SCL, board.SDA) # Identifies the GPIO pins

# Initializes sensor
sensor = si.SI7021(i2c)

# Display temp and humid values every two seconds
while True:
    temp = sensor.temperature	     # Holds value for temperature
    humid = sensor.relative_humidity # Holds value for humidity
    print(f"Temperature: {temp:.2f} C")
    print(f"Humidity: {humid:.2f} %")
    time.sleep(2)
