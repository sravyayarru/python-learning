# Write a program to calculate the average of three numbers.
num1 = float(input("enter first number"))
num2 = float(input("enter second number"))
avg = (num1 + num2) / 2
print('the average of numbers=%0.2f' % avg)

# Write a program to calculate the square root of a number.
import math

num = int(input("enter number:"))
sqRoot = math.sqrt(num)
print(f"the square root of {num} is", sqRoot)


# Write a program that calculates the number of seconds in a day.
def seconds_per_day(day):
    hours = day * 24
    minutes = hours * 60
    seconds = minutes * 60
    return seconds


print(seconds_per_day(1))


# Write a program the number of seconds and prints out how many minutes and seconds that isFor instance, 200 seconds
# is 3 minutes and 20 seconds.
totalSecs = int(input("enter seconds:"))
mins = totalSecs // 60
secs = totalSecs % 60
print(mins, "minutes and", secs, "seconds")


# Write a program to enter power. Then find the last digit of 2 raised to that power.
num = int(input("Enter a power Number: "))
res = str(2 ** num)
print(f"exponential of 2 is : {res}")
last_digit = len(res) - 1
print(f"last digit of 2 power {num} : {int(res[last_digit])}")


# Write a program to calculate the area of a circle.

from math import pi

r = float(input("input the radius of the circle:"))
print("the area of the circle with radius " + str(r) + " is:" + str(pi * r ** 2))

#

str_name = "Baby shark do doo, baby shark do dooo"
print(str_name.capitalize())
print(str_name.count('o'))
print(str_name.index('o'))
print(str_name.endswith('oo'))
print(str_name.find('shark'))
print(str_name.isalpha())
print(str_name.isalnum())
print(str_name.isdigit())
print(str_name.islower())
print(str_name.isspace())
print(str_name.replace("shark", "whale"))

# get India from below string
str_name = "IndiaUSSweden"
print(str_name[0:5])

# get US from below string
str_name = "India US Sweden"
print(str_name.split()[1])

#  get sweden from the below string
str_name = "India-US-Sweden"
print(str_name[9:15])


# check if hello is equal to Gello programmatically
a = "hello"
b = "gello"
if (a == b):
    print('a and b are equal')
else:
    print('a and b are not equal')


# get me the result of following string slicing operations
str_item = "Hello , Python is fun to learn"
print(str_item[1:])
print(str_item[:3])
print(str_item[1:200])
print(str_item[-1])
print(str_item[:-3])
print(str_item[-3:])

# execute the below programs and let me know the result
print(int(True))
print(int(False))
print(bool(1))
print(bool(-42))
print(bool(0))

# write a program to calulate are of circle mathematical formula is pi*r*square

from math import pi


def area_of_circle(r):
    pi = 3.1415926536
    area = pi * (r ** 2)
    return area


radius = float(input("enter radius:"))
print("area:", area_of_circle(radius))


# c = 3.14 + 2.73j
# write a program to get real,imaginary and conjugate(A + Bj is A - Bj) of above complex number

cn = complex(3.14 + 2.73j)
print("complex number", cn)
print("complex number-real part:", cn.real)
print("complex number-imaginary part", cn.imag)
print("complex number-conjugate part", cn.conjugate())
