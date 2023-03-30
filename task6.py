# Put number 1 till 50 in a tuple then,  print the first half values in one line and the last half values in another line.

numbers = tuple(range(1, 51))

first_half = numbers[0:25]
second_half = numbers[25:]

print("First half: " + str(first_half))
print("Second half: " + str(second_half))