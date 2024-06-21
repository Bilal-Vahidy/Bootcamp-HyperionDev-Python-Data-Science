#Taking in user's cycle time 

cycle= input ("Please enter the time taken to complete cycling in minutes using only numerical characters: ") 

if cycle.isnumeric()==False: 
    print ("Please only use numerical characters")
    cycle= input ("Please enter the time taken to complete cycling in minutes using numerical characters: ") 
    numeric_cycle= float(cycle)
else:
    numeric_cycle= float(cycle)
#Taking in user's running time 
run= input ("Please enter the time taken for running in minutes using only numerical characters: ") 

if run.isnumeric()==False: 
    print ("Please only use numerical characters")
    run= input ("Please enter the time taken for running in minutes  using only numerical characters: ") 
    numeric_run= float(run)
else: 
    numeric_run= float(run)
#Taking user's swimming time 
swim= input("Please enter the time to complete the swimming portion in minutes using  numerical characters only :")

if swim.isnumeric()==False: 
    print ("Please use numeric characters only")
    swim=input("Please enter the time to complete the swimming portion in  minutes using numerical characters only :")
    numer_swim= float(swim)       
else:
    numer_swim= float(swim)       
#Calculating toal 
total= numer_swim + numeric_cycle + numeric_run 
print("")
print ("Your total time is :")
print(total)  

#Determining Award 
#Checking if total time is between 0-100 minutes to recieve Provincial Colours
if total <=100: 
    print ("You recieve the award : Provincial colours ")
#Checking if total time is between 101-105 minutes to recieve Provincial half colours
if total >=101: 
    if total  <=105: 
        print ("Your award is Provincial half colours") 
# Checking if total time is between 106-110 minutes to recieve Pronvicial scroll
if total >=106: 
    if total <=110: 
        print ("You recieve the Provincial scroll award")
#Checking if total time is 111+ minutes to see if no award is given 
if total >=111:  
    print ("You  recieve no award. Better luck next time!")
