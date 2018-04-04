import numpy as np
import matplotlib.pyplot
import time
#Funcion que retorna el n-esimo numero de la serie de fibonacci
def fibonacci(N):
    #Casos base para 0 y 1
    if N==0:
        return 0
    if(N==1):
        return 1
    #Caso recursivo
    else:
        #segun la formula de fibonacci se calcula recursivamente
        return fibonacci(N-1)+fibonacci(N-2)
#retorna el tiempo que le toma calcular el numero n-esimo de fibonacci
def get_time(N):
    #inicia el cronometro
    t0 = time.time()
    # SOME CODE THAT TAKES TIME
    #corre fibonacci para N
    fibonacci(N)
    #termina de calcular n-esimo termino y para el cronometro
    t1 = time.time()-t0
    return t1

N=35
for i in range(N+1):
    print i,get_time(i)
