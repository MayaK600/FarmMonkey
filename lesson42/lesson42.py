# Lesson 42
def possibleSum(aList,target):
    '''determine if a pair of numbers in an array add up to a target value
    input (list): a list/array of randomly inputed numbers 
    input (target-> integer): the target value that  the program tries to reach by adding two numbers 

    process: the program will look through all the possible numbers in the array and look at all 
    the numbers that come after to determine if any of them add up to target. 

    output: True if true and flase if not possible 
    '''
    found=False
    for i, value in enumerate(aList): 
        newTarget=target - value
        if newTarget in aList[i+1:]:
            found=True 
    return found 

test=[1,3,4,11,16,20,28]
target=16
print (possibleSum(test,target))