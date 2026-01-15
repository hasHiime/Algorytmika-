def horner(tab, x):
    wynik = 0
    for i in tab:
        wynik = wynik*x + i
    return wynik

def main():
    a = int(input("Podaj stopien wielomianu: "))

    tab = []

    for i in range(a, -1, -1):
        tab.append(int(input(f"Podaj wspolczynnik stojacy przy potedze {i}: ")))

    x = int(input("Podaj argument: "))

    print(f"W({ x }) = {horner(tab, x)}")

if __name__ == "__main__":
    main()
