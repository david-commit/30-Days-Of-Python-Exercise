age = 17
height = 5.5
complex_number = (1 + 1j)
print(type((complex_number)))

# calculate an area of this triangle (area = 0.5 x b x h)
base = input('Enter base:')
height = input('Enter height:')
area = 0.5 * float(base) * float(height)
print('Area of triangle', area)

# perimeter of a rectangle (perimeter = 2 x (length + width))
length = input('Enter length:')
width = input('Enter width:')
perimeter = 2 * (float(length) + float(width))
print('Perimeter of rectangle', perimeter)

# Skipped analysis exercises

print(len('python') < len('dragon')) # False

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')
print('jargon' in 'I hope this course is not full of jargon.')
print('on' in 'python' and 'on' in 'dragon')

floor = 7 // 3
print(floor == 2.7) # False

print(type('10') == type(10)) # False

# # prompt the user to enter hours and rate per hour. Calculate pay of the person?
# hours = input('Hours worked:')
# rate = input('Pay rate per hour:')
# pay = int(hours) * float(rate)
# print('Pay is $', pay)

# prompt the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = input('Enter age:')
if int(years) > 100: 
    print('age must be less than 100')
else:
    lived = int(years) * 365 * 24 * 60 * 60
    print('You\'ve lived for', lived, 'seconds')