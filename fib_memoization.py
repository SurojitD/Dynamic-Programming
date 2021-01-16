# Implementation of Fibonacci using memoization
# Memoization using Dictionary


f_index = int(input("Enter the index of fibonacci: "))

memo = {}


def fib(n):

    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    else:
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]


print("The value of fibonacci is: ", fib(f_index))


