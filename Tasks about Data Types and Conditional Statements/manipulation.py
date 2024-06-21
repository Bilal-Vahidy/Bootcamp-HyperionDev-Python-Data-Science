#Creating variable that stores user input 
str_manip= input("Please write a sentence here:")

#Calculating length of input

length_of_string= len("string_manip")

print(length_of_string)
#Finding the last character of string and replacing it 
last_character= str_manip[-1]



replacement= str_manip.replace(last_character,"@")

print (replacement)

#Printing last three characters of string

reverse3= str_manip[-1] + str_manip[-2] + str_manip[-3]
print (reverse3)

#Combining first 3 characters of string with last two characters

x= str_manip [0] + str_manip [1] +str_manip[2] + str_manip[-1] +str_manip[-2]


print(x)