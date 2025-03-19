# Lesson 45
def wordLen(aList):
    dictionary={}
    for word in aList:
        dictionary[word]=len(word)
    return dictionary 

test=["apple","cherry","banana","lemon"]
print(wordLen(test))

#Fibonacci:
def d_fib(num):
    result={0:0 , 1:1}
    if num in result: 
        return result 
    else:
        for i in range(2,num+1):
            result[i]=result[i-1]+result[i-2]
    return result 

print(d_fib(4))