from math import *

#DEIVIS JOEL GUILLEN RODRÍGUEZ
#CÉDULA: 27 650 675 
#ALGORITMOS DE INTEGRACIÓN NUMERICA.
# SUMAS DE RIEMAN Y MÉTODO DEL TRAPECIO





def f(x):
    return x*sin(x** 2 + 1 )


def suma_rieman(a,b,n):
    h = (b-a)/(n)
    i =0
    suma_area = 0
    aux = a

    

    print("-----SUMAS DE RIEMAN-----")
    while i <= n:
       print("A",i,"= ",h*(f(aux)))
       suma_area += h*(f(aux))
       i = i + 1
       aux += h 
    
    return suma_area


def metodo_trapecio(a,b,n):
    h = (b-a)/(n)
    i = 0
    trapecio = 0
    aux = a
    aux2 = a+h

    while i < n:

        trapecio += (h)*((f(aux))+(f(aux2)))/(2)
        print("A",i,"=", trapecio)
        aux=aux2
        aux2+= h
        i = i +1 
        
    return trapecio



print("La solución es:",suma_rieman(1,2,3))
print("----------------------------------------------------------------------")

print("Método del trapecio es:",metodo_trapecio(1,2,3))
print("----------------------------------------------------------------------")
