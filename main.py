# Description:
# This program takes an input number from the user and categorizes it into different groups based on its value and sign.
# It then prints out a message indicating the category of the input number.

# Prompt the user to enter a number
num = float(input("Enter a number: "))

# Check if the number is negative
if num < 0:
    is_negative = True
else:
    is_negative = False

# Check the category of the number based on its value and sign
# Block 1
if num < 0 and num < -100:
    print("Number is a large negative number")

# Block 2
if num > 100 and not is_negative:
    print("Number is a large positive number")

# Block 3
if 50 <= num <= 100 and is_negative:
    print("Number is a medium negative number")

# Block 4
if 50 <= num <= 100 and not is_negative:
    print("Number is a medium positive number")

# Block 5
if 0 <= num <= 50 and is_negative:
    print("Number is a small negative number")

elif 0 <= num <= 50 and not is_negative:
    print("Number is a small positive number")

elif num == 0:
    print("Number is zero")
