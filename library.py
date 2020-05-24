'''
Functions of Costumer aid
Daj and Taz
Oct 26, 2018
'''
import sys
### Inputs ###
def menu():
        print('''Why hello there, welcome to the handy dandy root and andy menu''')
        

### processing ###

def addToList(item, list):
        #Just adds to an array
        list.append(item)
        return list


### outputs ###

def endScreen(a, b):
  try:
    view = int(input('''
    Hello there! What would you like to do?
    (1) View how many people got served
    (2) View how many peoplle didn't get served
    (3) To exit the program and close up shop for the day
    '''))
    if view == 1:
      print(a)
      return endScreen(a,b)
    elif view == 2:
      print (b)
      return endScreen(a,b)
    elif view == 3:
      sys.exit()
  except ValueError:
    return endScreen()
