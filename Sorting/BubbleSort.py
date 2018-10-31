def bubbleSort(L):
    length = len(L)
    if length <= 1:
        return L

    for i in range(length - 1):
        if L[i] > L[i+1]:
            L[i], L[i+1] = L[i+1], L[i]

    L[:length - 1] = bubbleSort(L[:length-1])

    return L


L = [90, 70, 80]
print(bubbleSort(L))