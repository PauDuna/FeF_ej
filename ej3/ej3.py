import collatz
import time

start = time.time()

secuencia2 = [] #sec de collatz mas larga hasta el momento
numero = 1000000
b = list(range(2,numero+1))

for i in b:
    a = collatz.collatz (i)
    if len(a) > len(secuencia2):
        secuencia2.clear()
        secuencia2 = a
        c = set(secuencia2) #hace lo que le digo abajo mas rapido si estan ordenados
        b = [j for j in b if j not in c] #que no pruebe los que estan en la sec ya encontrada, porque la sec a la cual dan lugar va a ser menor que la actual

print("El numero inicial menor a {} que produce la sucesion mas larga es: {}".format(numero,secuencia2[0]))
end = time.time()
print("El programa tardo {} segundos en ejecutarse." .format(end-start))
