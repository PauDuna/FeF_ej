import time

start = time.time()

n = 1000
suma = 0
for i in range(1,n): #no incluye n
    if i%3 == 0 or i%5 ==0: #es or: no incluye duplicados
        suma+=i #equivalente a suma = suma + i
print("La suma de todos los multiplos de 3 o 5 menores a {} es {}." .format(n,suma))

end = time.time()

print("El programa tardo {} segundos en ejecutarse." .format(end-start))