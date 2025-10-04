tab = [1, 2, 4, 5, 6, 12, 15, 21, 32, 36, 40, 54, 56, 65, 75]

search = int(input("Jakiej liczby szukasz: "))
right = len(tab)
left = 0
print(right, left)

def binary_search(right, left, tab, search):
    while left < right:
        middle = (left + right) // 2
        if search == tab[middle]:
            return middle
        elif search < tab[middle]:
            right = middle - 1
            print("Mniejsza", left, right, middle)
        else:
            left = middle + 1
            print("Większa", left, right, middle)
    return -1
    
filtered = binary_search(right, left, tab, search)

if filtered != -1:
    print("Szukana liczba", search, "znajduę się w tabeli na pozycji: ", filtered + 1)
else: 
    print("Nie znaleziono liczby")