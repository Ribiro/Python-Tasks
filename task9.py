# Write a program called stars.py. 
# It should prompt the user for a number, and it should print the number of stars till the number entered.

number = int(input("Enter a number: "))

for i in range(1, number+1):
    print('*' * i)
