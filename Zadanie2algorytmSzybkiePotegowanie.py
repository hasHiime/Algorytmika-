a = int(input("Podaj liczbę: "))
n = int(input("Podaj potęge: "))

def potegowanie(a, n):
    wynik = 1
    while n > 0:
        if n % 2 == 1:
            wynik = wynik * a
        a = a * a
        n = n // 2
        print("N:", n)
    return wynik
    
print("Wynik potęgi to: ", potegowanie(a, n))