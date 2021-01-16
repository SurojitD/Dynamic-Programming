# Implementation of Fibonacci without using memoization


n = int(input("Enter the index of fibonacci: "))


def fib(num):
    if num <= 2:
        return 1

    else:
        return fib(num-2) + fib(num-1)


print("The value of fibonacci is: ", fib(n))
