def obliczanie(liczba):
        tablica = []
        while liczba != 0:
            tablica.append(liczba % 2)
            liczba = liczba //= 2
        return tablica


def main():
    liczba = int(input("Podaj liczbę: "))
    wynik = obliczanie(liczba)

    print("Liczba", liczba, "po zamianie na postać binarną:", *wynik[::-1])

if __name__=="__main__":
    main()
