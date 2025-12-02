# MANEJO DE BUCLES EN PYTHON

"""
    NOMBRE DEL ALUMNO: PAULO RAMIREZ ALVAREZ
    MAESTRO: CHARLY MERCURY
    MATRICULA: 2530384 
    GRUPO: 1-1 IM 
"""

"""
    RESUMEN EJECUTIVO: 
    Un bucle for se usa para repetir acciones cuando ya sabes cuántas veces iterar o cuando
    recorres elementos de una colección. El bucle while es útil cuando no sabes cuántas 
    repeticiones habrá y dependes de una condición que debe seguir cumpliéndose. Un contador 
    sirve para llevar el número de iteraciones, mientras que un acumulador reúne o suma 
    valores durante el ciclo.

    LA IMPORTANCIA DE DEFINIR BIEN LAS CONDICIONES Y EVITAR INFINITE CYCLES
    Un programa necesita saber cuándo detenerse; si la condición está mal planteada, el ciclo 
    puede repetirse sin fin. Los ciclos infinitos consumen memoria y procesador, pueden bloquear 
    el programa y evitar que el usuario obtenga resultados. Diseñar correctamente la condición 
    evita errores, cuelgues y comportamientos inesperados, asegurando que el flujo del programa 
    avance de forma controlada y segura.

    También mostrará cómo aplicar bucles for y while en diferentes situaciones, como recorrer datos, 
    manejar menús o repetir procesos hasta cumplir una condición. En conjunto, servirá como una 
    guía práctica para entender y usar correctamente las estructuras repetitivas en distintos 
    escenarios.
"""

"""
    BUENAS PRACTICAS: 
    En esta sección se enfatiza usar for cuando el número de iteraciones está definido y while cuando 
    depende de una condición que puede cambiar durante la ejecución. También se destaca la importancia 
    de inicializar contadores y acumuladores antes del bucle, y actualizar correctamente las variables 
    de control dentro de un while para evitar ciclos infinitos. Además, se recomienda mantener el cuerpo 
    del bucle simple y, si surge lógica compleja, moverla a funciones para mejorar la claridad y el 
    mantenimiento del código.
"""

print("---------------FIRST PROBLEM-------------------")
"""
    Problem 1: Sum of range with for 
    Description: 
    En este problema se define una suma desde el 1 hasta "n" la cual se incluye ademas de eso se debe de 
    incluir la sume solo de los numeros pares en el mismo rango con un mismo bucle for obviamente siendo 
    "n" mayor o igual que 1 porque si no no jala el codigo,

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
    Problem 2: Multiplication table with for 
    Description: 
    Se debe de realizar un bucle for para generar y mostrarle una table de multiplicar al usuario sabiendo
    que el usuario debe de poner que table desea y un limite hasta que numero quiere esa tabla haciendo que 
    lo vea con ayuda del bucle. 

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
    Problem 3: Average of numbers with while and sentinel
    Description: 
    Mediante el bucle for de van a leer uno por uno los valores que ingrese el usuario hasta que se ingrese
    un valor sentinela posteriormente calcular el promedio de los valores validos que se ingresaron y la 
    cantidad de los numeros que se leyeron. En dado caso que solo se ingrese un sentinela y ningun numero 
    sea valido se muestra error.

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
    Problem 4: Password attempts with while
    Description:
    Basicamente es un un programa para dar acceso a un usuario ingresando una contraseña tu mismo defines 
    cual es la contraseña y pones un maximo de intentos si acierta pues muestras la bienvenida si no acierta
    y excede los intentos mostrar un mensaje de bloqueo. 

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
    Problem 5: Simple menu with while
    Description:
    Realizar un meno de texto esto quiere decir que mediante el bucle while se va a repetir hasta que el 
    usuario eliga la opcion de salir tu puedes definir que debe que ingresar para que suceda cada opcion las
    acciones son mostrar un saludo, mostrar el valor actual del contador y incrementar el contador se vuelve a 
    mostrar el meno hasta que se ingrese la opcion de salida.

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
    Problem 6: Pattern printing with nested loops
    Description: 
    Mediante bucles for imprimir patrones de asteristos o distintos signos en forma de triangulos rectangulos 
    y se decido con "n" numeros que ingrese el usuario asi incrementa el numero de filas. Opcional imprimir un 
    segundo patron invertido.

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
    Aprendí que usar for o while depende de lo que necesites: el for es ideal cuando ya sabes cuántas veces repetir 
    algo, y el while funciona mejor cuando esperas a que pase una condición. Los contadores y acumuladores me facilitaron 
    llevar control de repeticiones y sumas dentro de los ciclos. También entendí que con un while hay que tener cuidado, 
    porque si olvidas actualizar la condición puedes crear un ciclo infinito. Además, noté que cosas muy comunes como los 
    menús o los intentos de contraseña funcionan justamente con while. Y al trabajar con bucles anidados, descubrí cómo se 
    pueden generar patrones y resolver problemas más complejos paso a paso.
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