#Taking user's input 
user_number= int(input("Enter whole numbers in numeric form, enter -1 to exit :")) 
#Establishing sum and count 
sum=0 
count=0 

#While loop when the number is smaller than -1 
while user_number != -1 :
    sum+= user_number
    count+=1 
    user_number= int(input("Enter whole numbers in numeric form, enter -1 to exit :"))
    #calculating average when -1 is entered 
if user_number==-1:
    print ("The average of inputs is:")
    print (sum/count)
 




                 