import unittest
import libreriaComplejos
import math

class unit_calculadora(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(libreriaComplejos.suma_complejos(6, 10, -15, -5), (-9 , 5 ))
        self.assertEqual(libreriaComplejos.suma_complejos(2, 11, -14, -4), (-12, 7 ))
        self.assertEqual(libreriaComplejos.suma_complejos(3, 4 , -2 , -1), (1  , 3 ))
        self.assertEqual(libreriaComplejos.suma_complejos(7, 10, 12 , -5), (19 , 5 ))
        self.assertEqual(libreriaComplejos.suma_complejos(6, -2, 11 , -3), (17 , -5))
        self.assertEqual(libreriaComplejos.suma_complejos(5, -5, 10 , -4), (15 , -9))
        self.assertEqual(libreriaComplejos.suma_complejos(3, -1, 14 , -5), (17 , -6))
        self.assertEqual(libreriaComplejos.suma_complejos(1, -3, 15 , -2), (16 , -5))

    def test_mult(self):
        self.assertEqual(libreriaComplejos.producto_complejos(-1, 2, 1, -22), (43,24)  )
        self.assertEqual(libreriaComplejos.producto_complejos(-6, 4, 4, -11), (20,82)  )
        self.assertEqual(libreriaComplejos.producto_complejos(-2, 7, 5, -15), (95,65)  )
        self.assertEqual(libreriaComplejos.producto_complejos(-4, 9, 8, -35), (283,212))
        self.assertEqual(libreriaComplejos.producto_complejos(6, 10, 15, -5), (140,120))
        self.assertEqual(libreriaComplejos.producto_complejos(6, 11, 11, -6), (132,85) )
        self.assertEqual(libreriaComplejos.producto_complejos(6, 13, 12, -5), (137,126))
        self.assertEqual(libreriaComplejos.producto_complejos(6, 12, 13, -3), (114,138))

    def test_resta(self):
        self.assertEqual(libreriaComplejos.resta_complejos(6, 10, -15, -5), (21,15))
        self.assertEqual(libreriaComplejos.resta_complejos(2, 11, -14, -4), (16,15))
        self.assertEqual(libreriaComplejos.resta_complejos(3, 4 , -2 , -1), (5,5))
        self.assertEqual(libreriaComplejos.resta_complejos(7, 10, 12 , -5), (-5,15))
        self.assertEqual(libreriaComplejos.resta_complejos(6, -2, 11 , -3), (-5,1))
        self.assertEqual(libreriaComplejos.resta_complejos(5, -5, 10 , -4), (-5,-1))
        self.assertEqual(libreriaComplejos.resta_complejos(3, -1, 14 , -5), (-11,4))
        self.assertEqual(libreriaComplejos.resta_complejos(1, -3, 15 , -2), (-14,-1))

    def test_division(self):
        self.assertEqual(libreriaComplejos.division_complejos(6, 10, -15, -5), (-0.56,-0.48))
        self.assertEqual(libreriaComplejos.division_complejos(2, 11, -14, -4), (-0.33962264150943394,-0.6886792452830188))
        self.assertEqual(libreriaComplejos.division_complejos(3, 4 , -2 , -1), (-2.0,-1.0))
        self.assertEqual(libreriaComplejos.division_complejos(7, 10, 12 , -5), (0.20118343195266272,0.9171597633136095))
        self.assertEqual(libreriaComplejos.division_complejos(6, -2, 11 , -3), (0.5538461538461539,-0.03076923076923077))
        self.assertEqual(libreriaComplejos.division_complejos(5, -5, 10 , -4), (0.603448275862069,-0.25862068965517243))
        self.assertEqual(libreriaComplejos.division_complejos(3, -1, 14 , -5), (0.21266968325791855,0.004524886877828055))
        self.assertEqual(libreriaComplejos.division_complejos(1, -3, 15 , -2), (0.09170305676855896,-0.18777292576419213))

    def test_modulo(self):
        self.assertEqual(libreriaComplejos.modulo_complejos(-3, 4), 5.0)
        self.assertEqual(libreriaComplejos.modulo_complejos(-2, 4), 4.47213595499958)
        self.assertEqual(libreriaComplejos.modulo_complejos(3, 12), 12.36931687685298)
        self.assertEqual(libreriaComplejos.modulo_complejos(6, -4), 7.211102550927978)
        self.assertEqual(libreriaComplejos.modulo_complejos(4, -9), 9.848857801796104)
        self.assertEqual(libreriaComplejos.modulo_complejos(7, -5), 8.602325267042627)
        self.assertEqual(libreriaComplejos.modulo_complejos(9, 41), 41.97618372363071)
        self.assertEqual(libreriaComplejos.modulo_complejos(1, -4), 4.123105625617661)

    def test_angulo(self):
        self.assertEqual(libreriaComplejos.angulo_complejos(-6, 15), 111.80140948635182)
        self.assertEqual(libreriaComplejos.angulo_complejos(6, -15), 291.8014094863518)
        self.assertEqual(libreriaComplejos.angulo_complejos(6, 15), 68.19859051364818)
        self.assertEqual(libreriaComplejos.angulo_complejos(-6, -15), 248.19859051364818)
        self.assertEqual(libreriaComplejos.angulo_complejos(-6, -15), 248.19859051364818)
        self.assertEqual(libreriaComplejos.angulo_complejos(-6, -15), 248.19859051364818)
        self.assertEqual(libreriaComplejos.angulo_complejos(-6, -15), 248.19859051364818)
        self.assertEqual(libreriaComplejos.angulo_complejos(-6, -15), 248.19859051364818)
        self.assertEqual(libreriaComplejos.angulo_complejos(-6, -15), 248.19859051364818)

    def test_conjugado(self):
        self.assertEqual(libreriaComplejos.conjugado_complejos(-45, 3), (-45, -3))
        self.assertEqual(libreriaComplejos.conjugado_complejos(-23, 5), (-23, -5))
        self.assertEqual(libreriaComplejos.conjugado_complejos(-40, 6), (-40, -6))
        self.assertEqual(libreriaComplejos.conjugado_complejos(-15, 8), (-15, -8))
        self.assertEqual(libreriaComplejos.conjugado_complejos(-46, -2), (-46, 8))
        self.assertEqual(libreriaComplejos.conjugado_complejos(-25, -1), (-25, 1))
        self.assertEqual(libreriaComplejos.conjugado_complejos(-95, -8), (-95, 8))
        self.assertEqual(libreriaComplejos.conjugado_complejos(-42, -9), (-42, 9))

    def test_polarcart(self):
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos(2, 32), (1.6684467210130205,1.1028533624833812))
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos(1, 34), (-0.8485702747846052,0.5290826861200238))
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos(2, 22), (-1.9999216527892743,-0.017702618580807752))
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos(5, 67), (-2.5888489989475256,-4.277599894876611))
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos(2, 0.22), (1.951794898661211,0.43645924616173865))
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos(8, 0.55), (6.8201961764760455,4.181497831445274))
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos(9, 0.44), (8.14276496897967,3.8334551855939965))
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos(2, 0.33), (1.892084687056774,0.6480860567897367))

    def test_cartepoalr(self):
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos(2, 22), (22.090722034374522,1.4801364395941514))
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos(3, 12), (12.36931687685298,1.3258176636680326))
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos(4, 3), (5.0,0.6435011087932844))
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos(2, 3), (3.605551275463989,0.982793723247329))
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos(6, 3), (6.708203932499369,0.4636476090008061))
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos(1, 4), (4.123105625617661,1.3258176636680326))
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos(3, 9), (9.486832980505138,1.2490457723982544))
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos(2, 5), (5.385164807134504,1.1902899496825317))

unittest.main()