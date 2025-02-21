# Lesson 24
name=input("Name: ").lower()
largestName=''
length=0
while name!="x":
    if len(name)>length:
        length=len(name)
        largestName = name

    name=input("Enter next Name: ").lower()

print(f"The longest name is: {largestName}")