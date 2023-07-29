from math import *
from tabulate import tabulate

#DEIVIS JOEL GUILLEN RODRÍGUEZ
#CÉDULA: 27 650 675 
#ALGORITMO DEl MÉTODO DE EULER





def EDO(t1,y1):
    t = t1 
    y = y1 

    return t/y1

def metodo_euler(t1, y1, h, n):

    y_actual = y1
    y_siguiente = 0
    ti = t1
    i= 0

    # Crear la lista de diccionarios
    tabla = []

    while(i<=n):
        y_siguiente = (y_actual + h *(EDO(ti, y_actual)))
        fila = {"i":i, "ti":ti, "yi":y_actual, "yi+1":y_siguiente}
        tabla.append(fila)
        ti += h
        y_actual = y_siguiente 
        i += 1 

    # Imprimir la tabla
    print(tabulate(tabla, headers="keys", tablefmt="fancy_grid"))

    return y_actual


