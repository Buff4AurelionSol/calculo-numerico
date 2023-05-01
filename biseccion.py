from math import *

cotaInferior = int(input("Ingrese la Cota Inferior: "))
cotaSuperior = int(input("ingrese la Cota Superior: "))
errorRelativo = float(input("Ingrese el Error relativo: "))
numeroIteraciones = int(input("Ingrese el número de iteraciones: "))

def f(x):
    return sin(x)-exp(-x)


Ea = 100 
I = 0
M_Actual = 0 #Punto Medio Actual.
M_Previa = 0 #Punto Medio Previo.

while(I<numeroIteraciones and Ea >errorRelativo):
    M_Previa = M_Actual
    M_Actual = (cotaInferior+cotaSuperior)/2

    if(f(M_Actual)*f(cotaSuperior)<0):
        cotaInferior = M_Actual
    else:
        cotaSuperior = M_Actual
    
    if(I>0):
        Ea = abs((M_Actual - M_Previa)/M_Actual)

    I+= 1 

print("El punto medio Actual es de: ",M_Actual)
print("El error absoluto es: ",Ea)
print("El número de iteraciones fue: ",I)