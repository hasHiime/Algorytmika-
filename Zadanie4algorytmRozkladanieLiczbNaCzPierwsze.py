n = int(input("Wprowadź liczbę: "))

def rozkladLiczb(n):
    k = 2
    while n > 1:
        while n % k == 0:
            print(k)
            n = n / k
            print(n)
        k += 1

rozkladLiczb(n)