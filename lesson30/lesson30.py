# Lesson 30
num = int(input("Num: "))
pyramid=''
for number in range (1,num+1):
    if number % 2 ==1:
        pyramid+='1'
    else:
        pyramid+='0'
    print (pyramid)
