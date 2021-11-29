#Ivan VAY
#29/11/21
#Vrius sim v3

#User input is stored
country_lists = []
percent_infected = []
max_length_list = 3
country_name = ""

#Data Collection
while len(country_name) < max_length_list:
    country_name = str(input("Please enter the name of a country you like to add to the list. ")).upper()
    country_lists.append(country_name)
    infected_percent = int(input("What percent fo the country is infected? "))
    percent_infected.append(infected_percent)


#Function to display informations
def print_details(self):
    details = "" + self.country_name + "has " + str(self.infected_percent) + " percent infected, and "
    if self.is_in_lockdown == True:
        details += "is in lockdown."
    else:

        details += "is not in lockdown."
    return details
    

#Function to ask user which country to support
def ask_which_country_to_support():
    support_country = "Which country would you like to support? "
    for country_name in country_list:
        help_country += "\n" + country.country_name
    #See if country name is vaild
    
    
print_details()
