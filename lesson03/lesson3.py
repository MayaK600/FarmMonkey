# Lesson 3
import math
tiles = input ("Enter the number of input: ") 
tiles = int(tiles) #Assumes it is string so have to conert to int
sqrt = math.floor(math.sqrt(tiles))
print (f"The sides of the square will be {sqrt}")
# ORR 
#calculation = int((tiles ** 0.5)//1) --> which then converts it into an int and to be safe using an int f
# The two // mean floor division, so it divides and rounds down