# Initialize variables
pool_volume = int(input("Enter pool volume in liters: "))
filter_capacity = int(input("Enter filter capacity in liters: "))
current_water_level = 0

# Display menu options
menu = {
    "B": "Backwash",
    "R": "Rinse",
    "F": "Filter",
    "W": "Waste",
    "C": "Recirculate",
    "X": "Closed"
}


# Define functions for each option
def backwash():
    global current_water_level
    print("Activating backwash valve...")
    print("Draining wastewater from the pool...")
    current_water_level -= filter_capacity
    print("Current water level: {} liters".format(current_water_level))


def rinse():
    print("Activating rinse valve...")
    print("Running pump for a few minutes...")
    print("Current water level: {} liters".format(current_water_level))


def pool_filter():
    print("Activating filter valve...")
    print("Cleaning the filter...")
    print("Maintaining current water level...")
    print("Current water level: {} liters".format(current_water_level))


def waste():
    global current_water_level
    print("Activating waste valve...")
    print("Draining water from the pool without passing through the filter...")
    current_water_level -= int(input("Enter amount of water to drain in liters: "))
    print("Current water level: {} liters".format(current_water_level))


def recirculate():
    print("Activating recirculate valve...")
    print("Bypassing the filter and circulating water back into the pool...")
    print("Current water level: {} liters".format(current_water_level))


def closed():
    print("Closing all valves and turning off the pump...")


# Main program loop
while True:
    # Display menu options
    print("Menu:")
    for key, value in menu.items():
        print("{}: {}".format(key, value))
    option = input("Enter option: ").upper()

    # Perform action based on option
    if option == "B":
        backwash()
    elif option == "R":
        rinse()
    elif option == "F":
        pool_filter()
    elif option == "W":
        waste()
    elif option == "C":
        recirculate()
    elif option == "X":
        closed()
        break
    else:
        print("Invalid option. Please try again.")

    # Ask if user wants to perform another action
    another_action = input("Perform another action? (Y/N): ").upper()
    if another_action == "N":
        break

print("Program ended.")
