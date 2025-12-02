# MANEJO LISTAS, DICCIONARIOS Y TUPLAS EN PYTHON 

"""
    NOMBRE DEL ALUMNO: PAULO RAMIREZ ALVAREZ
    MAESTRO: CHARLY MERCURY
    MATRICULA: 2530384 
    GRUPO: 1-1 IM 
"""

"""
    RESUMEN EJECUTIVO:

    Una lista, una tupla y un diccionario en Python son estructuras de datos, pero se 
    diferencian en su comportamiento. Las listas son colecciones ordenadas y modificables, 
    las tuplas son colecciones ordenadas pero inmutables, y los diccionarios almacenan datos 
    mediante pares clave–valor, permitiendo acceder a la información a través de una clave en 
    lugar de un índice. Los diccionarios son especialmente útiles cuando se necesita asociar 
    un identificador con un dato, como códigos con nombres, productos con precios o materias 
    con calificaciones.
    ¿QUE SIGNIFICA QUE UNA LISTA SEA MUTABLE Y UNA TUPLA INMUTABLE?

    Primero que nada se tiene que definir que es mutable y inmutable eso es primordial 
    para definir que es una lista y una tupla. La definicion de mutable es que nos permite 
    modificar la cantidad de datos significa que se pueden meter mas datos en esa lista. En 
    cambio las tuplas son inmutaples dando a entender que no se puede modificar su proporcion 
    DICCIONARIOS PARA ASOCIAR CLAVES O VALORES 

    Los diccionarios se usan para asociar claves con valores, permitiendo acceder rápidamente 
    a la información sin necesidad de buscar por posición. Cada clave funciona como un 
    identificador único, y a esa clave se le asigna un valor, que puede ser un número, un 
    string, una lista, otra estructura o incluso otro diccionario.

    Este documento describirá cada problema trabajado, explicará el diseño de las entradas y 
    salidas, detallará las validaciones aplicadas y mostrará cómo se utilizan listas, tuplas y 
    diccionarios en situaciones prácticas como catálogos, registros y cálculos estadísticos.
"""

"""
    PRINCIPIOS Y BUENAS PRACTICAS:
    Las listas son útiles cuando necesitas agregar o eliminar elementos con frecuencia, mientras
    que las tuplas sirven para datos que no deben cambiar. Los diccionarios permiten buscar información 
    mediante una clave, como un id o un nombre. Es importante no modificar una lista mientras se recorre
    con un for y usar claves descriptivas en los diccionarios para mantener claridad. En general, escribir 
    código legible y mensajes claros ayuda a que el programa sea más fácil de entender y mantener.

"""

print("---------------FIRST PROBLEM-------------------")
"""
    Problem 1: Shopping list basics 
    Description: 
    El programa tiene como objetivo crear una lista inicial de los productos
    que ingrese el usuario, que al final sea permitido ingresar un nuevo producto
    trabajados con una lista de productos siendo strings y sus cantidades manejados
    en enteros. Por ultimo verificar si un producto ya esta en la lista con un 
    booleano.

    Inputs:
    - 

    Outputs:
    - 

    Validations:
    - 

    Test cases:
    1) Normal: 
    2) Border: 
    3) Error: 

"""

print("---------------SECOND PROBLEM-------------------")
"""
    Problem 2: Points and distances with tuples 
    Description: 
    Primero el usuario debe de ingresar unas coordenadas de dos puntos para 
    que con este programa calcular la distancia entre ambos puntos y asi crear
    una nueva tupla con el punto medio.

    Inputs:
    - 

    Outputs:
    - 

    Validations:
    - 

    Test cases:
    1) Normal: 
    2) Border: 
    3) Error: 

"""

print("---------------THIRD PROBLEM-------------------")
"""
    Problem 3: Product catalog with dictionary
    Description:
    Este codigo principalmente tiene como objetivo crear y administrar un 
    pequeño catalogo de productos usando ahi los dccionarios donde se pone 
    nombre y precio del producto. Lo que se quiero hacer es crear un diccionario
    con al menos 3 productos leer el nombre del producto y la cantidad que se 
    quiere comprar, se debe dar un total a pagar y si el producto no existe imprimir 
    un mensaje de error.

    Inputs:
    - 

    Outputs:
    - 

    Validations:
    - 

    Test cases:
    1) Normal: 
    2) Border: 
    3) Error: 

"""

print("---------------FOURTH PROBLEM-------------------")
"""
    Problem 4: Student grades with dict and list
    Description: 
    Como objetivo principal de este problema se tiene que administrar las calificaciones
    de un grupo con la ayuda de diccionarios como el anterior tiene que tener el nombre
    y calificacion (en flotante). Cada estudiante tien que tener una lista de sus calificaciones
    se lee el nombre y calcula el promedio de sus calificaciones por ultimo con un booleano se 
    indica si el estudiante esta reprobado o no.

    Inputs:
    - 

    Outputs:
    - 

    Validations:
    - 

    Test cases:
    1) Normal: 
    2) Border: 
    3) Error: 

"""

print("---------------FIFTH PROBLEM-------------------")
"""
    Problem 5: Word frequency counter
    Description: 
    Contar la frcuencia de cada palabra en una oracion se usan listas y diccionarios
    con la palabra y su frecuencia. Debe de leer una oracion y se normaliza convirtiendola
    en minuscula se separa en una lista y construye un diccionario de frecuencias. Se le
    muestra al usuario el diccionario y la palabra mas frecuente.

    Inputs:
    - 

    Outputs:
    - 

    Validations:
    - 

    Test cases:
    1) Normal: 
    2) Border: 
    3) Error: 

"""

print("---------------SIXTH PROBLEM-------------------")
"""
    Problem 6: Simple contact book
    Description: 
    Se tiene como objetivo implementar un mini libro de contactos con ayuda de un diccionario
    tiene que tener el nombre del contacto y su telefono. Se tiene que leer una accion son tres
    add, search y delete en si agregar buscar y eliminar y mostrar un mensaje de resultado 
    dependiendo de la operacion que el usuario desea realizar. 

    Inputs:
    - 

    Outputs:
    - 

    Validations:
    - 

    Test cases:
    1) Normal: 
    2) Border: 
    3) Error: 

"""


"""
    CONCLUSION:
    Las listas, tuplas y diccionarios se usan según la necesidad: las listas son útiles cuando 
    requieres almacenar datos que cambiarán, porque permiten agregar, eliminar o modificar 
    elementos con mucha flexibilidad. En cambio, las tuplas son convenientes cuando necesitas 
    garantizar que los datos permanezcan fijos, como coordenadas, configuraciones o valores que 
    no deben alterarse. Los diccionarios resultan muy prácticos cuando necesitas hacer búsquedas 
    rápidas usando claves, ya que permiten acceder a la información de manera directa sin recorrer 
    toda la estructura. Al combinar estas estructuras aparecen patrones comunes, como diccionarios 
    que guardan listas o listas de diccionarios, lo cual facilita organizar información compleja de 
    forma ordenada y eficiente.

"""


"""
    REFRENCIAS:
    1) 
    2) 
    3) 
    4) 
    5) 

"""

"""
    REPOSITORIO GIT HUB:

"""