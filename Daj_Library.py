"""
Title: Library_Dhiraj
Authour: Dhiraj Meenavilli
Date: October 26 2018
"""
### --- Inputs --- ###
def operations():
    customer = str(input("What is the customer's name?"))
    print("")
    return customer

def served():
  try:
    ask = int(input("Was the previous customer served justice ice tea? (1 yes, 2 no)"))
  except ValueError:
    return served()
  return ask

