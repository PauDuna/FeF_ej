from auxiliares import esPrimo
import time

start = time.time()

def divisoresPrimosFx(numero):
    divisoresPrimos = [1] #arranco con 1 para poder comparar
    for i in range(2, numero + 1):
        if numero < divisoresPrimos[-1]: #si es menor al mayor que encontró, no me sirve
            break
        if numero % i == 0:
            if esPrimo(i):
                divisoresPrimos.append(i)
                numero = numero / i
    return(divisoresPrimos)

numero = int(600851475143)
listaDivPrimos = divisoresPrimosFx(numero) #solo los que sean mayores a los que va encontrando
divPrimoMasGrande = listaDivPrimos[-1]
print("El divisor primo mas grande del numero {} es: {}." .format(numero,divPrimoMasGrande))

end = time.time()
print("El programa tardo {} segundos en ejecutarse." .format(end-start))