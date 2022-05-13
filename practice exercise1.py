# Write a 'while' loop that prints integers from zero to 5.
i = 0
while i <= 5:
    print(i)
    i = i + 1

# Write a 'while' loop that starts at the last character in the string and works its way backwards to the first
# character in the string, printing each letter on a separate line, except backwards.

fruit = 'banana'
index = len(fruit) - 1
while index >= 0:
    letter = fruit[index]
    print(letter)
    index -= 1

# Write a program that asks the user to enter a number and prints out all the divisors of that number.
num = int(input("Please enter number"))
list_divisors = []

for i in range(1, num):
    if num % i == 0:
        list_divisors.append(i)
print(list_divisors)

# Write a program to calculate factorial of any given number.
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print(" Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)


# Write a program to find the greatest common divisor (GCD) or highest common factor (HCF) of given two numbers.

x = int(input("enter first number:"))
y = int(input("enter second number:"))
if x > y:
    smaller = y
else:
    smaller = x
for i in range(1, smaller + 1):
    if ((x % i == 0) and (y % i == 0)):
        hcf = i
print("the H.C.F of", x, "and", y, "is", hcf)


# Write a program to print whether the given number is a palindrome or not.
num = int(input("Enter a number:"))
temp = num
rev = 0
while (num > 0):
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
if (temp == rev):
    print("yes,a palindrome number")
else:
    print("Not a palindrome number")


# Write a program that uses list and range to create the list [3,6, 9, . . . , 99] .
my_list = [*range(3, 100, 3)]
print(my_list)

# Write a program to convert a list of characters into a single string.
s = ['a', 'b', 'c', 'd']
str1 = ''.join(s)
print(str1)

# Write a program to read a string from the user and print the list of characters in the string.
str = 'abcd'
print("actual string:", str)
print("converted to list:\n", list(str))

# Write a Python program to find common items from two lists.
color1 = ["Red", "Green", "Orange", "White"]
color2 = ["Black", "Green", "White", "Pink"]
color = []
for i in color1:
    if i in color2:
        color.append(i)
print("the common elements are:", color)

# Write a Python program to get the difference between the two lists.
list1 = [1, 2, 3, 4]
list2 = [1, 2]
print(list(set(list1) - set(list2)))

# write a Python program to get the largest number from a list.
list1 = [1, 2, -8, 0]
list1.sort()
print(list1)
print("the largest element is:", list1[-1])

# Write a Python program to find the second-smallest number in a list.
li = []
n = int(input("Enter the number of elements: "))
for i in range(1, n + 1):
    elem = int(input("Enter the elements: "))
    li.append(elem)
li.sort()

print("The sorted list: ", li)
print("The second smallest value of this list: ", li[1])

# Write a Python program to remove duplicates from a list.
my_list = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
print("List Before ", my_list)
temp_list = []

for i in my_list:
    if i not in temp_list:
        temp_list.append(i)

my_list = temp_list

print("List After removing duplicates ", my_list)

# # Write a Python program to sum all the items in a list.
list1 = [1, 2, -8]
total = sum(list1)
print("sum of all elements in given list:", total)


# Write a Python program to multiply all the items in a list.
list = [1, 2, 3, 4]
result = 1
for x in list:
    result = result * x
print(result)
