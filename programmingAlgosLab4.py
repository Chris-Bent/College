def main():
    question = int(input("What question do you want to run? "))
    if question == 1:
        firstFiveEven()
    elif question == 2:
        averageFive()
    elif question == 3:
        factorialFor()
    elif question == 4:
        questionFour()
    elif question == 11:
        questionFourReasoning()


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

def factorialFor():
    val = int(input("Enter your number: "))
    total = 1
    for x in range(val, 0, -1):
        total = total * x
    print(total)

def questionFour():
    for a in range(1, 100, 10):
        print(a, a+1, a+2, a+3, a+4, a+5, a+7, a+8, a+9)

def questionFourReasoning():
    print("- The for loop iterates with 'a' through a range between 1, 96, with a step of 10")
    print("each loop a increases by 10. As 'a' is initially assigned the value of 1, the next value would be 11 (a + 10), then 21, then 31, and so on.")
    print("Each print statement then prints a (1, 11, 21, 31 and so on). Then it's next 9 values. (a+1, a+2, etc.)")
    print("this results in the output of the function.")
    print("The second value '97' is somewhat arbitrary as the program will only check for numbers up to the value - 1 ")
    print("The second value could be any value between 92 - 100 and achieve the same result")
main()