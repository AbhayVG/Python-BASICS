def linearsearch(L, v):
    found = False
    for i in range(len(L)):
        if L[i] == v:
            found = True
    return found

a = [5, 4, 3, 2, 1]
print(linearsearch(a, 3))