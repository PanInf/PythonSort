# Function
def countingSort(T, m):
    P = []
    for i in range(m):
        P.append(0)
    for i in T:
        P[i] += 1
    k = 0
    for i in range(m):
        for j in range(0, P[i]):
            T[k] = i
            k += 1

# Example
# Zmienna na potrzeby algorytmu
m = 100
from random import randint
X = [randint(1,m-1) for i in range(20)]
print(X)
countingSort(X, m)
print(X)
