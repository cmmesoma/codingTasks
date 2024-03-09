# This is python programming task
# the aim of this task is to create a holiday cost of any cities of your choice.
# def keywords are primarily used here.
# if, elif and else statements are used.

print("WELCOME TO MESO LOGISTICS, WE WILL BE TAKING YOU TO PARIS, BRUSSELS, LISBON, NAIJA OR ONTARIO") # prints out WELCOME TO MESO LOGISTICS, WE WILL BE TAKING YOU TO PARIS, BRUSSELS, LISBON, NAIJA OR ONTARIO

city_flight = input("Please enter the city: ").lower() # inputs made by user whether in lowercase or uppercase is recognised and accepted. 

def plane_cost(city_flight): # the def keyword defines the function plane_cost containing the parameter city_flight.
    
    if city_flight == "paris": # if user enters paris, 80 is returned.
        return 80
    elif city_flight == "brussels": # if user enters brussels, 100 is returned.
        return 100
    elif city_flight == "lisbon": # if user enters lisbon, 220 is returned.
        return 220
    elif city_flight == "naija": # if user enters naija, 550 is returned.
        return 550
    elif city_flight == "ontario": # if user enters ontario, 600 is returned.
        return 600
    else:
        return print("Invalid Input") + exit() # if user enters any other character apart from the aforementioned cities, the application exits and prints out invalid input. 

print("") # an empty string to create space and make the output less compacted.

num_nights = int(input("Please enter the number of nights you will spend: ")) # user enters the number of nights he or she will spend in the city. Since we are dealing with days or nights, whole numbers are used, thus the reason for the int variable.


def hotel_cost(num_nights): # the def keyword defines the function hotel_cost containing the parameter num_nights.
    per_night = 100 # you can assign a fixed amount of your choice.
    return per_night*num_nights # the product of per_night and num_nights is returned.

print("") # an empty string to create space and make the output less compacted 

rental_days = int(input("Please enter the number of days you will hire a car: ")) #user enters the number of days he or she will hire a car. if he or she does not want a rental car, he or she inputs zero.
def rental_cost(rental_days): # the def keyword defines the function rental_cost containing the parameter rental_days 
    per_day = 10 # you can affix a chosen amount
    return per_day*rental_days # the product of per_day and rental_days is returned.

print("") # an empty string to create space and make the output less compacted 

def holiday_cost(num_nights, city_flight, rental_days): # the def keyword defines the function holiday_cost containing the parameters num_nights, city_flight and rental_days

    hotelCost = hotel_cost(num_nights) # the defined function is assigned a new variable called hotelCost

    planeCost = plane_cost(city_flight) # the defined function is assigned a new variable called planeCost

    rentalCost = rental_cost(rental_days) # the defined function is assigned a new variable called rentalCost

    total_cost = hotelCost + planeCost + rentalCost # sum of the hotelCost, planeCost and rentalCost.

    return total_cost # total_cost is returned


print("For", num_nights, "days in", city_flight, "the holiday cost is £",holiday_cost(num_nights, city_flight, rental_days)) # prints out the holiday cost, the city and the days planned to stay.
