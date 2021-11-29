#Ivan VAY
#26/11/21
#Virus sim 2

#List to hold all the countries
country_list = []

NZ = ("New Zealand")
CH = ("China")
JP = ("Japan")
country_list.append(NZ)
country_list.append(CH)
country_list.append(JP)

#Function to ask user which country to add
def add_country():
    #Loop keeps adding countries until the user is done
    while True:
        country = input("Which country would you like to add?")
        if country != "done":
            infected = int(input("What percent of the country is infected"))
        #If user is done adding countries break out of function
        else:
            break
        newlist = country
        i = country_list.append(newlist)
        for i in country_list:
            print(i)
            
#Function to ask user if they will want to add a country
def main():
    country = input("If you would like to add in a country, type in \"add\" or type in \"done\" and press enter")
    if country.lower() == "add":
        add_country()
    elif country.lower() == "done":
        help()


if __name__ == "__main__":
    main()
