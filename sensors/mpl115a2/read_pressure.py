import board
import busio
import adafruit_mpl115a2 as mpl

# Initializes I2C
i2c = busio.I2C(board.SCL, board.SDA) # Identifies the GPIO pins

# Initializes sensor
sensor = mpl.MPL115A2(i2c)

# Retrieve atmospheric pressure and temperature
temp = sensor.temperature
pres = sensor.pressure

# Display temp and pres values
print(f"Temperature: {temp:.2f} C")
print(f"Pressure: {pres:.2f} hPa")
