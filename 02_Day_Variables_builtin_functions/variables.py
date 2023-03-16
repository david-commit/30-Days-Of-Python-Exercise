# Day 2: 30 Days of python programming
first_name = 'David'
age = 10
is_married = False
os, os_type, os_build = 'Windows', 'Windows 11', '22H2' 

print(type({'name', 'age'}))
print(len('name'))

num_one, num_two = 5, 4
print('Add', num_one + num_two)
print('subtract', num_one - num_two)
print('Multiply', num_one * num_two)
print('Divide', num_one / num_two)
print('Modulus', num_one % num_two)
print('Power', num_one ** num_two)
print('Floor division', num_one // num_two)

# AREA OF A CIRCLE = π × r2
import math
radius = 30
area_of_circle = math.pi * (radius ** 2)
print('area_of_circle:', area_of_circle)

# Circumference of a circle = 2πr
circum_of_circle = 2 * math.pi * radius
print('circum_of_circle:', circum_of_circle )

# Custom Input radius
custom_radius = input('Enter radius:\n')
custom_area_of_circle = math.pi * (float(custom_radius) ** 2)
print('custom_area_of_circle:', custom_area_of_circle)