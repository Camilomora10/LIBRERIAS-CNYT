# Libreria Números Complejos

Este proyecto consiste en una libreria que permitiera conocer los numeros complejos y cómo se realizan sus operaciones a travez de funciones de codigo creadas en el lenguaje de programacion phyton, con el fin de dar una nocion de los numeros complejos y como se podrian trabajar desde un lenguaje de programacion.

Cuenta con las operaciones mas basicas de los numeros complejos como lo son:

 * Suma 
 * Resta
 * Producto 
 * Divison
 * Modulo 
 * Fase
 * Conjugado
 * Cambio Cartesianas a Polares
 * Cambio Polares a Cartesianas

Ademas de las operaciones basicas entre numeros complejos, en esta libreria trabajeremos con vectores y matrices complejas, en la cual podremos realizar las siguientes operaciones:

* Adición de vectores complejos.
* inverso (aditivo) de un vector complejo.
* Multiplicación de un escalar por un complejo vectorial.
* Adición de matrices complejas.
* Inversa (aditiva) de una matriz compleja.
* Multiplicación de un escalar por una matriz compleja.
* Transpuesta de una matriz / vector
* Conjugada de una matriz / vector
* Adjunta (daga) de una matriz / vector
* Producto de dos matrices (de tamaños compatibles)
* Calcular la "acción" de una matriz sobre un vector.
* Producto interno de dos vectores
* Norma de un vector
* Distancia entre dos vectores
* Revisar si una matriz es unitaria
* Revisar si una matriz es Hermitiana
* Producto tensor de dos matrices / vectores

## ¿ Cómo funciona ?
El uso y operaciones de numeros complejos los trabajaremos por medio de lenguaje de programacion phyton en el cuál se le presentara archivos .py en donde se encuentran codigificas las funciones que operan los numeros complejos. A continuacion te mostramos como puedes acceder a estás.

## Pre-requisitos
Para que puedas usar nuestra libreia de numeros complejos necesitaras un ordenador con caracteristicas adecuadas para ejecutar un lenguaje de programacion, ademas de un programa en el cual puedas usar el lenguaje de programacion, donde podras usar nuestras librerias.
El lenguaje de programacion que usaremos sera phyton el cual lo puedes ejecutar desde consolas como lo son ide o PyCharm entre otros.

