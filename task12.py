# Write a program that prints the largest of 4 inputs taken in from a user. 
# Assume that the user would not enter any two numbers which are the same.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))

numbers = [num1, num2, num3, num4]

numbers.sort()

print("The largest number is: " + str(numbers[-1]))