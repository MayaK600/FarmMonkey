# Lesson 33
def medianFinder(numberList):
    numberList=numberList.split(" ")
    numberList=list(map(float, numberList))
    numberList=sorted(numberList)
    median=0
    if len(numberList)%2==0:
        median =(numberList[len(numberList)//2 -1] + (numberList[(len(numberList)//2)*(-1)]))/2
    else: 
        median = numberList[len(numberList)//2]
    mean=sum(numberList)/len(numberList)
    return median,mean

print (medianFinder("3 7 1 2 5"))