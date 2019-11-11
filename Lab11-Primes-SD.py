#Lab11-Primes-SD.py
#Stephen Davies
#program to determine if a number is prime

import math

def main():
    n = eval(input("Enter a positive integer, or a non-positive value to quit: "))
    #user inputs intial number to check if its prime
    while prime(n):
        if n == 1:
            print(n, "is not a prime number")
        elif n > 2 and n % 2 == 0:
            print(n, "is not a prime number")
        else:
            print(n, "is a prime number")
        n = eval(input("Enter a positive integer, or a non-positive value to quit: "))
        #evaluates if number is prime or not
        #end if-elif-else
    #end while
#end main

def prime(n):
    if n > 0:
        return True
    else:
        return False
    #determines if number is greater than 0 to put into while loop
    #end if-else
#end prime

main()