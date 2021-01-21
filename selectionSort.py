# Function
def selectionSort(T):
    n = len(T)
    for i in range(n-1):
        k = i
        for j in range(i+1,n):
            if T[j] < T[k]:
                k = j
        T[k], T[i] = T[i], T[k]


#Example
from random import randint
X = [randint(1,100) for i in range(20)]
print(X)
selectionSort(X)
print(X)

