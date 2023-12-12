# Const variable declared
# The basic hour rate is declared
basicHourRate = 50.43
# The over time small rate is declared
overTimeSmallRate = 1.5
# The over time big rate is declared
overTimeBigRate = 2
# The USC small rate is declared
uscSmallRate = 1.5
# The USC big rate is declared
uscBigRate = 2
# The small tax rate is declared
taxSmallRate = 22.5
# The big tax rate is declared
taxBigRate = 40.5


# Main function for displaying welcome and menu results
def main():
    displayWelcome()

    displayMenuResults()


# Displays a welcome message and summarises what the program does
def displayWelcome():
    print("***************** Welcome to our tax calculator! *****************"
          "\n* This program calculates an employee’s tax, USC, gross and net. *"
          "\n******************************************************************")


# Prompts the employee for an ID number and returns it
def getEmployeeId():

    validInt = False
    while not validInt:
        try:
            # Prompts user for employee ID
            employeeId = input("\nEnter Employee ID:(min 5 digits) ")
            # While the length is less or equal to 4 prompt for employee ID again
            while len(employeeId) <= 4:
                employeeId = input("\nEnter Employee ID:(min 5 digits only) ")
            # Converts employeeID string into an int to check if it is valid as an int in the try except
            int(employeeId)
        except ValueError:
            print("\nError: Min 5 Digits!")
        else:
            validInt = True
    return employeeId


# Prompts the employee for basic work hours and returns it
def getBasicWorkHours():
    validInt = False
    while not validInt:
        try:
            basicWorkHours = int(input("Enter your work hours: "))
        except ValueError:
            print("Please enter the amount of hours worked.\n")
        else:
            validInt = True
    return basicWorkHours


# Prompts the employee for overtime work hours and returns it
def getOverTimeWorkHours():
    validInt = False
    while not validInt:
        try:
            overTimeHours = int(input("Enter your overtime work hours: "))
        except ValueError:
            print("Please enter the amount of hours worked for overtime.\n")
        else:
            validInt = True
    return overTimeHours


# Displaying a menu full of options and returns userOption
def displayMenu():
    print("\nMenu Options: (choose a number)"
          "\n1. Calculate Gross Pay",
          "\n2. Calculate USC and Tax",
          "\n3. Calculate Net Pay",
          "\n4. Summary",
          "\n5. Exit")
    # Prompting the user to pick a number that corresponds to the menu above
    validInt = False
    while not validInt:
        try:
            userOption = int(input("Please choose an option via number: "))
        except ValueError:
            print("Please enter an number that corresponds to the menu.\n")
        else:
            validInt = True
    return userOption


# Calculating only the basic gross pay and returns basicGrossPay
def calcBasicGrossPay(basicWorkHours):
    basicGrossPay = basicWorkHours * basicHourRate
    return basicGrossPay


# Calculating over time pay and returns overTimePay
def calcOverTimePay(basicGrossPay, overTimeHours):
    if basicGrossPay < 1700:
        overTimePay = overTimeSmallRate * (overTimeHours * basicHourRate)
    else:
        overTimePay = overTimeBigRate * (overTimeHours * basicHourRate)
    return overTimePay


# Calculating the total gross pay with over time pay included, and returns the totalGrossPay
def calcTotalGrossPay(basicGrossPay, overTimePay):
    totalGrossPay = basicGrossPay + overTimePay
    return totalGrossPay


