# Prompt the user for a number either on a form input or the terminal. 
# Depending on whether the number is even or odd, display  either “odd” or “even” to the user.

number = int(input('Enter a number: '))

if number % 2 == 0:
    print(str(number) + ' is an even number')
    if number % 4 == 0:
        print(str(number) + ' is also divisible by 4')
else:
    print(str(number) + ' is an odd number')