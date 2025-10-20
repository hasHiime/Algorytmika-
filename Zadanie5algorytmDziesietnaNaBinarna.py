liczba = int(input("Podaj liczbę: "))
tablica = []
i = 0

def obliczanie(tablica, i, liczba):
    while liczba != 0:
        tablica.append(liczba % 2)
        liczba = liczba // 2

obliczanie(tablica, i, liczba)

print("Liczba", liczba, "po zamianie na postac binarna:", *tablica[::-1])