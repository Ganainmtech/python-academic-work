import datetime

# Importing the realtime date for the invoice
todays_date = datetime.datetime.today().strftime('%d-%m-%y')

# Basic price per barrel
butchers_barrel_price = 125.50
farriers_barrel_price = 105.90
gatehouse_barrel_price = 132.35

# Get the clients name, address and phone number
client_company = input("Enter your company name: ")
client_addr_one = input("Enter your company address line one: ")
client_addr_two = input("Enter your company address line two: ")
client_addr_three = input("Enter your company address line three: ")
client_phone_num = input("Enter your phone number: ")

# Get the clients order amounts
butchers_order_amount = int(input("\nEnter Butchers' Pale Ale barrel order amount: "))
farriers_order_amount = int(input("Enter Farriers' Ale barrel order amount: "))
gatehouse_order_amount = int(input("Enter Gatehouse Brown Ale barrel order amount: "))

# Get the first two numbers excluding the zero for the phone number
first_2_phone_num = client_phone_num.replace('0', '')

# Get the final two digits of the phone number
final_2_phone_num = client_phone_num[-2:]

# Get the last letter of clients company name
client_name_upper = client_company.upper()
client_second_last_char = client_name_upper[-2]

# Creating the invoice number
invoice_num = "WTA" + (first_2_phone_num[0:2]) + final_2_phone_num + client_second_last_char

# Calculating clients order price per alcohol order
butchers_order_price = butchers_order_amount * butchers_barrel_price
farriers_order_price = farriers_order_amount * farriers_barrel_price
gatehouse_order_price = gatehouse_order_amount * gatehouse_barrel_price
subtotal_order_price = butchers_order_price + farriers_order_price + gatehouse_order_price

# Calculating the surcharge
num_of_barrels = butchers_order_amount + farriers_order_amount + gatehouse_order_amount
rack_spaces = 15 - (num_of_barrels % 15)
surcharge_cost = 0

if rack_spaces < 15:
    surcharge_cost = rack_spaces * 2

# Calculating the Butchers' Pale Ale discount price
butchers_discount_num = int(butchers_order_amount / 10)
butchers_discount_price = butchers_discount_num * 10

# Calculating the Farriers IPA discount price
farriers_discount_num = int(farriers_order_amount / 12)
farriers_discount_price = farriers_discount_num * 8.40

# Calculating the Farriers discount price
gatehouse_discount_num = int(gatehouse_order_amount / 9)
gatehouse_discount_price = gatehouse_discount_num * 11.65

# Calculating the total amount due and displaying it onto the invoice
total_discount_price = butchers_discount_price + farriers_discount_price + gatehouse_discount_price
total_order_price = subtotal_order_price + surcharge_cost - total_discount_price

# Display the top of the Invoice in proper formatting
print('{:>50}'.format("Walled Town Ale"))
print('{:>65}'.format("Invoice No:"), '{:>10}'.format(invoice_num))
print('{:>59}'.format("Date:"), '{:>16}'.format(todays_date))

print('{:20}'.format("\nCompany Name:"), '{:}'.format(client_company))
print('{:19}'.format("Address:"), '{:}'.format(client_addr_one))
print('{:19}'.format(""), '{:}'.format(client_addr_two))
print('{:19}'.format(""), '{:}'.format(client_addr_three))

# Display the Sales Details in proper formatting
print("\n"'{:}'.format("Sales Details:"))
print(f"{'Butchers Pale Ale:':<30}{butchers_order_amount:>10}{'€':>20}{butchers_order_price:>12,.2f}")
print(f"{'Farriers IPA:':<30}{farriers_order_amount:>10}{'€':>20}{farriers_order_price:>12,.2f}")
print(f"{'Gatehouse Brown Ale:':<30}{gatehouse_order_amount:>10}{'€':>20}{gatehouse_order_price:>12,.2f}")
print("\n", '{:>73}'.format("\u2500" * 15))
print(f"{'Subtotal:':>55}{'€':>5}{subtotal_order_price:>12,.2f}")

# Displaying the surcharge if its needed
if rack_spaces < 15:
    print("\nSurcharge:")
    print(f"{'Rack spaces unused:':<30}{rack_spaces:>10}{'€':>20}{surcharge_cost:>12,.2f}")

# Displaying the barrels discounts if its needed
if butchers_discount_price or farriers_discount_price or gatehouse_discount_price > 0:
    print("\n"'{:25}'.format("Discount:"))

if butchers_discount_price > 0:
    print(f"{'Butchers Ale Pale:':<30}{butchers_discount_num:>10}{'€':>20}{butchers_discount_price:>12,.2f}")

if farriers_discount_price > 0:
    print(f"{'Farriers IPA:':<30}{farriers_discount_num :>10}{'€':>20}{farriers_discount_price:>12,.2f}")

if gatehouse_discount_price > 0:
    print(f"{'Gatehouse Brown Ale:':<30}{gatehouse_discount_num:>10}{'€':>20}{gatehouse_discount_price:>12,.2f}")

# Printing out the final total order price
print("\n"'{:>74}'.format("\u2500" * 15))
print("\n"f"{'Total:':>55}{'€':>5}{total_order_price:>12,.2f}")