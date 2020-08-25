from libreriaComplejos import suma_complejos, resta_complejos, producto_complejos, conjugado_complejos
import math

def suma_vectoresr2(x:int, y:int, z:int, w:int , a:int, b:int, c:int, d:int)->str:
    suma_x = suma_complejos(x,y,a,b)
    suma_y = suma_complejos(z,w,c,d)
    respuesta = "(" + suma_x + "," + suma_y + ")"
    return respuesta
def suma_vectoresr3(a:int,b:int,c:int,d:int,e:int,f:int,u:int,v:int,w:int,x:int,y:int,z:int) -> str:
    suma_x = suma_complejos(a,b,u,v)
    suma_y = suma_complejos(c,d,w,x)
    suma_z = suma_complejos(e,f,y,z)
    respuesta = "(" + suma_x + "," + suma_y + "," + suma_z + ")"
    return respuesta

def inverso_aditivo_r2(a:int,b:int,c:int,d:int)->str:
    componente_x = "(" + str(a*(-1)) + "," + str(b*(-1)) + ")"
    componente_y = "(" + str(c*(-1)) + "," + str(d*(-1)) + ")"
    respuesta = "(" + componente_x + "," + componente_y + ")"
    return respuesta
def inverso_aditivo_r3(a:int, b:int,c:int,d:int,e:int,f:int)->str:
    componente_x = "(" + str(a*(-1)) + "," + str(b*(-1)) + ")"
    componente_y = "(" + str(c*(-1)) + "," + str(d*(-1)) + ")"
    componente_z = "(" + str(e*(-1)) + "," + str(f*(-1)) + ")"
    respuesta = "(" + componente_x + "," + componente_y + "," + componente_z + ")"
    return respuesta

def multi_escalar_r2(a:int,b:int,c:int,d:int,x:int)->str:
    componente_x = "(" + str(a*x) + "," + str(b*x) + ")"
    componente_y = "(" + str(c*x) + "," + str(d*x) + ")"
    respuesta = "(" + componente_x + "," + componente_y + ")"
    return respuesta
def multi_escalar_r3(a:int, b:int,c:int,d:int,e:int,f:int,x:int) ->str:
    componente_x = "(" + str(a*x) + "," + str(b*x) + ")"
    componente_y = "(" + str(c*x) + "," + str(d*x) + ")"
    componente_z = "(" + str(e*x) + "," + str(f*x) + ")"
    respuesta = "(" + componente_x + "," + componente_y + "," + componente_z + ")"
    return respuesta

def suma_matrices(mat_1, mat_2):
    fila = len(mat_1)
    columnas = len(mat_1[0])
    for i in range(fila):
        for j in range(columnas):
            mat_1[i][j] = int(mat_1[i][j]) + int(mat_2[i][j])
    return mat_1

def transpuesta_matriz_vec(mat):
    fila = len(mat)
    columnas = len(mat[0])
    copia_mat = mat
    for i in range(fila):
        for j in range(columnas):
            mat[i][j] = copia_mat[j][i]
    return mat

def multi_escalar_matriz(mat,x:int,y:int):
    fila = len(mat)
    columnas = len(mat[0])
    for i in range(fila):
        for j in range(columnas):
            mat[i][j] = producto_complejos(mat[i][j][0],mat[i][j][1],x,y)
    return mat

def conjugada_matriz_vec(mat):
    fila = len(mat)
    columnas = len(mat[0])
    for i in range(fila):
        for j in range(columnas):
            mat[i][j] = conjugado_complejos(mat[i][j][0],mat[i][j][1])
    return mat

def adjunta_mat_vec(mat):
    respuesta = conjugada_matriz_vec(transpuesta_matriz_vec(math))
    return respuesta

def producto_matrices(mat_1,mat_2):
    fila_1 = len(mat_1)
    fila_2 = len(mat_2)
    columna_1 = len(mat_1[0])
    columna_2 = len(mat_2[0])
    matriz = []
    for i in range(fila_1):
        lista = []
        for j in range(columna_2):
            lista.append(0)
        matriz.append(lista)
    if columna_1 == fila_2:
        for i in range(fila_1):
            for j in range(columna_2):
                for k in range(fila_2):
                    matriz[i][j] += producto_complejos(mat_1[i][k][0],mat_1[i][k][1],mat_2[k][j][0],mat_2[k][j][0])
    return matriz

def accion(mat,vec):
    respuesta = producto_matrices(mat,vec)
    return respuesta

def producto_interno(vec_1,vec_2):
    vector = [0,0]
    for i in range(len(vec_1)):
        vector = suma_vectoresr2(vector, producto_complejos(vec_1[x],vec_2[x]))
    return vector

def norma_vector(vector):
    respuesta = math.sqrt(abs(producto_interno(vector,vector))
    return  respuesta

def distance_vectores(vec1,vec2):
    copia_vec1 = vec1
    for i in range(len(vec1)):
        copia_vec1[i] = resta_complejos(vec1[i],vec2[i])
    return copia_vec1

def matriz_unitaria(matriz):
    fila = len(matriz)
    columna = len(matriz[0])
    if fila == columna:
       adjunta = adjunta_mat_vec(matriz)
       respuesta = producto_matrices(matriz,adjunta)
    if identityMatrix(matriz) == respuesta:
       return "La matriz es unitaria"
    else:
        return "La matriz no es unitaria"

def matrizhermitania(matriz):
    adjunta = adjunta_mat_vec(matriz)
    if adjunta == matriz:
       return "La matriz es hermitania"
    else:
       return "La matriz no es hermitania"

def producto_tensor(mat_1,mat_2):
    respuesta = []
    filas_1 = len(mat_1)
    filas_2 = len(mat_2)
    columnas_1 = len(mat_1[0])
    columnas_2 = len(mat_2[0])
    for i in range(filas_1*filas_2):
        row=[]
        for j in range(columnas_1*columnas_2):
            inA=  mat_1.idx(i//filas_1,j//filas_2)
            inB=  mat_2.idx(i%filas_2,j%filas_2)
            row.append(producto_complejos(inA,inB))
        respuesta.append(row)
    return respuesta