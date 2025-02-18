# Lesson 8
winCounter=0
for i in range(6):
    result = input(f"Enter if you won game number {i+1} ")
    if result == "W" or result =="w":
        winCounter+=1
if winCounter>4:
    print (f"Player is in group 1")
elif winCounter >2:
    print (f"Player is in group 2")
elif wincounter >0:
    print (f"Player is in group 3")
else:
    print ("Player is eliminated")
 
