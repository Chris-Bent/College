def main():

    first100Primes()

def first100Primes():
    for i in range(2, 100):
        x = i - 1
        isPrime = True

        while x != 1:
            if i % x == 0:
                isPrime = False
            break
        x = x - 1
        
    
    if isPrime == True:
        print(f"{i} is a prime number")
    else:
        print(f"{i} is not a prime number")

main()