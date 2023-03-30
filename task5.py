# Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables.
# Return the largest of the three. 
# Do this without using the the inbuilt max () function!

number_1 = int(input("Enter the first input: "))
number_2 = int(input("Enter the second input: "))
number_3 = int(input("Enter the third input: "))

if (number_1 > number_2) and (number_1 > number_3):
    print("The largest number is: " + str(number_1))
elif (number_2 > number_1) and (number_2 > number_3):
    print("The largest number is: " + str(number_2))
elif (number_3 > number_1) and (number_3 > number_2):
    print("The largest number is: " + str(number_3))
else:
    print("The Three Numbers are Equal!")

