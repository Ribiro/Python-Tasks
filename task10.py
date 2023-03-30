# Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.
# prods = [[‘omo’,’30kshs’,300], [‘milk’,’50kshs’,200],[‘bread’,’45kshs’,359], [‘coffee’,’5kshs’,’79’]]

prods = [['omo','30kshs',300], ['milk','50kshs',200],['bread','45kshs',359], ['coffee','5kshs','79']]

total_stock = 0

for i in prods:
    stock = int(str(i[2]))
    total_stock += stock

print("Total stock:", total_stock)
