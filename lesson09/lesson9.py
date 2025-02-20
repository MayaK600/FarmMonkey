# Lesson 9
user=input("Enter rock paper or scissors: ")
options = ["rock","paper","scissors"]
import random
computer = random.choice(options)
print (computer)
if computer == "rock":
    if user =="paper":
        print("user wins")
    elif user== "scissors":
        print ("computer wins")
    else:
        print ("Tie")

elif computer== "scissors":
    if user=="paper":
        print ("commputer wins")
    elif user == "rock":
        print ("user wins")
    else :
        print ("tie")
else :
    if user=="rock":
        print("computer wins")
    elif user =="scissors":
        print("user wins")
    else: 
        print ("tie")