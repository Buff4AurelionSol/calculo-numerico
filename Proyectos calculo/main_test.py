import unittest
from biseccion import *
from newton_raphson import newton_raphson
from integracion_numerica import suma_rieman
from integracion_numerica import metodo_trapecio
from metodo_euler import metodo_euler


#DEIVIS JOEL GUILLEN RODRÍGUEZ
#CÉDULA: 27 650 675 




class CalculoNumerico(unittest.TestCase):

    def test_biseccion(self):
        print("-----TEST BISECCION-----")
        self.assertEqual(biseccion(0,1,0.02,7),0.5859375)

    def test_newton_raphson(self):
        print("-----TEST NEWTON RAPHSON")
        self.assertEqual(newton_raphson(0.5, 0.02),0.5885294126263548)

    def test_suma_rieman(self):
        print('-----TEST SUMAS DE RIEMAN-----')
        self.assertEqual(suma_rieman(1,2,3), -0.5081046043821824)

    def test_metodo_trapecio(self):
        print('-----TEST METODO DEL TRAPECIO-----')
        self.assertEqual(metodo_trapecio(1,2,3), -0.34001275063208314)
  
    def test_metodo_euler(self):
        print('-----TEST MÉTODO DE EULER-----')
        self.assertEqual(metodo_euler(1, 2, 0.2, 5), 2.77526855383067)

if __name__== '__main__':
    unittest.main()