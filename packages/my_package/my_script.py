# The standard way to import NumPy:
import numpy as np

#number1 = 5
#number2 = 6

#result = np.add(number1, number2)

#message = "\nHello World!\n"

#print(message)
#print("Sum total", result)

import os

vehicle_name = os.environ['VEHICLE_NAME']
message = f"\nHello from {vehicle_name}!\n"
print(message)
