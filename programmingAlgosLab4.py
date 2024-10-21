def main():
    
    firstFiveEven()
    averageFive()

def firstFiveEven():
    count = 0
    evenNum = 2

    while count < 5:
        print(evenNum)
        count += 1
        evenNum += 2
    
def averageFive():
    totalSum = 0
    numsAdded = 1 
    while numsAdded <= 5:
        totalSum += numsAdded
        numsAdded += 1
    print(totalSum / 5)



main()