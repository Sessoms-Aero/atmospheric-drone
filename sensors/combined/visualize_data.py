import csv
import matplotlib.pyplot as plt
import datetime

# Opening CSV file in read mode
with open("combined_atmospheric_data.csv", "r") as file:
    reader = csv.DictReader(file) # Initializing a csv.DictReader

    for row in reader: # Iterates through each row
        print(row)     # Prints each row
