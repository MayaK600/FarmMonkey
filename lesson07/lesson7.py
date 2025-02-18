# Lesson 7
from random import randrange 
difficulty = int (input("Enter the DC: "))
diceRoll= randrange (1,21) #It never includes b
print (f"The player has rolled:{diceRoll}")
if diceRoll >=difficulty:
    print (f"The played was successful as {diceRoll} > {difficulty} ")
else: 
    print (f"The player was not successful as {diceRoll} is not greater than {difficulty} ")