# Lesson 29
def consonantsCounter(text, vowel=False ):
    '''
    Function will look over the characters of a word and retun the number of consonants in it
    input: 
        Text: The user will input a string 
        Vowel: It is assumed to be false when counting for consonants 
    Output: The number of consonants in that said string
    '''
    counter=0
    for character in text: 
        character=character.lower()
        if character.isalpha() and character not in {'a','e','i','o','u'}:
            counter+=1
    if not vowel:
        return counter
    else: 
        counter =0
        for character in text:
            character=character.lower()
            if character.isalpha() and character in {'a','e','i','o','u'}:
                counter+=1  
        return counter

value1 = consonantsCounter(Hello World!)
value2 = consonantsCounter(Hello World!, True)
print (f"The number is {value1}")
print (f"The number is {value2}")