def MergeSort(tab, l, r):
    if r > l:
        m = (l + r) // 2
        MergeSort(tab, l, m)
        MergeSort(tab, m + 1, r)
        Merge(tab, l, m, r)

def Merge(tab, l, m, r):
    lSize = m - l + 1
    rSize = r - m
    tabL = [0] * lSize
    tabR = [0] * rSize
    for x in range(lSize):
        tabL[x] = tab[l + x]
    for y in range(rSize):
        tabR[y] = tab[m+1+y]

    indexL = 0
    indexR = 0
    currIndex = l

    while indexL < lSize and indexR < rSize:
        if tabL[indexL] <= tabR[indexR]:
            tab[currIndex] = tabL[indexL]
            indexL += 1
        else:
            tab[currIndex] = tabR[indexR]
            indexR += 1
        currIndex += 1
    
    while indexL < lSize:
        tab[currIndex] = tabL[indexL]
        indexL += 1
        currIndex +=1
    
    while indexR < rSize:
        tab[currIndex] = tabR[indexR]
        indexR += 1
        currIndex +=1

tab = [70, 36, 86, 71, 22, 71, 89, 77]

print("\nTablica przed posortowaniem:")
for x in tab:
    print(f"{x} | ", end="")
print("\n")

print("Rozpoczynanie sortowania")

MergeSort(tab, 0, len(tab)-1)

print("\nTablica po posortowaniu:")
for x in tab:
    print(f"{x} | ", end="")
print("\n")
