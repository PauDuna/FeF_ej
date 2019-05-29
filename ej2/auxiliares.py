def esPrimo(n):
    noEsPrimo = False
    for i in range (2,n):
        if n % i == 0:
            noEsPrimo = True
            break
    esPrimo = not noEsPrimo
    return esPrimo