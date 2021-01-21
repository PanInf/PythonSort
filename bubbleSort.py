# Function
def bubbleSort(T):
    n = len(T)
    for j in range(n-1, 0, -1):
        for i in range(j):
            if T[i] > T[i+1]:
                T[i], T[i+1] = T[i+1], T[i]


#Example
from random import randint
X = [randint(1,100) for i in range(20)]
print(X)
bubbleSort(X)
print(X)

