# Lesson 32
def characterFinder(text,text2):
    '''Prints all characters used from strings
    input: 
    Text1 is a string based input that consist of different characters
    Output: 
    Putputs all the character that the string has without repetition
    '''
    text=text.replace(" ","")
    text2=text2.replace(" ","")
    totalCharacters=''
    for character in text:
        if character not in totalCharacters and character in text2:
            totalCharacters+=character 
    return sorted(totalCharacters)

input1=characterFinder(input("Word 1: "), input("Word 2: "))

print(f"The characters are: {input1}")
