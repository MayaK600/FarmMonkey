# Lesson 34

def stringToList(text):
    ''' take a string and return it back as a list of integers 
    '''
    text=text.split(",")
    text=list(map(int,text))
    return text
from random import randrange

def randList(start, end, frequency):
    ''' Creates a list of randomly generated numbers 
    Input: start and end which are the integers for the range of numbers
    frequncy is the numbers in the list
    Output: a list of integers
    '''
    if end>start and frequency>0:
        a_list=[]
        for i in range(frequency):
            a_list.append(randrange(start,end+1))
        return a_list
    else: 
        return []
print (stringToList("1,2,3,4,5"))
print (randList(1,100,5))


