# Author: Sara Jane Kenny, Student Num: R00255434 - complete 4 questions in 2 hours
# Purpose: A program that reads, prints and calculates the total of skip orders from a .txt file

# Setting global variable
order_amt = 0

print(f"{'Month':<10} Skip Orders"
      f"\n--------------------")
connection = open("skip.txt", "r")  # default access mode is r

for line in connection:
    line = line.rstrip()  # removes any space newline, tabs etc
    line = line.split(",")  # splits up the string based on commas
    month = line[0]
    skip_orders = int(line[1])

    order_amt += skip_orders
    order_avg = order_amt / 4

    print(f"{month:<11}{skip_orders}")

connection.close()

print(f"\nTotal number of orders for 4 months is {order_amt}. The average per month is {order_avg}.")
