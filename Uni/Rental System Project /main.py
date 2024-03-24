import datetime


def display_equipment_list(equipment_file):
    # Display list of equipment with daily rental rate.
    print("List of Equipment:\n")
    with open(equipment_file, "r") as file:
        for line in file:
            parts = line.strip().split(",")

            # Getting the equipment type and the equipment cost
            equipment_type = parts[0]
            equipment_cost = int(parts[1])

            print(f"Type: {equipment_type} | Daily Rental Cost: {equipment_cost}\n")


def get_rental_booking():
    # Open the file containing equipment details
    equipment_data = "equipment_data.txt"

    # Display list of equipment with daily rental rate
    display_equipment_list(equipment_data)

    # Ensure the name is at least 1 character long does not exceed 20 character
    while True:
        booking_name = input("Please enter your name: ")
        if 0 < len(booking_name) < 20:
            break
        else:
            print("Please enter a name with at least 1 character and max of 20.")

    # Validate phone num to be numeric and exactly 10 digits long
    while True:
        contact_number = input("Please enter your contact number: ")
        if contact_number.isdigit() and len(contact_number) == 10:
            break
        else:
            print("Please enter a phone number with exactly 10 digits long.")

    # Get rental equipment
    while True:
        booking_equipment = input("Please enter equipment for booking: ")

        # Open the file containing valid equipment options
        with open(equipment_data, "r") as file:
            # Read each line from the file
            valid_equipment = [line.strip().split(",")[0] for line in file]

        if booking_equipment in valid_equipment:
            break
        else:
            print("Invalid. Please pick from the list above.")

    # Maximum of 7 days per rental
    while True:
        rental_duration = int(input(f"Enter rental duration for {booking_equipment} (in days): "))
        if rental_duration > 7:
            print("There is a limit of 7 days per rental.")
        else:
            break

    # calculate the rental cost based on equip and duration
    with open(equipment_data, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if parts[0] == booking_equipment:
                equipment_cost = int(parts[1])
                break

    total_cost = equipment_cost * rental_duration

    # Create a file with customer details
    booking_details = f"Name: {booking_name}\nPhone number: {contact_number}\nEquipment rented: {booking_equipment}" \
                      f"\nRental duration: {rental_duration} days\nTotal cost: ${total_cost}"
    customer_file_name = f"{booking_name}_booking.txt"
    with open(customer_file_name, "w") as customer_file:
        customer_file.write(booking_details)

    # Add booking information to Bookings_2024.txt
    booking_info = f"{booking_name}, {datetime.datetime.now().strftime('%d/%m/%Y')}\n"
    with open("Bookings_2024.txt", "a") as bookings_file:
        bookings_file.write(booking_info)


def main():
    get_rental_booking()


main()
