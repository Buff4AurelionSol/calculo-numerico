from math import *
#DEIVIS JOEL GUILLEN RODRÍGUEZ
#CÉDULA: 27 650 675 
#ALGORITMO DE BISECCIÓN


def f(x):
    return sin(x)-exp(-x)

def biseccion(cotaInferior, cotaSuperior, error, numeroIteraciones):
    Ea= 100
    i = 0
    M_Actual = 0
    M_Previa = 0

    while(i<numeroIteraciones and Ea >error):
        M_Previa = M_Actual
        M_Actual = (cotaInferior+cotaSuperior)/2

        if(f(M_Actual)*f(cotaSuperior)<0):
            cotaInferior = M_Actual
        else:
            cotaSuperior = M_Actual
        
        if(i>0):
            Ea = abs((M_Actual - M_Previa)/M_Actual)

        i+= 1 
    
    print("El punto medio Actual es de: ",M_Actual)
    print("El error absoluto es: ",Ea)
    print("El número de iteraciones fue: ",i)
    return M_Actual
biseccion(0,1,0.02,7)





