## Teoria Cuantica Observables y Medidas

En este programa introduciremos los observables, los cuales pueden ser vistos como las cantidades que pueden ser observadas en cada estado del espacio de estados, de hecho cada observable puede pensarse como :

Cada observable puede pensarse como una pregunta específica que planteamos al sistema:
*si el sistema se encuentra actualmente en algún estado dado **|ψ>**, ¿qué valores podemos observar?*

## Contenido
El siguiente programa posee las siguientes funciones en el archivo llamado :

- Calcular la probabilidad de transitar de el uno al otro después de hacer la observación
- Operacion Bra
- Normalizacion de vectores
- Calcular los ve
- Observable y la probabilidad de que el sistema transite a alguno de los vectores propios después de la observación.
- ejercicios 4.3.1, 4.3.2, 4.4.1, 4.4.2, 4.5.2 y 4.5.3 del libro.


**Explicación de ejercicios 4.5.2**

**Explicación de ejercicios 4.5.3**

## Instalacion
Para que puedas usar las funciones de los numeros complejos primero tendras que cumplir con algunas condiciones:
1. Descargar el lenguaje de programacion [phyton](https://www.python.org/downloads/)(click para descargar), ya que nuestras librerias se basan en este lenguaje,usa versiones superiores a la 3 para que no tengas problemas con el uso de librerias externas.
2. Necesitaras una consola donde puedas ejecutar phyton, en este caso usaremos [PyCharm Comiunity](https://www.jetbrains.com/es-es/pycharm/download/#section=windows)(click para descargar) pero tu podras usar la que quieras.
3. Descarga las librerias correspondientes que deseas usar, Dirijase a la opcion ¨Codigo¨ en el inicio de este repositorio, Allí podras descargar los archivos en formato zip.A continuacion te presentamos las librerias con que contamos:
   * [Libreria de Operaciones Basicas de Numeros Complejos](https://github.com/Camilomora10/Cuantico/blob/master/libreriaComplejos.py).(click para ver)
   * [Libreria de matrices y Vectores Complejos](https://github.com/Camilomora10/Cuantico/blob/master/vectores_matrices.py).(click para ver)
   * [Libreria Sistemas Clasicos y Cuanticos](https://github.com/Camilomora10/Cuantico/blob/master/libreria_sistema_clasico_cuantico.py).(click para ver)
4. Una vez descargado el archivo zip descomprimelo,  Allí podras encontrar las librerias estas se caracterizan por terminar en .py.
5. Una vez descargadas las librerias inicialas en la aplicacion pycharm commiunity en la ventana file-open, Allí selecciona la ubicacion donde descargaste las librerias.
6. Una vez abiertas podra ver las funciones de los numeros complejos y poder usarlas. ¡Disfrutalas!

Adicionalmente usamos librerias externa que debes tener instaladas en tu consola para que te funcionen todas nuestras librerias.
* [Numpy](https://numpy.org/)(Click para descargar).
* [matplotlib](https://matplotlib.org/downloads.html)(Click para descargar).

Mira el siguiente Tutorial para instalar las librerias en Pycharm Commiunity:
* [Importar librerias PyCharm Commiunity](https://www.youtube.com/watch?v=aROm4KYHXLI)(Click para ver).

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
** Simulaciones y Experimentos Cuanticos:


1. simulation de experimento de la canicas con coeficiente booleanos:
Son matrizes y vectores que todos sus componentes son booleanos
```
matriz = [[bool], [bool], [bool], ....] 

vector = [bool, ...]

```

2. Experimentos de las múltiples rendijas clásico probabilístico, con más de dos rendijas. 
Son matrizes y vectores que todos sus componentes son Numeros complejos de la forma a + bi([a,b])
```
matriz = [[[a,b], [c,d], ...], ....]

vector = [[e,f], [i,h], ...] 
```

3. Experimento de las múltiples rendijas cuántico.
Son matrizes y vectores que todos sus componentes son Numeros complejos de la forma a + bi([a,b]) y el vector prob (probabilidad) es un vector con elementos ded tipo float.
```
matriz = [[[a,b], [c,d], ...], ....]

vector = [[e,f], [i,h], ...] 
proba = [float, ...]
```

4. Diagrama de barras que muestre las probabilidades de un vector de estados:
el vector prob (probabilidad) es un vector con elementos ded tipo float.
```
Prob = [float, ...]
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
 3. [Documentacion Sistemas Cuanticos](https://github.com/Camilomora10/Tecnologia/blob/master/documentacion3.md).(click para ver)
 
 * ## Pruebas
Las pruebas en un programa nos permiten verificar que las funcionalidades del programa se cumplan correctamente,usamos la biblioteca unittest de python con el parámetro assertEqual para comparar las respuestas.
Para este caso usaremos la libreria de python unittest ; la cual es usada para comparar un resultado con otro diciendo si son iguales o no, esta es importada con la línea de codigo import unittest, y la puedes encontrar en nuestro repositorio en formato .py. Los archivos de prueba con que contamos son:
1. [Unittest Numeros Complejos](https://github.com/Camilomora10/Tencologia-CNYT1/blob/master/test_complejo.py).(click para ver)
2. [Unittest Matrices y Vectores](https://github.com/Camilomora10/Tencologia-CNYT1/blob/master/test_matrices.py).(click para ver)
3. [Unittest Sistemas Clasicos y Caunticos](https://github.com/Camilomora10/Tencologia-CNYT1/blob/master/test_cuantico.py).(click para ver)

Se encontraran 4 pruebas por cada uno de los ejercicios del libro antes mencionados, propuestospara esta entrega, los cuales son:

**Seccion 4:  Basic Quantum Theory**
- 4.3.1
- 4.3.2
- 4.4.1
- 4.4.2

A continuacion se mostrara un ejemplo de la prueba mostrarRespuesta4_3_1 la cual permite calcular cuales son los posibles estados en el cual puede transitar los diferentes sipin's , de forma analoga sera para las demas funciones:

```
def testExercice4_3_1( self  ):
        #exercice4.4.1 of Quantum Computing for Computer Sci, para el ejericio solo se pedia para Sx , pero para nosotros era para los 3 spin operators
        
        self.assertEqual(mostrarRespuesta4_3_1( sx ),[[[0.7071067811865475, 0.0], [-0.7071067811865475, 0.0]], [[0.7071067811865475, 0.0], [0.7071067811865475, 0.0]]])
```

## Ejecutando Programa 

Para ejecutar el programa se deben seguir los siquientes pasos:

1) Descargar el repositorio en git usando el comando git clone y direccion del repositorio.  
```
git clone https://github.com/Rincon10/CNYT.git
```

2)  abrir el lugar donde se encuentra la implementacion
```
cd Implementations/observables

```
3) ejecutar el archivo con el siguiente comando 

```
python quantumTheory.py
```

 * ## Clonar
Tambien puedes apropiarte de las librerias que usamos clonandolas, para realizar esto dirigete a la opcion ¨Codigo¨ en el inicio de el repositorio, Allí tendras 2 opciones:
 1. Descarga los archivos en formato zip, descomprimelos y usa las librerias en tu consola, estas se caracterizan por terminar en .py.
 2. Para poder clonar el repositorio sin necesidad de descargarlo, debes tener instalado la aplicacion [Git hup](https://desktop.github.com/)(Click para descargar). Una vez instalada la aplicacion crea una cuenta, Ahora dirigete a la opcion ¨Codigo¨ en el inicio de el repositorio y selecciona "Abrir con GitHup Deskop" y automaticamente la aplicacion clonara el repositorio en tu cuenta.
 3. Tambien podras compartir la libreria usando el comando git clone el cual se enceuntra en la opcion la opcion ¨Codigo¨ en el inicio de el repositorio, Alli encontraras el link:
 ```
https://github.com/Camilomora10/Observable.git
```

* ## Ejecutar Pruebas Unittest
1. Descarga Nuestro Repositorio con alguna de las formas que te mostramos antes.
2. Mira el siguiente tutorial [unittest-Marco de prueba automatizado](https://rico-schmidt.name/pymotw-3/unittest/)(click para ver).
Recuerda que las pruebas se encuentran en formato .py en la pagina principal del repositorio, en las siguientes direcciones:
* [Unittest Numeros Complejos](https://github.com/Camilomora10/Tencologia-CNYT1/blob/master/test_complejo.py).(click para ver)
* [Unittest Matrices y Vectores](https://github.com/Camilomora10/Tencologia-CNYT1/blob/master/test_matrices.py).(click para ver)
* [Unittest Sistemas Clasicos y Caunticos](https://github.com/Camilomora10/Tencologia-CNYT1/blob/master/test_cuantico.py).(click para ver)


## Built With

* [GipHup](https://desktop.github.com/) - Plataforma utilizada para crear el proyecto.
* [Pycharm Commiunity](https://www.jetbrains.com/es-es/pycharm/download/#section=windows) - Consola utilizada para crear funciones.
* [phyton 3.8](https://www.python.org/downloads/) - lenguaje de programacion usado.

## Versiones
* Version 1 Numeros Complejos.
* Version 2 Matrices y Vectores Complejos
* Version 3 Sistemas cuanticos 
* Version 4 Doble rendija. 
* Version 5 Observables y Medidas. (Actual)

## Licencia
[Licencia](https://github.com/Camilomora10/Cuantico/blob/master/License).(click para ver)
## Authors

* **Yesid Camilo Mora Barbosa** - Todas las librerias.


