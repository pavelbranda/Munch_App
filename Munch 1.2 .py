''''

Munch App MVP
v0.1
By Pavel Branda
The purpose of Munch is to produce a dinner menu from favourite dishes,
and produce a shopping list of ingrediens if required.
'''

#---- Imports ----

from random import choice


# ----- A. Functions -----
# A1. Choose dishes

def chooseDishes(days):
    while len(myMenu) < int(days):
        chosenDish = choice(foodWeLike)
        if chosenDish not in myMenu:
            myMenu.append(chosenDish)
    print("Done! Here's your menu...")
    import time 
    time.sleep(1)
    print() 
    for dish in myMenu:
        print(myMenu.index(dish) + 1, dish)
    print()
    print("Out of all these dishes, my favourite has to be..." + choice(myMenu))
    import time 
    time.sleep(1)

# A2. Build shopping list

def buildShoppingList():
    myShoppingList = []   
    if "Pizza" in myMenu:
        myShoppingList.append(pizza)
    if "Beef Burgers" in myMenu:
        myShoppingList.append(beefBurgers)
    if "Pork Stir Fry" in myMenu:
        myShoppingList.append(porkStirFry)
    if "Chicken Fajitas" in myMenu:
        myShoppingList.append(chickenFajitas)
    if "Bangers and Mash" in myMenu:
        myShoppingList.append(bangersMash)
    if "Fish and Chips" in myMenu:
        myShoppingList.append(fishChips)
    if "Spanish Omelette" in myMenu:
        myShoppingList.append(spanishOmelette)
    print()
    for dish in myShoppingList:
        for ingredient in dish:
            print(ingredient)
    print()
    print("Voila! Bon apetit!")

# ------ B. Lists --------

foodWeLike = ["Pizza", "Beef Burgers", "Pork Stir Fry", "Chicken Fajitas", "Bangers and Mash", "Fish and Chips", "Spanish Omelette"]

pizza = ["Pizza  Base", "Tomato Sauce", "Cheese", "Peperroni", "Chillis",""]
beefBurgers = ["Beef Patties", "Burger Rolls", "Lettuce", "Tomatoes", "Relish",""]
porkStirFry = ["Pork Loin", "Peppers", "Onions", "Hoi Sin Sauce", "Noodles",""]
chickenFajitas = ["Chicken Breast", "Red Peppers", "Onion", "Fajita Kit",""]
bangersMash = ["Sausages", "Mashed Potatoes", "Gravy", "Onion", "Peas",""]
fishChips = ["Fish", "Potatoes", "Tartare Sauce", "Peas",""]
spanishOmelette = ["Eggs", "Chorizo", "Baby Potatoes", "Peppers", "Onions",""]


myMenu = []




# 1. How many days to plan?

print("Hello, I'm Munch! I'll help you to plan your dinner menu...")
import time 
time.sleep(1)

answer = input("How many days would you like me to plan? ")

print("OK, I'm going to plan "+ answer + " dinner(s) from your favourite meals list")
import time 
time.sleep(1)

# 2. Choose dishes

chooseDishes (answer)


# 3. Build shopping list?

def endProgram():
    print()
    print("You got it! Bye for now :)")
    

while True:
    answer = input("Would you like a shopping list for this menu? Enter 'y' or 'no'...")
    import time 
    time.sleep(1)
    if answer in ("y", "Y", "n", "N"):
        break
    print("Hmm. Sorry, I didn't catch that. Please try again...")
    
if answer in ("y", "Y"):
    buildShoppingList()
else:
    endProgram()

