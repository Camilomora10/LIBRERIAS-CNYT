## LIBRERÍA NÚMEROS  COMPLEJOS

El lenguaje de programación de esta librería se basa en Phyton y nos permitirá trabajar operaciones con números complejos

---
>import math  

 >"""Libreria de Numeros complejos. Contara con atributos x, y , r y angle.  
 Donde a y b con las componentes cartesianes ( x : parte real , y: parte imaginaria), r es el modulo o magnitud, y angle es angulo theta en coordenadas polares. 
 Son INMUTABLES , por lo tanto una vez creados no se pueden modificar ninguno de sus atributos. """
 
>def suma_complejos(x: int, y: int, a: int, b: int) -> str:  
    """   
Funcion que realiza la suma de dos números complejos.  
:param x: Parte real de el primero numero complejo 
 :param y: Parte imaginaria del primer numero complejo  
 :param a: Parte real del segundo numero complejo  
 :param b: Parte imaginaria del segundo numero complejo  
 :return: string que representa la suma de los numeros complejos.  
 """  
 suma_real = str(int(x) + int(a))  
 suma_imaginaria = str(y + b)  
 respuesta = "(" + suma_real + "," + suma_imaginaria + ")"  
 return respuesta  
 
 >def resta_complejos(x: int, y: int, a: int, b: int) -> str:  
    """  
 Funcion que realiza la resta de dos numeros complejos.  
 :param x: Parte real de el primero numero complejo  
 :param y: Parte imaginaria del primer numero complejo  
 :param a: Parte real del segundo numero complejo  
 :param b: Parte imaginaria del segundo numero complejo  
 :return: string que representa la resta de los numeros complejos.  
 """  
 parte_real = str(x - a)  
 parte_imaginaria = str(y - b)  
 respuesta = "(" + parte_real + "," + parte_imaginaria + ")"  
 return respuesta  
  
>def producto_complejos(x: int, y: int, a: int, b: int) -> str:  
    """  
 Funcion que realiza el producto de dos numeros complejos. 
 :param x: Parte real de el primero numero complejo  
 :param y: Parte imaginaria del primer numero complejo  
 :param a: Parte real del segundo numero complejo  
 :param b: Parte imaginaria del segundo numero complejo  
 return: string que representa el producto de los numeros complejos.  
 """  
 parte_real = str((x * a)-(y * b))  
 parte_imaginaria = str((x * b)+(y * a))  
 respuesta = "(" + parte_real + "," + parte_imaginaria + ")"  
return respuesta  
  
>def division_complejos(x: int, y: int, a: int, b: int) -> str:  
    """  
 Funcion que realiza la division de dos numeros complejos.  :param x: Parte real de el primero numero complejo  :param y: Parte imaginaria del primer numero complejo  :param a: Parte real del segundo numero complejo  :param b: Parte imaginaria del segundo numero complejo  :return: string que representa la division de los numeros complejos.  
 """  parte_real = str(((x * a)+(y * b))/(a ** 2 + b ** 2))  
    parte_imaginaria = str(((y * a)-(x * b))/(a ** 2 + b ** 2))  
    respuesta = "(" + parte_real + "," + parte_imaginaria + ")"  
  return respuesta  
  
>def conjugado_complejos(x: int, y: int) -> str:  
    """  
 Funcion que realiza el conjugado de un numero complejo.  
 :param x: Parte real del numero complejo  
 :param y: Parte imaginaria del numero complejo  
 :return: string que representa el conjugado del numero complejo.  
 """ 
  parte_real = str(x)  
  parte_imaginaria = str(y*(-1))  
  respuesta = "(" + parte_real + "," + parte_imaginaria + ")"  
  return respuesta  
  
>def modulo_complejos(x: int, y: int) -> str:  
    """  
 Funcion que realiza el modulo de un numero complejo.  
 :param x: Parte real del numero complejo  
 :param y: Parte imaginaria del numero complejo  
 :return: string que representa el modulo del numero complejo.  
 """  
 respuesta = str((x **2 + y **2) **(0.5))  
 return respuesta  
  
 
>def angulo_complejos(x: int, y: int) -> str:  
    """  
 Funcion que realiza la fase o angulo de un numero complejo.  
 :param x: Parte real del numero complejo  
 :param y: Parte imaginaria del numero complejo  
 :return: string que representa la fase del numero complejo.  
 """  
 angle = math.atan2(y, x)  
    if (angle > 0) :  
        angle = angle*(-1)  
        angle = angle%(math.pi * 2)  
        angle = math.pi*2 - angle  
    respuesta = str(angle)  
    return respuesta  
  
>def cartesianas_polares_complejos(x: int, y: int) -> str:  
    """  
 Funcion que realiza la transformacion de coordenadas cartesianas a polares de un numero complejo.  
 :param x: Parte real del numero complejo  
 :param y: Parte imaginaria del numero complejo  
 :return: string que representa la forma polar del numero complejo.  
 """  
 radio = str((x ** 2 + y ** 2  )**(0.5))  
    angulo = str(math.atan(y/x))  
    respuesta = "(" + radio + "," + angulo + ")"  
  return respuesta  
  
>def polares_cartesianas_complejos(r:int, a:int) -> str:  
    """  
 Funcion que realiza la transformacion de coordenadas polares a cartesianas de un numero complejo.  
 :param r: representa el radio del numero complejo  
 :param a: representa el angulo del numero complejo  
 :return: string que representa la forma cartesiana del numero complejo.  
 """  
 parte_real = str(r*(math.cos(a)))  
    parte_imaginaria = str(r*(math.sin(a)))  
    respuesta = "(" + parte_real + "," + parte_imaginaria + ")"  
  return respuesta
  

  

---  
  
*Esta libreria fue creada en pycharm.*  

---  
### **Introduccion de los Numeros Complejos**  
El numero **a + ib** lo representaremos predeterminadamente mediante la dupla:  
$$(a,b) $$ 
con la opcion de imprimirla en el estilo  
$$(a + ib)$$  
y su forma polar:  
$$ (r, \theta) $$  
  
---
