import board
import busio
import adafruit_si7021 as si

# Initializes I2C
i2c = busio.I2C(board.SCL, board.SDA) # Identifies the GPIO pins

# Initializes sensor
sensor = si.SI7021(i2c)

# Holding values for temperature and humidity
temp = sensor.temperature
humid = sensor.relative_humidity

# Display temp and humid values
print(f"Temperature: {temp:.2f} C")
print(f"Humidity: {humid:.2f} %")
