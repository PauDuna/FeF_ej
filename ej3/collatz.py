def collatz (num):
    secuencia = [num]
    x = secuencia [-1]
    for x in secuencia:
        if x % 2 == 0:
            x = x / 2
            secuencia.append(int(x))
        elif x == 1:
            return (secuencia)
            break
        else:
            x = 3 * x + 1
            secuencia.append(int(x))
