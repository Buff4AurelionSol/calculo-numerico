from math import *


#DEIVIS JOEL GUILLEN RODRÍGUEZ
#CÉDULA: 27 650 675 
#ALGORITMO DE NEWTON-RAPHSON

def f(x):
    return sin(x)-exp(-x)

def df(x):
    return cos(x)+exp(-x)


def newton_raphson(xo, error):
    xi = xo
    tramo = abs(2*error)
    i=0

    while(tramo>=error):
        xnuevo = xi -f(xi)/df(xi)
        tramo = abs(xnuevo-xi)
        xi = xnuevo
        print("Iteración: ", i+1)
        print("Xnuevo: ",xnuevo)
        print('Tramo: ', tramo)
        print('\n')
        i+=1
    print("Tomó:",i,"iteraciones.")
    return xnuevo

