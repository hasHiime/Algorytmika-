def rozkladLiczb(n):
        zbior = []
        k = 2
        while n > 1:
            while n % k == 0:
                zbior.append(k)
                n = n / k
            k += 1
        return zbior

def main():
    n = int(input("Wprowadź liczbę: "))

    wynik = rozkladLiczb(n)
    print("Czynniki pierwsze liczby",n,":", *wynik)

if __name__ =="__main__":
    main()
