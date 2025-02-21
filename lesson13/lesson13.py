# Lesson 13
date= int(input("date: "))
month= int(input("month: "))
if month>2:
    print ("After")
elif month<2:
    print ("Before")
else: 
    if date> 18:
        print("After")
    elif date< 18:
        print ("Before")
    else:
        print("Special")
