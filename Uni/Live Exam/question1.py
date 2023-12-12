# Author: Sara Jane Kenny, Student Num: R00255434 - 2 Hours for 4 questions
# Purpose: A program that allows users to book for a skip

# Setting const variables
LARGE_SKIP_PRICE = 280
MEDIUM_SKIP_PRICE = 200
SMALL_BAG_PRICE = 50

# Setting global variables
discount_text = ""
user_cost = 0

# Display text and gather user inputs
print(f"Skip Drop\tCompany"
      f"\n------------------")
first_name = input("What is your first name? ")
surname = input("What is your surname? ")
print(f"1. {'Large':<8}€{LARGE_SKIP_PRICE:>5}"
      f"\n2. {'Medium':<8}€{MEDIUM_SKIP_PRICE:>5}"
      f"\n3. {'Bags':<8}€{SMALL_BAG_PRICE:>5} (4 for 180)")
user_choice = int(input(f">>>"))

if user_choice == 1:
    user_choice = "Large"
    user_cost = LARGE_SKIP_PRICE
elif user_choice == 2:
    user_choice = "Medium"
    user_cost = MEDIUM_SKIP_PRICE
else:
    bags_amt = int(input("How many bags do you want (up to 4)? "))
    if bags_amt > 4:
        print("Maximum bags allowed is 4. A quote for 4 will be given.")
        user_choice = "Bags X 4"
        user_cost = 180
    else:
        user_choice = f"Bags X {bags_amt}"
        user_cost = SMALL_BAG_PRICE * bags_amt

repeat_customer = input("Are you a repeat costumer? (y/n) ")

if repeat_customer == 'y':
    discount_text = "(10% discount applied)"
    discount = user_cost / 100 * 10
    user_cost = user_cost - discount

print(f"QUOTE DETAILS"
      f"\n=============="
      f"\nName:{first_name[0].capitalize():>8}. {surname.capitalize()}"
      f"\n{'Order:':<12}{user_choice}"
      f"\nCost:{'€':>8}{user_cost:>5.2f} {discount_text}")
