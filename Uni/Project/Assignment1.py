# Author: Sara Jane Kenny
# Purpose: A program that runs a practice quiz for students in maths and polish.

import random
import datetime

# Setting const variables
NOT_GOOD = f"\U0001F97A"
CONTENT = f"\U0001F60A"
VERY_GOOD = f"\U0001F44D"
PERFECT = f"\U0001F389"

# Gathering user input
first_name = input("Enter your first name? ")
surname_name = input("Enter your surname? ")

# Setting global variables
result = 0
rand_math_ans = 0
user_ans = -1
user_word = ""
polish_word = 0
quiz_count = 0
percentage = 0
percentage_total = 0
feedback_lang = ""
lang_level = ""
feedback_math = ""
user_finished = 'no'
user_validate = 'yes', 'no'
emoji = ""

f = open(f"logs.txt", "a")  # open filename, continue writing into file
print(f"Welcome {first_name}")

while user_finished == 'no':
    # Get user choice of quiz
    print(f"\n1: Maths"
          f"\n2: Polish")
    user_choice = int(input(">>> "))

    if user_choice == 1:
        # Setting up the time, each time a student takes a test update date and time
        dt = datetime.datetime.now()
        month = dt.strftime("%B")
        num_date = dt.strftime("%d")
        year = dt.strftime("%Y")
        timestamp = dt.strftime("%H:%M")
        date = f"{month} {num_date}, {year} {timestamp}"

        q_asked = 1
        quiz_count += 1
        score = 0
        num_math_q = int(input(f"\n{first_name} how many questions? "))
        while num_math_q < 5 or num_math_q > 25:
            num_math_q = int(input(f"\n{first_name} how many questions?(min5/max25) "))
        for a in range(num_math_q):
            user_ans = -1
            random_num_one = random.randint(1, 12)
            random_num_two = random.randint(1, 12)

            # to stop negatives numbers only do subtraction if 1st rand num is greater or equal to the 2nd rand num
            if random_num_one >= random_num_two:
                print(f"{q_asked}:", random_num_one, "-", random_num_two, "= ", end="")
                rand_math_ans = random_num_one - random_num_two
                while not int(user_ans > -1):
                    try:
                        user_ans = int(input(""))
                        # if user answer input is negative prompt the user again
                        if user_ans < 0:
                            print("There are no negative answers. Try again: ")
                    except ValueError:
                        print("That's not a valid number. Try again: ")
                feedback_math += f"\n{q_asked}: {random_num_one} - {random_num_two} = {user_ans}"
            else:
                # else just add the rand nums together
                print(f"{q_asked}:", random_num_one, "+", random_num_two, "= ", end="")
                rand_math_ans = random_num_one + random_num_two
                while not int(user_ans > -1):
                    try:
                        user_ans = int(input(""))
                        if user_ans < 0:
                            print("There are no negative answers. Try again: ")
                    except ValueError:
                        print("That's not a valid number. Try again: ")
                feedback_math += f"\n{q_asked}: {random_num_one} + {random_num_two} = {user_ans}"

            # Add to score and finished the string output
            if rand_math_ans == user_ans:
                score += 1
                feedback_math += f" \u2705"
            else:
                feedback_math += f" \u274C should be {rand_math_ans}"

            # Calculate the score percentage and add 1 to questions asked count
            percentage = score / num_math_q
            q_asked += 1

        # If the questions are finished print the feedback from the quiz
        if q_asked > num_math_q:
            if rand_math_ans == user_ans:
                print(f"{feedback_math}")
            else:
                print(f"{feedback_math}")

        if percentage < 0.5:
            emoji = NOT_GOOD
        elif percentage < 0.7:
            emoji = CONTENT
        elif percentage < 0.99:
            emoji = VERY_GOOD
        else:
            emoji = PERFECT
        print(f"\n{first_name}, you got {percentage:.0%} {emoji}\n")
        print(f"{first_name} {surname_name} - MATHS - {date}: {percentage:.0%}", file=f)
        percentage_total += percentage
        feedback_math = ""

        user_finished = input(f"Are you finished? (yes/no) ")
        while user_finished not in user_validate:
            user_finished = input(f"Are you finished? (yes/no) ")

    elif user_choice == 2:
        dt = datetime.datetime.now()
        month = dt.strftime("%B")
        num_date = dt.strftime("%d")
        year = dt.strftime("%Y")
        timestamp = dt.strftime("%H:%M")
        date = f"{month} {num_date}, {year} {timestamp}"

        quiz_count += 1
        score = 0
        # Open language level file student inputs and store in a variable
        user_level = int(input(f"What is your current level {first_name}? "))
        if user_level == 1:
            connection = open("Polish1.txt", "r")
            lang_level = "POLISH1"
        elif user_level == 2:
            connection = open("Polish2.txt", "r")
            lang_level = "POLISH2"
        elif user_level == 3:
            connection = open("Polish3.txt", "r")
            lang_level = "POLISH3"
        elif user_level == 4:
            connection = open("Polish4.txt", "r")
            lang_level = "POLISH4"
        else:
            connection = open("Polish5.txt", "r")
            lang_level = "POLISH5"

        for word in connection:
            user_word = ""
            word = word.rstrip()
            word = word.split(",")
            english_word = word[0]
            polish_word = word[1]

            print(f"{english_word} = ", end="")
            while not str(user_word):
                user_word = input("")
                if user_word == "":
                    print("You must give an answer. Try again: ")
            feedback_lang += f"\n{english_word} = {user_word}"

            # Add to score and finished the string output
            if user_word == polish_word:
                score += 1
                feedback_lang += f" \u2705"
            else:
                feedback_lang += f" \u274C should be {polish_word}"
            percentage = score / 5

        # If the questions are finished print the feedback from the quiz
        if user_word == polish_word:
            print(f"{feedback_lang}")
        else:
            print(f"{feedback_lang}")

        if percentage > 0.7:
            if user_level < 5:
                print(f"\nThe next time you use this program you should start with level {user_level + 1}")

        if percentage < 0.5:
            emoji = NOT_GOOD
        elif percentage < 0.7:
            emoji = CONTENT
        elif percentage < 0.99:
            emoji = VERY_GOOD
        else:
            emoji = PERFECT
        print(f"\nResult: {score}/5\n{first_name}, you got {percentage:.0%} {emoji}\n")
        connection.close()

        print(f"{first_name} {surname_name} - {lang_level} - {date}: {percentage:.0%}", file=f)
        percentage_total += percentage
        feedback_lang = ""

        user_finished = input(f"Are you finished? (yes/no) ")
        while user_finished not in user_validate:
            user_finished = input(f"Are you finished? (yes/no) ")

# Calculate the average of all the quiz percentages that were taken by the student
percentage_avg = percentage_total / quiz_count
print(f"\nYour average score for all quiz is {percentage_avg:.0%}"
      f"\nYour teacher can view details in log.txt")

f.close()
