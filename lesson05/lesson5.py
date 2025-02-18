# Lesson 5
startMoney = input ("Enter money you started with: ")
cookies = input ("Enter b for every big cookie and c for every small cootie:")
money = float(startMoney)

bigCookies=0
normalCookies=0
for currentCookie in cookies: 
    if currentCookie == "b":
        bigCookies+=1

    elif currentCookie == "c": 
        normalCookies+=1
    else: 
        print (f"{currentCookie} is not a valid sale item")

print (f"number of cookies sold is: {bigCookies+normalCookies}")

profit = (bigCookies*(2.00-0.75)) + (normalCookies*(1.25-0.5))
print(f"The total profit was: {profit}")
finalMoney = profit+money
print (f"The money at the end of the day was {finalMoney}")