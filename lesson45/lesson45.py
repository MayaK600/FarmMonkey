# Lesson 45
def wordLen(aList):
    dictionary={}
    for word in aList:
        dictionary[word]=len(word)
    return dictionary 

test=["apple","cherry","banana","lemon"]
print(wordLen(test))