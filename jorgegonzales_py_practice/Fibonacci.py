# Fibonacci Sequence
#
# If you do not know about the Fibonacci Sequence, read about it here.
#
#     Define a function that allows the user to find the value of the nth term in the sequence.
#     To make sure you've written your function correctly, test the first 10 numbers of the sequence.
#     You can assume either that the first two terms are 0 and 1 or that they are both 1.
#     There are two methods you can employ to solve the problem. One way is to solve it using a loop and the other way is to use recursion.
#     Try implementing a solution using both methods.
#
from functools import reduce


def recursive_fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return recursive_fib(n - 1) + recursive_fib(n - 2)


def iterative_fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        fib = 1
        mylist = [1, 0]
        while n > 2:
            mylist[1] = fib
            fib += mylist[0]
            mylist[0] = mylist[1]
            n -= 1
        return fib

seq_number = int(input("Enter number of desired Fib number\n"))
print("recursive function result: ", recursive_fib(seq_number),"\niterative function result: ", iterative_fib(seq_number), sep="")