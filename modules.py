print('Example of python modules importing')
# import math
from math import sqrt

# square_root = math.sqrt(25)
square_root = sqrt(25)
print(f'Square root = {square_root}')

print('\nExample of personalized modules')
import my_module
from my_module import hello, double

# message = my_module.hello('Arthur')
message = hello('Arthur')
# result_double = my_module.double(5)
result_double = double(5)

print(message)
print(f'The double of 5 is {result_double}')

# It is a good practice to import only the functions you need