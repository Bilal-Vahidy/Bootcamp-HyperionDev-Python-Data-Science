number_1 = input("Please type your first number (please use numeric characters): ")
if number_1.isnumeric():
    float_number_1 = float(number_1)
else:
    print("Please enter numeric characters only")
    number_1 = input("Please type your first number (please use numeric characters): ")

number_2 = input("Please type your second number (please use numeric characters): ")
if number_2.isnumeric():
    float_number_2 = float(number_2)
else:
    print("Please enter numeric characters only")
    number_2 = input("Please type your second number (please use numeric characters): ")

number_3 = input("Please type your third number (please use numeric characters): ")
if number_3.isnumeric():
    float_number_3 = float(number_3)
else:
    print("Please enter numeric characters only")
    number_3 = input("Please type your third number (please use numeric characters): ")
#the sum of all numbers 
total = float_number_1 + float_number_2 + float_number_3
print("")
print("the sum of your chosen numbers is : ") 
print(total)
print ("")
#first number minus second number 
second_calculation = float_number_1 - float_number_2
print ("the first number minus the second number is :")
print (second_calculation)
print("")

#third number multiplied by first number

third_calculation= float_number_3 * float_number_1 

print ("the third number multiplied by the first number is :")
print (third_calculation)
print ("")

#Sum divded by third number

final_calculation = total/float_number_3

print ("the total of your chosen numbers divided by your third number is :")
print (final_calculation)