def f(x):
    return x*(x*(x-3)+2)-6


# def PolowieniePrzedzialow(a, b, epsilon):
#     srodek = (a+b)/2
#     if f(a) == 0.0:
#         return a
#     elif f(b) == 0.0:
#         return b
#     elif b-a <= epsilon:
#         return srodek
#     elif f(a)*f(srodek) < 0:
#         return PolowieniePrzedzialow(a, srodek, epsilon)
#     return PolowieniePrzedzialow(srodek, b, epsilon)

def PolowieniePrzedzialow(a, b, epsilon):
    if f(a) == 0.0:
        return a
    elif f(b) == 0.0:
        return b
    while b-a > epsilon:
        srodek = (a+b)/2
        if f(srodek) == 0:
            return srodek
        elif f(a)*f(srodek) < 0:
            b = srodek
        else:
            a = srodek
    return (a+b)/2        

def main():
    a = -10
    b = 10
    epsilon = 0.00001
    wynik = PolowieniePrzedzialow(a, b, epsilon)
    print(f"Znalezione miejsce zerowe wynosi: {wynik:.5f}")


if __name__ == "__main__":
    main()
