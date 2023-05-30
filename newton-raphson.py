
fx = lambda x: x**3 + 4*(x**2) -10
dfx = lambda x: 3*(x**2)+8*x

x0 = 2
error = 0.0001
xi = x0
tramo = abs(2*error)
i=0


while (tramo>=error):
    
    xnuevo=  xi -  fx(xi)/dfx(xi)
    tramo = abs(xnuevo-xi)
    xi = xnuevo
    print('Iteracion: ',i+1)    
    print('Xnuevo: ',xnuevo)
    print('Tramo: ',tramo)
    print('\n')
    
    
    i+=1
print('El número de iteraciones fue: ',i)
