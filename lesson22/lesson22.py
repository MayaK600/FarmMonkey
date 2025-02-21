# Lesson 22
N=int(input("N: "))
fZero=0
fOne=1
fN=0
for i in range (2,N+1):
    fN=fZero+fOne
    fZero=fOne
    fOne=fN 

print(f"The Nth term is: {fN}")