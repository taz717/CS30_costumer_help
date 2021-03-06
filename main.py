'''
Costumer help
Daj and Taz
Oct 26, 2018
'''
### imports ###
from library import * # Big Library hours
from Daj_Library import * 

### Vars ###
Q = [] #The queue array
NS = [] #The not served array
S = [] #The served array

#### Actual Code Starts Here!!! ####
run =  True
menu()
loop = 0
termination = 0
enter = 1

### inputs ###
while run:
  if termination == 0: # This makes it so that the customer rep doesn't have to keep inputing customers that don't exist
    while enter == 1:
        customer = operations() # This asks for the customers name and holds it as an input
        ask = int(input("Are there more customers in line(1 for no)"))
        addToList(customer, Q)#This then appends the customers name to a list which we can edit.
        if ask == 1:
            enter = 0
      
  if loop > 0: # This is so that every time a new customer is entered the previousnes status can be updates so the sales rep doesn't have to remember at the end of the day/.
      
    askServe = served() #This allows for the customer rep to say wether a customer was served or not
    print("")
    
    if askServe == 1: 
      cust = Q.pop(0) #This removes the item from the list but stores it as a variable
      S.append(cust) #This then appends it to a list of served customers
      ask2 = int(input("Did more customers come in to be serviced(1 for yes)"))
      if ask2 == 1:
          enter = 1
    if askServe == 2:
      cust2 = Q.pop(0) #This removes the item from the list but stores it as a variable
      NS.append(cust2) #This then appends it to a list of unserved customers
      ask3 = int(input("Did more customers come in to be serviced(1 for yes)"))
      if ask3 == 1:
          enter = 1
          
  again =input("Do you want to close down for the day (1) means yes, any other imput will ask for the input of the next customers name") #This allows the service rep to close down the system once there are no more customers in need of service
  print("")
  
  print("")
  print(len(Q))

  if again == "1" and len(Q) == 0: # This is the function which allows the termination of the program
    run = False
  
  elif len(Q) > 0 and again == "1": #This makes it so that if there are no more customers for the dy wether the last customer was served or not is recorded
    termination = 1
  
  print("In queue is",Q) #This shows the Queued customers

  print("")
  
  loop = loop + 1
  

### proccessing ###
NS.reverse()# This makes it so that the Not Served list is in order of most recently not served to least recently not served

### outputs ###
endScreen(S,NS)

