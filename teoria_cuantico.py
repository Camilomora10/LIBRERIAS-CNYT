
## Observables del libro, Computación cuántica para científicos informáticos

from sistema_clasico_quantum import
import numpy as np
import math
from vectores_matrices import producto_interno,accion_matriz,adjunta_mat_vec,multi_escalar_matriz,producto_matrices,matriz_hermitania,norma_vector,inversa_aditiva_matriz
from vectores_matrices import suma_matrices,matriz_unitaria
from libreriaComplejos import modulo_complejos,angulo_complejos

def prob_particula(ket, posicion):
    norma_ket = (norma_vector(ket))**2
    norma_posicion = None
    for i in range(len(ket)):
        norma_posicion = (norma_vector(ket[i])[0])**2
    norma_posicion = (norma_vector(ket[posicion])[0])**2
    return posicion, norma_posicion/norma_ket
------------------------------------------------------------------------------------------------------------------------
def media(observable, ket):
    if matriz_hermitania(observable):
        bra_ket = bra(ket)
        res1 = accion_matriz(observable, ket)
        res2 = producto_interno(res1, bra_ket)
        return res2
    else:
        return "El observables no es hermitiano"

------------------------------------------------------------------------------------------------------------------------
def varianza(observable, ket):
    if matriz_hermitania(observable):
        bra_ket = bra(ket)
        aux = media(observable, ket)
        identidad_Mu =  [[(0, 0) for j in range(len(observable[0]))] for i in range(len(observable))]
        for i in range(len(observable)):
            for j in range(len(observable[i])):
                if i==j:
                    identidad_Mu[i][j] = inversa_aditiva_matriz(aux)
        identidad_Mu = suma_matrices(identidad_Mu, observable)
        observablealcudrado = producto_matrices(identidad_Mu, identidad_Mu)
        res1 = accion_matriz(observablealcudrado, ket)
        res2 = producto_interno(res1, bra_ket)
        return res2
    else:
        return "El observables no es hermitiano"

------------------------------------------------------------------------------------------------------------------------
def valores_vectores(observable):
    valores, vectores = np.linalg.eig(observable)
    lista_valores = []
    lista_vectores = []
    for index in range(len(valores)):
        lista_valores += [[valores[index], valores[index]]]
    for index in range(len(vectores)):
        vector = []
        for index_2 in range(len(vectores[0])):
            vector += [[vectores[index][index_2], vectores[index][index_2]]]
        lista_vectores += [vector]
    return lista_valores, lista_vectores
------------------------------------------------------------------------------------------------------------------------

def probabilidades_vectores(inicial, observable, posicion):
    vectores = valores_vectores(observable)[1]
    return norma_vector([[inicial, vectores[posicion]]])

------------------------------------------------------------------------------------------------------------------------
def sistema_dinamico(matriz,vector, clicks):
    if matriz_unitaria(matriz):
        for i in range(clicks):
            vector = accion_matriz(matriz, vector)
        return vector
    else:
        return "la matriz no es unitaria"

------------------------------------------------------------------------------------------------------------------------
def longitud(vect):
    """
    Calcula la longitud de un vector dado
    """
    acu = 0
    for i in range(len(vect)):
        acu += (module(vect[i]))**2
    return math.sqrt(acu)
------------------------------------------------------------------------------------------------------------------------

def normalizar(vect):
    """
    Normaliza un vector dado
    """
    length = longitud(vect)
    for i in range(len(vect)):
        vect[i] = [vect[i][0]/length,vect[i][1]/length]
    return vect
------------------------------------------------------------------------------------------------------------------------

def bra(vect):
    """
    Devuelve el bra de un vector dado
    """
    return adjunta_mat_vec(vect)
------------------------------------------------------------------------------------------------------------------------

def transicion(vect1, vect2):
    """
    Nos dice cuanto es la transicion de un vector a otro
    """
    ##(rvs hc)  el bra a vect1
    return producto_interno(vect1,vect2)
------------------------------------------------------------------------------------------------------------------------
def Exc441():
    """
    Verify that the next matrix are unitary, theri preoduct is also unitary
    """
    aux1 = [[(0, 0), (1, 0)], [(1, 0), (0, 0)]]
    aux2 = [[((2**(1/2))/2, 0), ((2**(1/2))/2, 0)], [((2**(1/2))/2, 0), (-(2**(1/2))/2, 0)]]
    if matriz_unitaria(aux1) and matriz_unitaria(aux2):
        return matriz_unitaria(producto_matrices(aux1,aux2))

------------------------------------------------------------------------------------------------------------------------
def Exc442():
    """
    with example 3.3.2 change the unitary map and answer Determine the state of the system after three time steps.
    What is the chance of the quantum ball to be found at point 3?
    """
    print(sistema_dinamico([[(0, 0), (1/(2**(1/2)), 0), (1/(2**(1/2)), 0), (0, 0)],
                        [(1/(2**(1/2)), 0), (0, 0), (0, 0), (-1/(2**(1/2)), 0)],
                        [(1 / (2 ** (1 / 2)), 0), (0, 0), (0, 0), (1 / (2 ** (1 / 2)), 0)],
                        [(0, 0), (-1/(2**(1/2)), 0), (1/(2**(1/2)), 0), (0, 0)]],
                        [(1,0), (0,0), (0,0), (0,0)], 3))
    print(sistema_dinamico([[(0, 0), (1 / (2 ** (1 / 2)), 0), (1 / (2 ** (1 / 2)), 0), (0, 0)],
                   [(0, 1 / (2 ** (1 / 2))), (0, 0), (0, 0), (1 / (2 ** (1 / 2)), 0)],
                   [(1 / (2 ** (1 / 2)), 0), (0, 0), (0, 0), (0, 1 / (2 ** (1 / 2)))],
                   [(0, 0), (1 / (2 ** (1 / 2)), 0), (-1 / (2 ** (1 / 2)), 0), (0, 0)]],
                  [(1, 0), (0, 0), (0, 0), (0, 0)], 3))
------------------------------------------------------------------------------------------------------------------------

def Exc431():
    v1 = [[(1, 0)], [(0, 0)]]
    observable_x = [[(0, 0), (1, 0)], [(1, 0), (0, 0)]]
    vr = Spaces.m_action(observable_x, v1)
    valores_x, vectores_x = valores_vectores(observable_x)

    print("El resultado de la observacion es: ", vr)
    print("Los valores porpios del observable son: ", valores_x)
    print("Sus vectores poropios son: ", vectores_x)
    print(" por tanto el sistema colapsa en un vector poropio")
------------------------------------------------------------------------------------------------------------------------
