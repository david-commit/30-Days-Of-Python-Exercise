# Exercise: Level 1
def addition(x, y): return x + y
def subtraction(x, y): return y + x
def multiplication(x, y): return x * y
def modulus(x, y): return y % x
def division(x, y): return y / x
def exponential(x, y): return y ** x
def floor_division(x, y): return y // x
    
print(addition(3, 4))
print(subtraction(3, 4))
print(multiplication(3, 4))
print(modulus(3, 4))
print(division(3, 4))
print(exponential(3, 4))
print(floor_division(3, 4))

print('I am enjoying 30 days of python')

print(type(10))  # Int
print(type(9.8))  #Float
print(type(4 - 4j))  # Float
print(type(['Asabeneh', 'Python', 'Finland']))  # List
print(type('I am enjoying 30 days of python'))  # String
print(type(True))  # Boolean
print(type((9, 3, 7)))  # Tuple
print(type({1, 2, 3}))  # Set
print(type({'name': 'Python'}))  # Dictionary

# Exercise: Level 3 (ChatGPT)
import math

# Define the two points
point1 = (2, 3)
point2 = (10, 8)

# Calculate the Euclidean distance using the formula
distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Print the distance
print("The Euclidean distance between", point1, "and", point2, "is", distance)

