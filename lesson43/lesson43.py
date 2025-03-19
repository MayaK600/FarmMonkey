# Lesson 43
def duplicateRemove(aList):
    ''' turns a list into a set so the duplicates are removed'''
    aSet=set()
    for item in aList:
        aSet.add(item)
    return aSet

test=[1,2,3,3,45,5,45]
print (duplicateRemove(test))
