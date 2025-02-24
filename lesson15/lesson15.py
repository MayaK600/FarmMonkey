# Lesson 15
userInput=input("Enter fruit: ").lower()
fruits= ['apple','bananas', 'kiwi', 'strawberry']
found= False
for fruit in fruits: 
    if fruit == userInput:
        print (f"{userInput} is found!")
        found = True 
if not found: 
    print (f"{userInput} is not found")