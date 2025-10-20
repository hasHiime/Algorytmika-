n = int(input("Wprowadź liczbę: "))

zbior = []

def rozkladLiczb(n, zbior):
    k = 2
    while n > 1:
        while n % k == 0:
            zbior.append(k)
            n = n / k
        k += 1

rozkladLiczb(n, zbior)
print("Czynniki pierwsze liczby",n,":", *zbior)