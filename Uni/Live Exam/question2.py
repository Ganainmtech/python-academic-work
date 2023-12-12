# Author: Sara Jane Kenny, Student Num: R00255434 - 2 Hours for 4 questions
# Purpose: A program that allows users to book for a skip

# Setting const variables
LARGE_SKIP_PRICE = 280
MEDIUM_SKIP_PRICE = 200
SMALL_BAG_PRICE = 50

# Setting global variables
discount_text = ""
user_cost = 0
quote_feedback = ""
order_feedback = ""
quote_count = 1
bags_ordered = 0
bags_count = 0

# Display text and gather user inputs
num_of_quotes = int(input("Enter the number of skips you wish to order: "))

for a in range(num_of_quotes):
    print(f"\nSkip Drop\tCompany"
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
        quote_feedback += (f"\nName:{first_name[0].capitalize():>8}. {surname.capitalize()}" 
                           f"\nOrder:{user_choice:>11}" 
                           f"\nCost:{'€':>8}{user_cost:>5.2f} {discount_text}")
    elif user_choice == 2:
        user_choice = "Medium"
        user_cost = MEDIUM_SKIP_PRICE
        quote_feedback += (f"\nName:{first_name[0].capitalize():>8}. {surname.capitalize()}" 
                           f"\nOrder:{user_choice:>12}" 
                           f"\nCost:{'€':>8}{user_cost:>5.2f} {discount_text}")
    else:
        bags_ordered += 1
        bags_amt = int(input("How many bags do you want (up to 4)? "))
        if bags_amt > 4:
            bags_count += 4
            print("Maximum bags allowed is 4. A quote for 4 will be given.")
            user_choice = "Bags X 4"
            user_cost = 180
        else:
            bags_count += bags_amt
            user_choice = f"Bags X {bags_amt}"
            if bags_amt == 4:
                user_cost = 180
            else:
                user_cost = SMALL_BAG_PRICE * bags_amt
        quote_feedback += (f"\nName:{first_name[0].capitalize():>8}. {surname.capitalize()}" 
                           f"\nOrder:{user_choice:>14}" 
                           f"\nCost:{'€':>8}{user_cost:>5.2f} {discount_text}")

    repeat_customer = input("Are you a repeat costumer? (y/n) ")
    if repeat_customer == 'y':
        discount_text = "(10% discount applied)"
        discount = user_cost / 100 * 10
        user_cost = user_cost - discount
    else:
        # if user is not a repeat costumer
        f = open(f"new_customers.txt", "a")  # open file
        print(f"{surname},{first_name}", file=f)
        f.close()

    print(f"QUOTE #{quote_count}"
          f"\n=============="
          f"\n{quote_feedback}")
    order_feedback += f"\n#{quote_count:<3}{first_name[0].capitalize():>3}. {surname.capitalize()}"
    quote_count += 1

quote_count = 0
print(f"\nOrder Contacts"
      f"\n---------------"
      f"{order_feedback}\n"
      f"\nTotal Bag Orders: {bags_ordered} ({bags_count} bags)")