## Instalacion
Para que puedas usar las funciones de los numeros complejos primero tendras que cumplir con algunas condiciones:
1. Descargar el lenguaje de programacion [phyton](https://www.python.org/downloads/)(click para descargar), ya que nuestras librerias se basan en este lenguaje,usa la version que prefieras.
2. Necesitaras una consola donde puedas ejecutar phyton, en este caso usaremos [PyCharm Comiunity](https://www.jetbrains.com/es-es/pycharm/download/#section=windows)(click para descargar) pero tu podras usar la que quieras.
3. Descarga las librerias correspondientes que deseas usar, Dirijase a la opcion ¨Codigo¨ en el inicio de este repositorio, Allí podras descargar los archivos en formato zip.A continuacion te presentamos las librerias con que contamos:
   * [Libreria de Operaciones Basicas de Numeros Complejos.](https://github.com/Camilomora10/LIBRERIAS-CNYT/blob/master/libreriaComplejos.py).(click para ver)
   * [Libreria de matrices y Vectores Complejos.](https://github.com/Camilomora10/LIBRERIAS-CNYT/blob/master/vectores_matrices.py).(click para ver)
4. Una vez descargado el archivo zip descomprimelo,  Allí podras encontrar las librerias estas se caracterizan por terminar en .py.
5. Una vez descargadas las librerias inicialas en la aplicacion pycharm commiunity en la ventana file-open, Allí selecciona la ubicacion donde descargaste las librerias.
6. Una vez abiertas podra ver las funciones de los numeros complejos y poder usarlas. ¡Disfrutalas!

## Manual de Uso
 * ## Introduccion
Antes de empezar se debe tener en cuenta la forma en que los numeros complejos seran representados, como se sabe los numeros complejos se caracterizan por tener una parte real  y una imaginaria como se observa a continuacion:
```
a + bi
```
lo equivalente para la libreria sera una lista de longitud 2, cuya posicion 0 sera la parte real y la posicion 1 la parte imaginaria; con respecto al numero anterior el equivalente en la libreria  sera:

```
[a,b]
```
Ademas para representar vectores y matrizes lo haremos por medio de listas en donde la longitud de la lista seran las filas y las columnas la longitud de las filas.

* Una matriz de tamaño 2x2 compleja seria:
```
 | a + bi   c + di |
 | e + fi   g - hi |
```
En nuestra libreria sera:
```
[ [[a,b],[c,d]], [[e,f],[g,h]] ]
```
* Un vector de 2 elementos complejo seria:
```
 | a + bi |
 | c + di |
```
En nuestra libreria sera:
```
[ [[a,b]], [[e,f]] ]
```
* Un numero en forma polar sera:
```
(r, θ) 
```
En nuestra libreria sera:
```
[r, θ] 
```

 * ## ¿Cómo usar las Funciones?
 Para que puedas usar las funciones de los numeros complejos abre la libreria que deseas usar y dirigete al final del archivo, digita main y dale enter, te aparesera lo sieguiente:
 
```
if__name__ == '__main__': 
```
Ahora crea una variable respuesta en donde su valor sera el resultado de la operacion que deseas usar e imprimelo.
 ```
if__name__ == '__main__': 
    respuesta = operacion
    print(respuesta)
```
Cambia "respuesta" por la operacion que deseas realizar, allí podras digitara los parametros que requiere la operacion compleja, luego dale Run en la consola y automaticamente te aparecera la respuesta de la operacion que usaste. A continuacion un ejemplo:
 1. Coloca la operacion que deseas realizar:
```
if__name__ == '__main__': 
    respuesta = suma_complejos()
    print(respuesta)
```
2. Digite los parametros:
```
if__name__ == '__main__': 
    respuesta = suma_complejos([12,3],[4,6])
    print(respuesta)
```
3. Salida del Resultado:
```
(17,7)
```
 * ## Documentacion
 Es necesario que conozcas que operacion realiza cada funcion y cuales son los parametros que debes ingresar para poder usarla, por eso te mostramos la documuentacion de las librerias que manejamos.
 1. [Documentacion Complejos](https://github.com/Camilomora10/LIBRERIAS-CNYT/blob/master/documentacion1.md).(click para ver)
 2. [Documentacion Matrizes y Vectores](https://github.com/Camilomora10/LIBRERIAS-CNYT/blob/master/documentacion2.md).(click para ver)
 
 * ## Pruebas
Las pruebas en un programa nos permiten verificar que las funcionalidades del programa se cumplan correctamente.
Para este caso usaremos la libreria de python unittest ; la cual es usada para comparar un resultado con otro diciendo si son iguales o no, esta es importada con la línea de codigo import unittest, y la puedes encontrar en nuestro repositorio en formato .py. Los archivos de prueba con que contamos son:
1. [Unittest Numeros Complejos]().(click para ver)
2. [Unittest Matrices y Vectores]().(click para ver)

A continuacion se mostrara un ejemplo de una prueba de la funcion suma_vectores la cual nos dice el resultado de la suma entre los vectores complejos a y b el cual es igual a [[2, 6], [4, 8]],  de forma analoga sera para las demas funciones:
```
#Numeros Complejos
a = [ 1,3 ]
b = [ 2,4 ]

def testsumaVect(self):
   self.assertEqual(suma_vectoresr2([a, b], [a, b]), [[2, 6], [4, 8]])
```
 
 * ## Clonar
Tambien puedes apropiarte de las librerias que usamos clonandolas, para realizar esto dirigete a la opcion ¨Codigo¨ en el inicio de el repositorio, Allí tendras 2 opciones:
 1. Descarga los archivos en formato zip, descomprimelos y usa las librerias en tu consola, estas se caracterizan por terminar en .py.
 2. Para poder clonar el repositorio sin necesidad de descargarlo, debes tener instalado la aplicacion [Git hup](https://desktop.github.com/)(Click para descargar). Una vez instalada la aplicacion crea una cuenta, Ahora dirigete a la opcion ¨Codigo¨ en el inicio de el repositorio y selecciona "Abrir con GitHup Deskop" y automaticamente la aplicacion clonara el repositorio en tu cuenta.
 3. Tambien podras compartir la libreria usando el comando git clone el cual se enceuntra en la opcion la opcion ¨Codigo¨ en el inicio de el repositorio, Alli encontraras el link:
 ```
git clone https://github.com/Camilomora10/LIBRERIAS-CNYT.git
```
## Built With

* [GipHup](https://desktop.github.com/) - Plataforma utilizada para crear el proyecto.
* [Pycharm Commiunity](https://www.jetbrains.com/es-es/pycharm/download/#section=windows) - Consola utilizada para crear funciones.
* [phyton](https://www.python.org/downloads/) - lenguaje de programacion usado.

## Versiones
* Version 1 Numeros Complejos.
* Version 2 Matrices y Vectores Complejos (Actual).

## Licencia
[Licencia](https://github.com/Camilomora10/LIBRERIAS-CNYT/blob/master/License).(click para ver)
## Authors

* **Yesid Camilo Mora Barbosa** - Codigo: 2168535


