# Lesson 31
def anagramChecker(text1,text2):
    '''Checks if two strings are anagrams of each other 
    Input: 
        text1= first string  input 
        text2= a second string input 
    Output: Outputs True or False based on if it is an anagram or not
    '''
    checker=True
    for character in text1:
        if character.isalpha() and character in text2:
            text2=text2.replace (character,"",1) 
        else :
            checker=False 
    return checker
print (f"The words are anagrams: {anagramChecker('hello','ollhe')}")
