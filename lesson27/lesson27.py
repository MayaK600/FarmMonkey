# Lesson 27
def stringCleaner(text):
    '''cleans string and retuns the word with only alpha characters in lower case
    input: User inputs a certain word 
    output: The program outputs all alpha characters in lower case together
    '''
    reslut =""
    for character in text:
        if character.isalpha():
            result+=character.lower()
    return result 
value= stringCleaner("Hell0, world!")
print (value)
