def quicksortLomuto(T, lewy, prawy):
    pivot = T[prawy]
    i = lewy
    for k in range(lewy, prawy):
        if T[k] <= pivot:
            T[i], T[k] = T[k], T[i]
            i = i + 1
    
    T[i], T[prawy] = T[prawy], T[i]

    if lewy<i-1:
        quicksortLomuto(T, lewy, i-1)
    if prawy>i+1:
        quicksortLomuto(T, i+1, prawy)

# example
from random import randint
T = [randint(1, 100) for i in range(20)]
print(T)
quicksortLomuto(T, 0, len(T)-1)
print(T)
