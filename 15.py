from random import randint

def printMatrix(n):
    for i in range(n):
        for j in range(n):
            print(randint(0,1),end=" ")
        print("")

n=int(input("Enter n - "))
printMatrix(n)
