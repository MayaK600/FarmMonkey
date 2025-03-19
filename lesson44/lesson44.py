# Lesson 44
def cFrequency(word):
    characterList=sorted(word.lower())
    answer = {}
    for letter in characterList:
        if letter not in answer:
            answer[letter]=1
        else:
            answer[letter]+=1     
    return answer

test="hello"
print (cFrequency(test))