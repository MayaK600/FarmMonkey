# Lesson 41
def scrabbleScore(text):
    counter=0
    for character in text.upper():
        if character in "EAIOUNSRTL":
            counter+=1
        elif character in "DG":
            counter+=2
        elif character in "BCMP":
            counter+=3
        elif character in "FHVWY":
            counter+=4
        elif character in "K":
            counter +=5
        elif character in "JX":
            counter+=8
        elif character in "ZQ":
            counter+=10

    return counter

def bestScore(aList):
    '''
    '''
    bestScore=["",0]
    for word in aList:
        currentScore=scrabbleScore(word)
        if currentScore>=bestScore[1]:
            bestScore[0]=word
            bestScore[1]=currentScore
    return bestScore

words={
    'hello',
    'my',
    'name',
    'is',
    'Maya'
}

print(bestScore(words))