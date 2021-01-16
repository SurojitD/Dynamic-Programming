# Implementation of gridTraveler using memoization

rows = int(input("Enter the number of rows"))
columns = int(input("Enter the number of columns"))

memo = {}


def gridTraveler(m,n):
    if (m,n) in memo:
        return memo[(m,n)]
    if m == 0 or n == 0:
        return 0
    elif m == 1 and n == 1:
        return 1
    else:
        memo[(m,n)] = gridTraveler(m-1, n) + gridTraveler(m, n-1)
        return memo[(m,n)]


print("The number of ways the traveler can travel through the grid is: ", gridTraveler(rows, columns))
