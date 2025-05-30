# Python3 implementation to check 
# if a number is a prime power number

from math import *

# Array to store the 
# prime numbers
is_prime = [True for i in range(10**6 + 1)] 
primes =[]

# Function to mark the prime 
# numbers using Sieve of 
# Eratosthenes
def SieveOfEratosthenes(n): 
    p = 2
    while (p * p <= n):
        # If prime[p] is not 
        # changed, then it is a prime 
        if (is_prime[p] == True): 
            # Update all multiples of p 
            for i in range(p * p, n + 1, p): 
                is_prime[i] = False
        p += 1
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)

# Function to check if the 
# number can be represented 
# as a power of prime
def power_of_prime(n):
    for i in primes:
        if n % i == 0:
            c = 0
            while n % i == 0:
                n//= i
                c += 1
            if n == 1:
                return (i, c)
            else:
                return (-1, 1)
    
    return (-1, 1)  # If no prime factor found, return -1

# Driver Code         
if __name__ == "__main__":
    n = input("Enter a serial number section (or -1 to exit): ")
    while n != "-1":
        n = int(n)
        if n < 1:
            print(-1)
        else:
            # Generate primes up to sqrt(n)
            SieveOfEratosthenes(int(sqrt(n)) + 1)
            
            # Function Call
            num, power = power_of_prime(n)
            if num > 1:
                print(num, "^", power)
            else:
                print(-1)
        n = input("Enter a serial number section (or -1 to exit): ")