#Creating variable rental days to get user to input how many days car will be rented
  #ensuring input is only a whole interger


while True:
    try:
        rental_days=int(input("Using whole numbers in numeric format"
                              ",Please enter how many days a car will be rented : "))
        break
    except ValueError:
        print ("Please use whole numbers and numeric digits!")


#Creating num_nights input to see how long user stays at hotel 
        
while True:
    try:
        num_nights=int(input("Using whole numbers in numeric format"
                              ",Please enter how many nights you will stay at the hotel : "))
        break
    except ValueError:
        print ("Please use whole numbers and numeric digits!")

#Calculating the cost of city desination
#Note rather than give an option of cities for user to select, this programme will ascribe 
    #numerical values to each letter of the city

#Making dictionary for letter values
letter_values = {'a': 4, 'b': 21, 'c': 13, 'd': 4, 'e': 5, 'f': 19, 'g': 12, 'h': 8, 'i': 9, 'j': 10,
    'k': 17, 'l': 13, 'm': 14, 'n': 16, 'o': 17, 'p': 16, 'q': 17, 'r': 4, 's': 2,
    't': 12, 'u': 11, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26 ,'A': 4, 'B': 21, 'C': 13, 'D': 4, 'E': 5, 'F': 19, 'G': 12, 'H': 8, 'I': 9, 'J': 10,
    'K': 17, 'L': 13, 'M': 14, 'N': 16, 'O': 17, 'P': 16, 'Q': 17, 'R': 4, 'S': 2,
    'T': 12, 'U': 11, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26 ,' ':0 , '.':0 }


#Creating city_flight to get user to input destination 
city_flight=input("Please enter desination city : ")
#plane_cost function

def plane_cost (city_flight):
    numerical_value=0
    for letter in city_flight:
        numerical_value+=letter_values[letter]
        int(numerical_value)
        ticket_price=numerical_value
        # holiday_cost(ticket_price)
    return( numerical_value)   
ticket=plane_cost(city_flight)



#creating hotel_cost function 
def hotel_cost(num_nights):
    """This function takes the cost of hotel  as 100 per night and multiplies it to the num_nights  user input
              i.e how many nights do you stay at the hotel"""
    hotel_rate=100
    stay_price=num_nights * hotel_rate
    # holiday_cost(stay_price)
    return (num_nights * hotel_rate)


stay_cost=hotel_cost(num_nights)



# creating car_rental function to multiply rental_days with car cost
def car_rental(rental_days):
    """This function takes the cost of car as 80 per day and multiplies it to the rental_days user input
              i.e how many days the car was rented"""
    cost_car=80 
    vehicle=rental_days * cost_car
    # holiday_cost(vehicle)
    return (rental_days * cost_car)

vehicle=car_rental(rental_days) 

#driver function for holiday cost 
def holiday_cost ():
    total=holiday_cost
    print (f"  The total cost of your holiday is : ", vehicle + ticket +stay_cost)

holiday_cost()

#Printing details 
print ("")
print("Based on the information you entered : ")

print (f" Your expenditure on the plane ticket will be :", ticket)
print (f"Your expenditure on hotel costs :" , stay_cost)
print (f"Your expenditure on car rental will be : ", vehicle)

print ("")
print ("HAVE A PLEASANT HOLIDAY!")