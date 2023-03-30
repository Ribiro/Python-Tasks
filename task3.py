# Write a program which gets a phone number from a form input or terminal. 
# Validates the phone number by checking if it starts with +254.. or 07.. or 71… or 254.. or 01... Convert the number to start with +254…  
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”

phone_number = input("Enter a phone number: ")

if phone_number[0:4] == "+254":
    print("Valid Phone Number!")
elif phone_number[0:3] == "254":
    valid_phone_number = "+" + phone_number[0:]
    print("Valid Phone Number: " + valid_phone_number)
elif phone_number[0] == "0":
    valid_phone_number = "+254" + phone_number[1:]
    print("Valid Phone Number: " + valid_phone_number)
elif phone_number[0] == "1" or phone_number[0] == "7":
    valid_phone_number = "+254" + phone_number[0:]
    print("Valid Phone Number: " + valid_phone_number)
else:
    print("Enter a valid phone number!")