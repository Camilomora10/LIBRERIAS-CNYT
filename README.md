.
## Observable

En este programa introduciremos los observables, los cuales pueden ser vistos como las cantidades que pueden ser observadas en cada estado del espacio de estados, de hecho cada observable puede pensarse como :

Cada observable puede pensarse como una pregunta específica que planteamos al sistema:
*si el sistema se encuentra actualmente en algún estado dado **|ψ>**, ¿qué valores podemos observar?*




## Empezando
El siguiente programa posee las siguientes funciones en el archivo llamado :

- Calcular la probabilidad de transitar de el uno al otro después de hacer la observación
- Operacion Bra
- Normalizacion de vectores
- Calcular los ve
- Observable y la probabilidad de que el sistema transite a alguno de los vectores propios después de la observación.
- ejercicios 4.3.1, 4.3.2, 4.4.1, 4.4.2,  4.5.2 y 4.5.3 del libro.


**Explicación de ejercicios 4.5.2**


**Explicación de ejercicios 4.5.3**

### Pre-requisitos

-Tener instalado una version mayor o igual a python 3
-Es opcional tener instalado git **( ya que los comandos pueden ser introducios desde CMD )**
-Tener de manera virtual o fisica el libro:
**Noson S. Yanofsky, Mirco A. Mannucci. Quantum Computing for Computer Scientists.
Cambridge University Press. 2013 (First published 2008). **
- Tener instalado la libreria numpy en su ordenador 

### Instalando y ejecucion del programa

En caso de no tener instalado python o tener python 2.7 ,este  se podra descargar del siguiente link 
https://www.python.org/downloads/ .

En caso de no tener instalado git, este  se podra descargar del siguiente link 
https://git-scm.com/downloads.

En caso de no tener instalado numpy, seguir las indicaciones del siguiente video https://www.youtube.com/watch?v=oE4KeuVNqcQ&list=LLwZJu6f8CavefyakHGC1HEw


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

### Pruebas del programa 

Las pruebas en un programa son muy importantes, tanto es asi que estas permiten verificar que las funcionalidades del programa se cumplen en cada iteración correctamente.

Para este caso se usa la libreria de python  **unittest**; la cual es usada para comparar un resultado con otro diciendo si son iguales o no, esta es  importada con la linea de codigo **import unittest** que se encuentra en observableTest.py .

En este .py se encontraran 4 pruebas por cada uno de los ejercicios del libro antes mencionados, propuestospara esta entrega, los cuales son:

**Seccion 4:  Basic Quantum Theory**
- 4.3.1
- 4.3.2
- 4.4.1
- 4.4.2

A continuacion se mostrara un ejemplo de la prueba mostrarRespuesta4_3_1 la cual permite calcular cuales son los posibles estados en el cual puede transitar los diferentes sipin's , de forma analoga sera para las demas funciones:

# Funcion en la libreria 
```
def testExercice4_3_1( self  ):
        #exercice4.4.1 of Quantum Computing for Computer Sci, para el ejericio solo se pedia para Sx , pero para nosotros era para los 3 spin operators
        
        self.assertEqual(mostrarRespuesta4_3_1( sx ),[[[0.7071067811865475, 0.0], [-0.7071067811865475, 0.0]], [[0.7071067811865475, 0.0], [0.7071067811865475, 0.0]]])
```




## Ejecutando Pruebas

Para ejecutar las pruebas se deben seguir los siquientes pasos:

1) Descargar el repositorio en git hub usando el comando git clone  
```
git clone https://github.com/Rincon10/CNYT.git
```

2)  abrir el lugar donde se encuentra la implementacion
```
cd Implementations/observableTest

```

3) ejecutar las pruebas  con el siguiente comando 

```
 python quantumTheoryTest.py
```
# Salida en IDLE

![image](https://user-images.githubusercontent.com/53798019/78055834-baae1880-7349-11ea-95a2-7977b1f3d107.png)


## Autor

**Iván Camilo Rincón Saavedra** -[Rincon10](https://github.com/Rincon10)


## Referencias
El modelo que se siguio para diseñar el readme fue tomado del usuario:

[PurpleBooth](https://github.com/PurpleBooth)


