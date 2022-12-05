#!/usr/bin/python3

# Louis Fennell III, November 14, 2022, CPT-168-W02, Final Projects

# This program, party_planner.py, is as party planning program that is an 
# interface for interacting with a database of party attendees, their meal 
# choice, their paid fee, their guests, and their guests meal choice, which is
# stored in an external CSV file. This program will iterate on each row in the
# csv file through the program which allows it to be searched through, read 
# from, and written to.

import sys
import csv
import locale as lc
from decimal import Decimal, ROUND_HALF_UP

FILENAME = "partyplanner.csv"

# Defines the function, write_attendees(), with the argument, attendees. This 
# function is called when the user is going to write new data into the 
# external csv file, "partyplanner.csv" which is stored in the constant, 
# FILENAME.
def write_attendees(attendees):
    with open(FILENAME, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerows(attendees)

# Defines the function, read_attendees(). This function is called when the 
# user wants to read the data stored in the external csv file, 
# "partyplanner.csv" which is stored in the constant, FILENAME.
def read_attendees():
    attendees = []
    with open(FILENAME, newline="", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        for row in reader:
            attendees.append(row)
    return attendees

# Defines the function, set_platform(). This function should set the correct
# locale based on what system being used.
def set_platform():
    if sys.platform == "win32":
        # displays the results in the correct currency format for the US for 
        # Windows.
        lc.setlocale(lc.LC_ALL, "us")      # for Windows
    elif sys.platform == "darwin":
        # display the results in the correct currency format for the US for 
        # macOS.
        lc.setlocale(lc.LC_ALL, "en_US")    # for Mac OS X

# Defines the function, display_meal_choices(). This function displays the 
# menu choices menu, that the user can select their choice from. 
# Example output:
#
#     Meal choices are as follows:
#
#     1.   Chicken Picatta
#     2.   Beef Wellington
#     3.   Vegetarian Lasagna
#     4.   Filet Mignon
#     5.   Blackened Mahi-Mahi
#     6.   Fettuccine Alfredo
#     7.   Fish and Chips
#
#     Command: 
#
def display_meal_choices():
    print("\nMeal choices are as follows:")
    print("\n1.   Chicken Picatta")
    print("2.   Beef Wellington")
    print("3.   Vegetarian Lasagna")
    print("4.   Filet Mignon")
    print("5.   Blackened Mahi-Mahi")
    print("6.   Fettuccine Alfredo")
    print("7.   Fish and Chips")

# Defines the function, attendee_meal_choice_commands(). This function 
# contains all of the code to choose which meal choice the attendee wants.
# the choices are stored in the variable, meal_choice, inside of a while True:
# loop.
def attendee_meal_choice_commands():
    # Calls the display_meal_choices() to print out the menu choices.
    display_meal_choices()
    
    while True:
        
        meal_choice = input("\nChoose an entree option: ")
        if meal_choice == "1":
            meal_choice = "Chicken Picatta"
        elif meal_choice == "2":
            meal_choice  = "Beef Wellington"
        elif meal_choice == "3":
            meal_choice  = "Vegetarian Lasagna"
        elif meal_choice == "4":
            meal_choice  = "Filet Mignon"
        elif meal_choice == "5":
            meal_choice  = "Blackened Mahi-Mahi"
        elif meal_choice == "6":
            meal_choice  = "Fettuccine Alfredo"
        elif meal_choice == "7":
            meal_choice = "Fish and Chips"
        else:
            print("Invalid choice. Please try again.")
        return meal_choice

# Defines the function, search_attendees(), with the argument, attendees. This
# function is intended to allow the user to search for if a user has been 
# entered into the csv file.
def search_attendees(attendees):
    choice = "y"
    
    attendees = read_attendees()
    
    while choice == "y":
        search_term = input("\nEnter First or Last Name to Search For: ").title()
        print("_" * 79)
        #search_term = "Blair"
        #loop through the csv list
        for row in attendees:
            if search_term in row[0]:
                print(f"\nName: {row[2]} | Meal Choice: {row[3]}")
            if search_term in row[1]:
                print(f"\nName: {row[2]} | Meal Choice: {row[3]}")
            if len(row) > 5 and search_term in row[5] and row[5] != "":
                print(f"\nName: {row[7]} | Meal Choice: {row[8]}")
            if search_term in row[6]:
                print(f"\nName: {row[7]} | Meal Choice: {row[8]}")
#        if search_term not in row[0] not in row[1] not in row[5] not in row[6]:
#                print("\nNo such attendee.")
            #elif search_term in row[5]:
                #print(print(f"\nName: {row[7]} | Meal Choice: {row[8]}"))
            #if current rows 2nd value is equal to input, print that row
                #print(f"\nName: {row[7]} Meal Choice: {row[8]}")
        print("_" * 79)
        choice = input("\nWould you like to search for another attendee? y/n: ")

# Defines the function, add_guest(), with the argument, attendees. This 
# function uses a while loop for, while the variable, choice, matches the 
# string, "y". This loop contains an if and an elif statement for whether the
# attendee is bringing a guest or not. When the user enters, "y", for bringing
# a guest the user is asked to input the attendees first name then their last
# name. That users meal choice is then asked for and that value is stored, the
# paid fee value, $22.00 is stored then the user is asked for the first and 
# last names of the guest and then their meal choice. Once all this data is
# stored in the list, attendee, that data is then appended to the attendees
# list and then that data is written to the partyplanner.csv file.
def add_guest(attendees):

    attendees = read_attendees()
    
    choice = "y"
    
    while choice == "y":
        
        bringing_guest = input("\nIs the member bringing a guest? (y/n): ").lower()
        if bringing_guest == "y":

            first_name = input("\nEnter Member's First Name: ").title()
            last_name = input("\nEnter Member's Last Name: ").title()
            full_name = (f"{first_name} {last_name}")
            meal_choice = attendee_meal_choice_commands()
            fee_paid = Decimal(22.00)
            fee_paid = fee_paid.quantize(Decimal("1.00"), ROUND_HALF_UP)
            fee_paid = lc.currency(fee_paid, grouping=True)
            guests_first_name = input("\nEnter Guest's First Name: ").title()
            guests_last_name = input("\nEnter Guest's Last Name: ").title()
            guests_full_name = (f"{guests_first_name} {guests_last_name}")
            guests_meal_choice = attendee_meal_choice_commands()
            guests_fee_paid = Decimal(22.00)
            guests_fee_paid = guests_fee_paid.quantize(Decimal("1.00"), 
                                                    ROUND_HALF_UP)
            guests_fee_paid = lc.currency(guests_fee_paid, grouping=True)

            attendee = [first_name, last_name, full_name, meal_choice,
                                fee_paid, guests_first_name,
                                guests_last_name, guests_full_name,
                                guests_meal_choice, guests_fee_paid]
            
            fee = Decimal(44.00)
            fee = lc.currency(fee, grouping=True)
            
            print(f"\n{full_name} has been added to the list. {first_name}",
                f"has paid their {fee} total fee and {guests_first_name}",
                "is attending the party with them.")
            
            attendees.append(attendee)
            write_attendees(attendees)
            
            choice = input("\nAdd another Member and/or Guest? (y/n): ")
                
        elif bringing_guest == "n":
            first_name = input("\nEnter Member's First Name: ").title()
            last_name = input("\nEnter Member's Last Name: ").title()
            full_name = (f"{first_name} {last_name}")
            meal_choice = attendee_meal_choice_commands()
            fee_paid = Decimal(22.00)
            fee_paid = fee_paid.quantize(Decimal("1.00"), ROUND_HALF_UP)
            fee_paid = lc.currency(fee_paid, grouping=True)
            
            attendee = [first_name, last_name, full_name, meal_choice,
                        fee_paid]

            fee_paid

            print(f"\n{full_name} has been added to the list. {first_name}",
                f"has paid their {fee_paid} total fee.")

            attendees.append(attendee)
            write_attendees(attendees)
            
            choice = input("\nAdd another Member and/or Guest? (y/n): ")

def delete_attendee(attendees):
    attendees = read_attendees()
    
    option = "y"
    
    adjusted_attendees_list = []
    
    while option == "y":
        delete_attendee = input("Member to delete: ").title()
        if option == "y":
            for row in attendees:
                if row[0] == delete_attendee:
                    attendees.remove(row)
                    adjusted_attendees_list.append(row)
                elif len(row) == 10 and row[5] == delete_attendee:
                    attendees.remove(row)
                    adjusted_attendees_list.append(row)
                elif row[0] == delete_attendee:
                    print("Attendee does not exist")
                elif len(row) == 10 and row[5] != delete_attendee:
                    print("Attendee does not exist")
        if option == "n":
            break
        option = input("Would you like to remove another member? (y/n)").lower()
        
    adjusted_attendees_list.append(attendees)
    write_attendees(attendees)

''' if len(row) == 10 and row[5] != "":
    print(f"{row[0]:10}| {row[1]:<12}| {row[2]:<18}|".format(*row),
            f"{row[3]:<20}| {row[4]:<10}".format(*row))
    print(f"{row[5]:10}| {row[6]:<12}| {row[7]:<18}|".format(*row),
            f"{row[8]:<20}| {row[9]:<10}".format(*row))
if len(row) == 5:
    print(f"{row[0]:10}| {row[1]:<12}| {row[2]:<18}|".format(*row),
            f"{row[3]:<20}| {row[4]:<10}".format(*row))'''
        
# Defines the function, print_table_list(), with the argument, attendees. This
# function prints an output of all guests and their meal choices formatted in a
# table with members who aren't bringing guests printing below that. Example:
#
# First     | Last        | Full Name         | Meal                | Fee
# --------------------------------------------------------------------------
# Katie     | Stayton     | Katie Stayton     | Beef Wellington     | $22.00
# Brian     | Lord        | Brian Lord        | Filet Mignon        | $22.00
# Louis     | Fennell     | Louis Fennell     | Fettuccine Alfredo  | $22.00
# Danielle  | Fennell     | Danielle Fennell  | Blackened Mahi-Mahi | $22.00
# Bob       | Marley      | Bob Marley        | Vegetarian Lasagna  | $22.00
# Louis     | Fennell     | Louis Fennell     | Filet Mignon        | $22.00
# Susan     | Fennell     | Susan Fennell     | Chicken Picatta     | $22.00
#
def display_all_attendees(attendees):
    
    print()
    print("First\t  | Last\t| Full Name\t    | Meal\t\t  | Fee")
    print("-" * 74)
    
    for row in attendees:
        if len(row) == 10 and row[5] != "":
            print(f"{row[0]:10}| {row[1]:<12}| {row[2]:<18}|".format(*row),
                  f"{row[3]:<20}| {row[4]:<10}".format(*row))
            print(f"{row[5]:10}| {row[6]:<12}| {row[7]:<18}|".format(*row),
                  f"{row[8]:<20}| {row[9]:<10}".format(*row))
        if len(row) == 5:
            print(f"{row[0]:10}| {row[1]:<12}| {row[2]:<18}|".format(*row),
                  f"{row[3]:<20}| {row[4]:<10}".format(*row))
        elif len(row) == 0 and row[5] == "":
            continue
        elif row[5] == "":
            print(f"{row[0]:10}| {row[1]:<12}| {row[2]:<18}|".format(*row),
                  f"{row[3]:<20}| {row[4]:<10}".format(*row))
    print("-" * 74)

def total_fees_paid(attendees):
    attendees = read_attendees()
    
    number_of_fees = 0
    
    for row in attendees:
        if len(row) == 11 and row[6] != "":
            number_of_fees += 2
        if len(row) == 5:
            number_of_fees += 1
        elif len(row) == 0 and row[6] == "":
            continue
        elif row[5] == "":
            number_of_fees += 1
    
    number_of_fees = Decimal(number_of_fees)
    total_fees = number_of_fees * 22
    
    total_fees = total_fees.quantize(Decimal("1.00"), ROUND_HALF_UP)
    total_fees = lc.currency(total_fees, grouping=True)

    print(f"Total fees collected: {total_fees}")

# Defines the function, view_all_attendees(), with the argument, attendees. 
# This function will bring a three option menu allowing the user to choose
# to view a list of either all members or all guests.
def view_all_attendees(attendees):
    choice = "y"
    
    attendees = read_attendees()
    
    while choice == "y":
        print()
        print("1.   Members")
        print("2.   Guests")
        option = input("\nPlease choose an option: ").lower()
        if option == "1":
            view_all_members(attendees)
        elif option == "2":
            view_all_guests(attendees)
        elif option == "0":
            break
        else:
            print("Invalid command. Please try again.")
        choice = input("\nWould you like to view another list? y/n: ")

# Defines the function, view_all_attendees(), with the argument, attendees. 
# This function adds up the total amount of both members and guests and outputs
def total_attendees(attendees):
    attendees = read_attendees()
    
    number_of_attendees = 0
    
    for row in attendees:
        if len(row) == 10 and row[5] != "":
            number_of_attendees += 2
        if len(row) == 5:
            number_of_attendees += 1
        elif len(row) == 0 and row[5] == "":
            continue
        elif row[5] == "":
            number_of_attendees += 1

    print(f"\nThe Total Number of Attendees is: {number_of_attendees}")

# Defines the function, calculate_meal_totals(), with the argument, attendees. 
# This function adds up the total amount of every meal choice for both members
# and guests and prints each meal choice name followed by total number of that
# choice.
def calculate_meal_totals(attendees):
    attendees = read_attendees()
    
    chicken_picatta_total = 0
    beef_wellington_total = 0
    filet_mignon_total = 0
    fettuccine_alfredo_total = 0
    vegetarian_lasagna_total = 0
    blackened_mahi_mahi_total = 0
    fish_and_chips_total = 0
    total_number_of_meals = 0
    
    for row in attendees:
        if len(row) == 10:
            if row[3] == "Chicken Picatta":
                chicken_picatta_total += 1
            if row[3] == "Beef Wellington":
                beef_wellington_total += 1
            if row[3] == "Filet Mignon":
                filet_mignon_total += 1
            if row[3] == "Fettuccine Alfredo":
                fettuccine_alfredo_total += 1
            if row[3] == "Vegetarian Lasagna":
                vegetarian_lasagna_total += 1
            if row[3] == "Blackened Mahi-Mahi":
                blackened_mahi_mahi_total += 1
            if row[3] == "Fish and Chips":
                fish_and_chips_total += 1
            if len(row) > 5 and row[8] != "":
                if row[8] == "Chicken Picatta":
                    chicken_picatta_total += 1
                if row[8] == "Beef Wellington":
                    beef_wellington_total += 1
                if row[8] == "Fettuccine Alfredo":
                    filet_mignon_total += 1
                if row[8] == "Fettuccine Alfredo":
                    fettuccine_alfredo_total += 1
                if row[8] == "Vegetarian Lasagna":
                    vegetarian_lasagna_total += 1
                if row[8] == "Blackened Mahi-Mahi":
                    blackened_mahi_mahi_total += 1
                if row[8] == "Fish and Chips":
                    fish_and_chips_total += 1
        if len(row) == 5:
            if row[3] == "Chicken Picatta":
                chicken_picatta_total += 1
            if row[3] == "Beef Wellington":
                beef_wellington_total += 1
            if row[3] == "Fettuccine Alfredo":
                filet_mignon_total += 1
            if row[3] == "Fettuccine Alfredo":
                fettuccine_alfredo_total += 1
            if row[3] == "Vegetarian Lasagna":
                vegetarian_lasagna_total += 1
            if row[3] == "Blackened Mahi-Mahi":
                blackened_mahi_mahi_total += 1
            if row[3] == "Fish and Chips":
                fish_and_chips_total += 1

    total_number_of_meals += (fish_and_chips_total + blackened_mahi_mahi_total 
    + vegetarian_lasagna_total + fettuccine_alfredo_total + filet_mignon_total 
    + beef_wellington_total + chicken_picatta_total)

    print("\nTotal Number of Each Meal Choice")
    print(f"\nChicken Picatta: {chicken_picatta_total}")
    print(f"Beef Wellington: {beef_wellington_total}")
    print(f"Filet Mignon: {filet_mignon_total}")
    print(f"Fettuccine Alfredo: {fettuccine_alfredo_total}")
    print(f"Vegetarian Lasagna: {blackened_mahi_mahi_total}")
    print(f"Blackened Mahi-Mahi: {blackened_mahi_mahi_total}")
    print(f"Total meals to cook: {total_number_of_meals}")

'''
The below function was used to test and work out what methods and functions 
were and were not working inside of the partyplanner.py program. This function
was mostly used while initially testing to get the input of attendees and 
their guests from the user and storing that data in the attendee and attendees
lists. Was consistently having issues where none of the data that I inputted 
was saving to the external csv file like I wanted them to.

def test_function():
    
    with open(FILENAME, encoding="utf-8-sig") as f:
        csv_f = f.read()
        # Create a list of each row
        rows = csv_f.split("\n")
        #print(f"\n{rows}\n")
        #print(type(rows))

        # Iterate through each row
        for row in rows:
            # Split the row into info
            info = row.split(",")
            #print(f"\n{row}")
            #print(type(info), (f"\n{info}\n"))
            
            # Checks if the row is the proper length if member is bringing 
            # a guest.
            if len(info) > 4:
                # Separate out the data
                first_name = info[0]
                last_name = info[1]
                full_name = info[2]
                meal_choice = info[3]
                fee_paid = float(info[4])
                fee_paid = Decimal(fee_paid)
                fee_paid = fee_paid.quantize(Decimal("1.00"), ROUND_HALF_UP)
                fee_paid = lc.currency(fee_paid, grouping=True)
                guests_first_name = info[5]
                guests_last_name = info[6]
                guests_full_name = info[7]
                guests_meal_choice = info[8]
                #print(info[9])
                #guests_fee_paid = float(info[9])
                #guests_fee_paid = Decimal(guests_fee_paid)
                #guests_fee_paid = guests_fee_paid.quantize(Decimal("1.00"), ROUND_HALF_UP)
                #guests_fee_paid = lc.currency(guests_fee_paid, grouping=True)
            
                #attendee_and_guest = [first_name, last_name, full_name, 
                #                      meal_choice, fee_paid, guests_first_name,
                #                      guests_last_name, guests_full_name,
                #                      guests_meal_choice, guests_fee_paid]
            # Checks if the row is shorter than 10 items.
            elif len(info) == 4:
                # Separate out the data
                first_name = info[0]
                last_name = info[1]
                full_name = info[2]
                meal_choice = info[3]
                fee_paid = float(info[4])
                fee_paid = Decimal(fee_paid)
                fee_paid = fee_paid.quantize(Decimal("1.00"), ROUND_HALF_UP)
                fee_paid = lc.currency(fee_paid, grouping=True)
                
                attendee = [first_name, last_name, full_name, meal_choice,
                            fee_paid, guests_first_name,]

'''

# Defines the function, view_all_attendees, with the argument, attendees. This
# function, when called, will print a list of all the current attendees using
# a for loop.
def view_all_members(attendees):
    attendees = read_attendees()
    print("\n#  | Full Name")
    print("-" * 25)
    for i, row in enumerate(attendees, start=1):
        print(f"{i:<3}| {row[2]:20}".format(*row))
    print("-" * 25)

def party_stats(attendees):
    
    total_number_of_attendees = total_attendees()
    total_number_of_meals = calculate_meal_totals()
    
    print(f"Total number of attendees: {total_number_of_attendees}")
    print(f"Total number of meals: {total_number_of_meals}")
    print(f"Total fee amount paid: {total_number_of_meals}")

# Defines the function, view_all_attendees, with the argument, attendees. This
# function, when called, will print a list of all the current guest attendees 
# using a for loop.
def view_all_guests(attendees):
    
    attendees = read_attendees()
    
    guests_list = []
    
    print("\n#  | Full Name")
    print("-" * 25)

    for row in attendees:
        if len(row) > 5 and row[5] != "":
            guests_list = guests_list.append(attendees)
        if len(row) < 6 or row[5] == "":
            continue
    print(guests_list)
    '''for i, row in enumerate(attendees, start=1):
        if len(row) > 5 or row[5] != "":
            #print(row[7])
            print(f"{i:<3}| {row[7]:20}".format(*row))'''

    print("-" * 25)

# Defines the function, search_options_commands(). This function is to display
# the search menus options.
def display_search_options():
    print()
    print("-" * 30)
    print("| Search Menu |")
    print("-" * 30)
    print("0.   Exit Search")
    print("1.   Start Search")
    print("2.   Info")

# Defines the function, search_options_commands(), with the argument, 
# attendees. This function is for the search menus commands. Allow the user to
# choose the option they want to run.
def search_options_commands(attendees):
    
    attendees = read_attendees()
    
    command = True
    while command == True:
        display_search_options()
        
        option = input("\nPlease Select an Option: ")
        if option == "1":
            search_attendees(attendees)
        elif option == "2":
            print("Searches list of attendees and outputs the user and their",
                  "\nmeal choice if they are in the list of attendees.")
        elif option == "0":
            command = False
            display_registration_menu()
        else:
            print("Invalid command. Please try again.")

# Defines the function, display_main_menu(). This function will draw the main
# menu that displays when the program is first ran. The output display will be
#
#    -----------------------------
#    | The Party Planner Program |
#    -----------------------------
#    
#    Main Menu
#
#    Please Choose An Option:
#
#    0.   Exit the Planner
#    1.   Registration Menu
#    2.   Reports Menu
#    ______________________________
#    
#    Command: 
#
def display_main_menu():
    print()
    print("-" * 29)
    print("| The Party Planner Program |")
    print("-" * 29)
    print("\nMain Menu\n")
    print("Please Choose An Option:\n")
    print("0.   Exit the Planner")
    print("1.   Registration Menu")
    print("2.   Reports Menu")
    print("_" * 30)

# Defines the function, main_menu_commands(), with the argument, attendees.
# This function contains a while loop that, while True, loops through all of
# the available main menu commands.
def main_menu_commands(attendees):
    
    attendees = read_attendees()
    
    while True:
        print()
        command = input("Command: ")
        if command == "1":
            registration_menu_commands(attendees)
        elif command == "test":   # Used to quickly test new functions
        #    total_fees_paid(attendees)
            delete_attendee(attendees)
        #    calculate_meal_totals(attendees)
        #    total_attendee_report(attendees)
        #    test_print_list(attendees) # renamed
        #    test_find_guest()
        #    test_find_guest()
        #elif command == "fee test":
        #    paid_fee(guest_list)
        elif command == "2":
            reports_menu_commands(attendees)
        elif command == "3":
            print("nothing here yet")
        elif command == "0":
            print("\nGoodbye!")
            break
        else:
            print("Unknown command. Please try again.")

# Defines the function, display_reports_menu. This function contains the code
# to display the reports menu and its options. Below is an example:
#
#   ---------------------
#   | Registration Menu |
#   ---------------------
#   
#   Please Choose An Option
#   
#   0.   Return to Main Menu
#   1.   List All Attendees
#   2.   Add A Member
#   3.   Delete A Member
#   4.   Search for a Member
#   5.   View Reports Menu
#   ______________________________
#   
#   Command: 
#
def display_registration_menu():
    print()
    print("-" * 21)
    print("| Registration Menu |")
    print("-" * 21)
    print("\nPlease Choose An Option\n")
    print("0.   Return to Main Menu")
    print("1.   List All Attendees")
    print("2.   Add A Member")
    print("3.   Delete A Member")
    print("4.   Search Attendees")
    print("5.   View Reports Menu")
    print("_" * 30)

# Defines the function, registration_menu_commands(), with the argument, 
# attendees. This function contains
def registration_menu_commands(attendees):
    
    attendees = read_attendees()
    
    command = True
    while command == True:
        display_registration_menu()

        option = input("\nCommand: ").lower()
        if option == "1":
            display_all_attendees(attendees)
        elif option == "2":
            add_guest(attendees)
        elif option == "3":
            delete_attendee(attendees)
        elif option == "4":
            search_options_commands(attendees)
        elif option == "5":
            reports_menu_commands(attendees)
        elif option == "0":
            command = False
            display_main_menu()
        else:
            print("Invalid command. Please try again.")

# Defines the function, display_reports_menu. This function contains the code
# to display the reports menu and its options. Below is an example:
# 
#    ----------------------------------
#   | The Party Planner Reports Menu |
#   ----------------------------------
#   0.   Return to Main Menu
#   1.   Attendee List
#   2.   Guest List
#   3.   View All
#   4.   Party Statistics
#   5.   View All Meal Choices
#   6.   List Total Paid Attendees
#   7.   View Total Meal Amount
#   8.   View Total Fees Paid
#   9.   Registration Menu
#   ______________________________
#   
#   Command: 
#
def display_reports_menu():
    print()
    print("-" * 34)
    print("| The Party Planner Reports Menu |")
    print("-" * 34)
    print("0.   Return to Main Menu")
    print("1.   View All")
    print("2.   View Members or Guests")
    print("3.   Party Statistics")
    print("4.   List Total Attendees")
    print("5.   List Total Members")
    print("6.   List Total Guests")
    print("7.   View Total Meal Amount")
    print("8.   View Total Fees Paid")
    print("9.   Registration Menu")
    print("-" * 34)

# Defines the function, reports_menu_commands. This function contains the code
# to choose what reports to run.
def reports_menu_commands(attendees):
    
    attendees = read_attendees()
    
    command = True
    while command == True:
        display_reports_menu()
        option = input("\nCommand: ").lower()
        if option == "0":
            command = False
            display_main_menu()
        elif option == "1":
            display_all_attendees(attendees)
        elif option == "2":
            view_all_attendees(attendees)
        elif option == "3":
            party_stats(attendees)
        elif option == "3":
            print("FUNCTION UNAVAILABLE")
        elif option == "4":
            total_attendees(attendees)
        elif option == "7":
            calculate_meal_totals(attendees)
        elif option == "8":
            total_fees_paid(attendees)
        elif option == "9":
            registration_menu_commands(attendees)
        else:
            print("\nUnknown command. Please try again")

# Defines the main function.
def main():
    
    # Sets the correct locale for the operating system that the user is on.
    set_platform()
    
    # Calls the function, display_main_menu, which prints the initially 
    # available commands.
    display_main_menu()

    # Sets the list, attendees as equal to calling the read_attendees() 
    # function.
    attendees = read_attendees()
    # Used to test above function, read_attendees(), was stored in attendees
    # properly
    # print(f"\n{attendees}")
   
    # Calls the function, write_attendees(attendees)
    write_attendees(attendees)
    # calls the function, main_menu_commands(attendees).
    main_menu_commands(attendees)

# If statement that calls the main() function at the programs start, if 
# __name__ matches the text string, "__main__".
if __name__ == "__main__":
    main()