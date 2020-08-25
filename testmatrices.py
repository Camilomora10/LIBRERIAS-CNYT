import unittest
import math
from vectores_matrices import suma_vectoresr2, inverso_aditivo_r2, multi_escalar_r2,suma_matrices,inversa_matriz
from vectores_matrices import multi_escalar_matriz,transpuesta_matriz_vec,conjugada_matriz_vec,adjunta_mat_vec
from vectores_matrices import producto_matrices,accion_matriz,producto_interno,norma_vector,distance_vectores
from vectores_matrices import matriz_unitaria, matriz_hermitania,producto_tensor

#Numeros Complejos
a = [ 1,3 ]
b = [ 2,4 ]
c = [ 6,5 ]
d = [ 4,9 ]

class TestLibComplex(unittest.TestCase):

    def testsumaVect(self):
        self.assertEqual(suma_vectoresr2([a, b], [a, b]), [[2, 6], [4, 8]])
        self.assertEqual(suma_vectoresr2([a, c], [c, b]),[[7, 8], [8, 9]])

    def testinverso_aditivo(self):
        self.assertEqual(inverso_aditivo_r2([a, c]), [[-1, -3], [-6, -5]])
        self.assertEqual(inverso_aditivo_r2([b, a]), [[-2, -4], [-1, -3]])

    def testmulti_escalar(self):
        self.assertEqual(multi_escalar_r2([a, b], b),[[-10, 10], [-12, 16]])
        self.assertEqual(multi_escalar_r2([b, c], c),[[-8, 34], [11, 60]])

    def testsuma_matrices(self):
        self.assertEqual(suma_matrices([[a, a], [b, b]],[[b, a], [a, b]]), [[[3, 7], [2, 6]], [[3, 7], [4, 8]]])
        self.assertEqual(suma_matrices([[c, a], [a, b]],[[b, c], [b, b]]), [[[8, 9], [7, 8]], [[3, 7], [4, 8]]])

    def testInversa_matriz(self):
        self.assertEqual(inversa_matriz([[a], [b], [c]]),[[[-1, -3]], [[-2, -4]], [[-6, -5]]])
        self.assertEqual(inversa_matriz([[a, a, c], [c, b, a], [d, c, b]]),[[[-1, -3], [-1, -3], [-6, -5]], [[-6, -5], [-2, -4], [-1, -3]],
                          [[-4, -9], [-6, -5], [-2, -4]]])

    def testmulti_escalar_matriz(self):
        self.assertEqual(multi_escalar_matriz(d, [[c, a], [a, d]]), [[[-21, 74], [-23, 21]], [[-23, 21], [-65, 72]]])
        self.assertEqual(multi_escalar_matriz(c, [[a, a], [b, b]]),[[[-9, 23], [-9, 23]], [[-8, 34], [-8, 34]]])

    def testtranspuesta_matriz_vec(self):
        self.assertEqual(transpuesta_matriz_vec([[b, a, a], [a, b, a]]),[[[2, 4], [1, 3]], [[1, 3], [2, 4]], [[1, 3], [1, 3]]])
        self.assertEqual(transpuesta_matriz_vec([[a, b, c], [c, b, a]]),[[[1, 3], [6, 5]], [[2, 4], [2, 4]], [[6, 5], [1, 3]]])

    def testconjugada_matriz_vec(self):
        self.assertEqual(conjugada_matriz_vec([[b, a, c], [c, b, d]]),[[[2, -4], [1, -3], [6, -5]], [[6, -5], [2, -4], [4, -9]]])
        self.assertEqual(conjugada_matriz_vec([[a, b, c], [c, b, a]]),[[[1, -3], [2, -4], [6, -5]], [[6, -5], [2, -4], [1, -3]]])

    def testadjunta_mat_vec(self):
        self.assertEqual(adjunta_mat_vec([[b, a, a], [a, b, a]]),[[[2, -4], [1, -3]], [[1, -3], [2, -4]], [[1, -3], [1, -3]]])
        self.assertEqual(adjunta_mat_vec([[a, b, c], [c, b, a]]),[[[1, -3], [6, -5]], [[2, -4], [2, -4]], [[6, -5], [1, -3]]])

    def testproducto_matrices(self):
        self.assertEqual(producto_matrices([[a, a], [b, b]], [[b, a], [a, b]]),[[[-18, 16], [-18, 16]], [[-22, 26], [-22, 26]]])
        self.assertEqual(producto_matrices([[a, a, b], [b, b, a]], [[b, a], [a, b], [b, b]]),[[[-30, 32], [-30, 32]], [[-32, 36], [-32, 36]]])

    def testaccion_matriz(self):
        a = [1, 4]
        b = [4, 0]
        c = [7, -1]
        d = [0, 1]
        e = [5, 6]
        self.assertEqual(accion_matriz([[a, c, d], [b, c, b], [d, b, e]], [e, d, c]),[[-17, 40], [49, 27], [35, 46]])

    def testproducto_interno(self):
        a, b = [3, 0], [-6, 0]
        c = [2, 0]
        self.assertEqual(producto_interno([a, b, c], [a, b, c])[0], 49)

    def testnorma_vector(self):
        a, b = [3, 0], [-6, 0]
        c = [2, 0]
        self.assertEqual(norma_vector([a, b, c]), math.sqrt(49))

    def testdistance_vectores(self):
        a, b = [3, 0], [1, 0]
        c, d = [2, 0], [-1, 0]
        self.assertEqual(distance_vectores([a, b, c], [c, c, d]), math.sqrt(11))

    def testmatriz_unitaria(self):
        a, b = [1, 0], [0, 0]
        c = [0, 1]
        self.assertEqual(matriz_unitaria([[c, b], [b, c]]),True)
        self.assertEqual(matriz_unitaria([[a, b], [b, a]]),True)

    def testmatriz_hermitania(self):
        a = [7, 0]
        b = [6, 5]
        c = [6, -5]
        d = [-3, 0]
        e, f = [1, 0], [0, 0]
        self.assertEqual(matriz_hermitania([[a, b], [c, d]]),True)
        self.assertEqual(matriz_hermitania([[e, f], [f, e]]),True)

    def testproducto_tensor(self):
        matrix1 = [[2, 0], [3, 0]]
        matrix2 = [[4, 0], [6, 0], [3, 0]]
        self.assertEqual(producto_tensor(matrix1, matrix2),[[8, 0], [12, 0], [6, 0], [12, 0], [18, 0], [9, 0]])
        A = [[[1, 0], [2, 0]], [[0, 0], [1, 0]]]
        B = [[[3, 0], [2, 0]], [[-1, 0], [0, 0]]]
        C = [[[6, 0], [5, 0]], [[3, 0], [2, 0]]]
        aXb = producto_tensor(A, B)
        bXc = producto_tensor(B, C)
        self.assertEqual(producto_tensor(A, bXc),
                         [[[18, 0], [15, 0], [12, 0], [10, 0], [36, 0], [30, 0], [24, 0], [20, 0]],
                          [[9, 0], [6, 0], [6, 0], [4, 0], [18, 0], [12, 0], [12, 0], [8, 0]],
                          [[-6, 0], [-5, 0], [0, 0], [0, 0], [-12, 0], [-10, 0], [0, 0], [0, 0]],
                          [[-3, 0], [-2, 0], [0, 0], [0, 0], [-6, 0], [-4, 0], [0, 0], [0, 0]],
                          [[0, 0], [0, 0], [0, 0], [0, 0], [18, 0], [15, 0], [12, 0], [10, 0]],
                          [[0, 0], [0, 0], [0, 0], [0, 0], [9, 0], [6, 0], [6, 0], [4, 0]],
                          [[0, 0], [0, 0], [0, 0], [0, 0], [-6, 0], [-5, 0], [0, 0], [0, 0]],
                          [[0, 0], [0, 0], [0, 0], [0, 0], [-3, 0], [-2, 0], [0, 0], [0, 0]]])

if __name__ == 'main':
    unittest.main()
# Author : Yesid Camilo Mora Barbosa