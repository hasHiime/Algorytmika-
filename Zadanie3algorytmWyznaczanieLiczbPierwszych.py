import math
n = int(input("Jaką liczbę chcesz sprawdzić: "))


def czylpierwsza(n):
    if n <= 2:
        return "Liczba nie zdolna do liczenia"
    for i in range(2, round(math.sqrt(n)) + 1):
        print(i)
        if n % i == 0:
            return (n, "Nie jest liczbą pierwszą")
    return (n, "Jest liczbą pierwszą")

print(czylpierwsza(n))