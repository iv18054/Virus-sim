# Ivan VAY
# 30/11/21
# Virus sim v4

#Import code from another file to generate color
from idlecolors import *

# List to hold all countries
name_of_the_countrys = []
infected_percentage = []
on_lockdown = []

#Intro
printc( orange("Welcome to Virus Simulator, to start the game follow the instruction below"))
printc( purple("==========================================================================="))

# Function which get the country data from the user
def add_countrys_to_game():
    add_country = ""
    # Loop allow user to continue to add countries
    while True:
        add_country = input("Write the name of the country you will like to add and then press enter. If you are done adding countries, type \"done\" and press enter to proceed. ")
        # If the user has entered a valid country, create the country and add it to the list
        if add_country != "done":
            while len(add_country) == 0:
                print("You haven't typed anything, try again")
                add_country = input()
            infected_percentages = int(input("Type in what the current percentage of infected people for " + add_country+ " and then press enter to continue. "))
            name_of_the_countrys.append(add_country)
            infected_percentage.append(infected_percentages)
            on_lockdown.append(False)
        # If the user is done, break out of function
        else:
            break


# Function to print the current information about infected and lockdown status
def print_infos(name_of_the_countrys, infected_percentage, on_lockdown):
    infos = "" + name_of_the_countrys + " right now has " + str(infected_percentage) + " percent infected, and "
    if on_lockdown == True:
        infos += "is in lockdown."
    else:
        infos += "is not in lockdown."
    return infos


# Function to ask the user which country to help
def ask_which_country_to_support():
    # Create a string to display to the user which each option
    chosen_country = "Which country would you like to provide assistance to? Choose from the following options:"
    for country in name_of_the_countrys:
        chosen_country += "\n" + country
    # Check that selected option is valid
    while True:
        country_to_support = input(chosen_country)
        for country in name_of_the_countrys:
            if country_to_support == country:
                # Return the name of the country if it is valid
                return country_to_support
        # Print an error message and return to the top of the loop if the entry is invalid
        print("The input was invalid, please try again.")


# Function runs every new day. Requires argument of the country to help.
def new_day(country_to_support):
    printc( red("=== NEW DAY ==="))
    list_index = 0
    for country in name_of_the_countrys:
        # If one of the country was asisted by the user, the percentage of infected will be deducted by 40%
        # For the country that is already at 40% or below, it can't be lesser than 0%
        if country == country_to_support:
            if infected_percentage[list_index] >= 40:
                infected_percentage[list_index] = infected_percentage[list_index] - 40
            else:
                infected_percentage[list_index] = 0
        # If one of the country is already at 80% or higher, it can't go over 100% infected
        else:
            if infected_percentage[list_index] >= 80:
                infected_percentage[list_index] = 100
            else:
                infected_percentage[list_index] = infected_percentage[list_index] + 20
        # Print the current status of the country
        print(print_infos(name_of_the_countrys[list_index], infected_percentage[list_index], on_lockdown[list_index]))
        list_index += 1
    printc( red("=== END DAY ==="))

add_countrys_to_game()
for i in range(0, 5):
    new_day(ask_which_country_to_support())
