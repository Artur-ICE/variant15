def f(n):
    a = bin(n)[2:]
    b = 0
    for i in range(0, len(a)):
        b += int(a[i])
    b = b % 2
    c = str(a) + str(b)
    d = 0
    for j in range(0, len(c)):
        d = d + int(c[j])
    d = d % 2
    e = int(str(c) + str(d), 2) # не забывай про двойку идиот, мне это стоило 5 минут разбирательств
    return e


for n in range(1, 10000):
    if f(n) > 55:
        print(f(n))
        break






