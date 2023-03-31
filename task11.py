# Write a program that takes the date of birth of a person and the program outputs the age in terms of years,months,days TODAY.
import datetime

# Prompt the user to enter their date of birth in YYYY-MM-DD format
dob_str = input("Enter your date of birth (YYYY-MM-DD): ")

# Convert the input string to a date object
dob = datetime.datetime.strptime(dob_str, "%Y-%m-%d").date()
print(dob)

# Calculate the age in years, months, and days
today = datetime.date.today()
age_years = today.year - dob.year
age_months = today.month - dob.month
age_days = today.day - dob.day

# Adjust the age for negative months or days
if age_months < 0 or (age_months == 0 and age_days < 0):
    age_years -= 1
    age_months += 12
    if age_days < 0:
        # Calculate the number of days in the previous month
        month_days = (today.replace(day=1) - datetime.timedelta(days=1)).day
        age_days += month_days

# Print the age in years, months, and days
print("You are {} years, {} months, and {} days old.".format(age_years, age_months, age_days))

