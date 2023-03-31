# Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123” , 
# if so then print  “Login is Successful” and if not print “Invalid username or password”. 
# ONLY accept 3 tries after which it notifies you that you have been blocked.

# Initialize the number of attempts to 0
num_attempts = 0

# Allow the user to try logging in three times
while num_attempts < 3:
    # Prompt the user to enter their email and password
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Check if the email and password match the given credentials
    if email == "admin@mail.com" and password == "Admin@123":
        print("Login is successful!")
        break  # Exit the loop if login is successful
    else:
        num_attempts += 1  # Increment the number of attempts
        print("Invalid email or password. Please try again.")

# Notify the user if they have been blocked
if num_attempts == 3:
    print("You have been blocked.")