# Calculating the USC Charge and Tax Charge, and returns uscCharge and taxCharge
def calcUscAndTax(totalGrossPay):
    # 250 euro from the first week is ignored from the USC charge
    uscAfterDeduction = totalGrossPay - 250
    # Calculating the USC at 1.5% for the next 200 euro and then at 2% for the remaining balance
    if uscAfterDeduction > 200:
        uscSpecialCharge = (200 / 100) * uscSmallRate
        uscBasicCharge = ((uscAfterDeduction - 200) / 100) * uscBigRate
        uscCharge = uscBasicCharge + uscSpecialCharge
    # Else calculating the USC at 2% for the remaining balance
    else:
        uscBasicCharge = (uscAfterDeduction / 100) * uscBigRate
        uscCharge = uscBasicCharge

    # Calculating the Tax at 22.5% if balance is greater than 1200 and then at 40.5% for the remaining balance
    afterUscCharge = totalGrossPay - uscCharge
    if afterUscCharge > 1200:
        taxSpecialCharge = (1200 / 100) * taxSmallRate
        taxBasicCharge = ((afterUscCharge - 1200) / 100) * taxBigRate
        taxCharge = taxBasicCharge + taxSpecialCharge
    # Else calculating the Tax at 40.5% for the remaining balance
    else:
        taxBasicCharge = (afterUscCharge / 100) * taxBigRate
        taxCharge = taxBasicCharge

    return uscCharge, taxCharge


# Calculating the total net-pay and returns it
def calcNetPay(totalGrossPay, uscCharge, taxCharge):
    netPay = totalGrossPay - uscCharge - taxCharge
    return netPay


# Display the results that the user selected
def displayMenuResults():

    # Call function to return employeeID
    employeeId = getEmployeeId()

    # Call function to return basic work hours
    basicWorkHours = getBasicWorkHours()

    # Call function to return over time hours
    overTimeHours = getOverTimeWorkHours()

    # Call function to return basic gross pay
    basicGrossPay = calcBasicGrossPay(basicWorkHours)

    # Call function to return over time pay
    overTimePay = calcOverTimePay(basicGrossPay, overTimeHours)

    # Call function to return total gross pay
    totalGrossPay = calcTotalGrossPay(basicGrossPay, overTimePay)

    # Keep displaying the menu until user has picked a valid option between 1 and 5
    userOption = displayMenu()
    while userOption > 1 or userOption < 5:
        if userOption == 1:
            # Runs total gross pay calculation and prints it
            totalGrossPay = calcTotalGrossPay(basicGrossPay, overTimePay)
            print(f"\n{'Gross Pay:':<25}{'€{:>10.2f}'.format(totalGrossPay)}")

        elif userOption == 2:
            # Runs USC and tax calculation and prints it
            uscCharge, taxCharge = calcUscAndTax(totalGrossPay)
            print(f"\n{'USC:':<25}{'€{:>10.2f}'.format(uscCharge)}"
                  f"\n{'Tax:':<25}{'€{:>10.2f}'.format(taxCharge)}")

        elif userOption == 3:
            # Runs net pay calculation and prints it
            netPay = calcNetPay(totalGrossPay, uscCharge, taxCharge)
            print(f"\n{'Net Pay:':<25}{'€{:>10.2f}'.format(netPay)}")

        elif userOption == 4:
            # Runs needed functions and prints them in a summary
            totalGrossPay = calcTotalGrossPay(basicGrossPay, overTimePay)
            uscCharge, taxCharge = calcUscAndTax(totalGrossPay)
            netPay = calcNetPay(totalGrossPay, uscCharge, taxCharge)
            print("\nSummary:"
                  f"\n{'Employee ID:':<25}{employeeId:>11}"
                  f"\n{'Basic Work Hours:':<25}{basicWorkHours:>11}"
                  f"\n{'Overtime Work Hours:':<25}{overTimeHours:>11}"
                  f"\n{'Gross Pay:':<25}{'€{:>10.2f}'.format(totalGrossPay)}"
                  f"\n{'USC:':<25}{'€{:>10.2f}'.format(uscCharge)}"
                  f"\n{'Tax:':<25}{'€{:>10.2f}'.format(taxCharge)}"
                  f"\n{'Net Pay:':<25}{'€{:>10.2f}'.format(netPay)}")

        elif userOption == 5:
            # Prints a goodbye message and exits the program
            print("\nThank you for using our calculator!")
            exit()
        userOption = displayMenu()


# Start of program
main()