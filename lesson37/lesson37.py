# Lesson 37
def stringCompresson(text):
    ''' takes a string and for all letters that are the same together it compresses to the letter 
    and number of occuranses 
    For exmple: 
        input: aaaaabbcaa
        output:a5b2c1a2
    '''
    result=''
    counter = 1
    for i in range(1,len(text)):
        if text[i] == text[i-1]:
            counter+=1
        else:
            result+=text[i-1]
            result+=str(counter)
            counter=1
    result+= text[-1] + str(counter)
    
    return result 

print(stringCompresson("abbbccccdddaa"))