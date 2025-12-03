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
    - n_input

    Outputs:
    - total_sum
    - even_sum 

    Validations:
    - Verificar que n pueda convertirse a int.
    - n >= 1; si no se cumple, mostrar "Error: invalid input".

    Test cases:
    1) Normal: 
    5

    Sum 1..n: 15
    Even sum 1..n: 6

    2) Border: 
    1

    Sum 1..n: 1
    Even sum 1..n: 0

    3) Error: 
    hola

    Error: invalid input
"""

n_input = input("Enter n: ")

try:
    n = int(n_input)
    if n < 1:
        print("Error: invalid input")
    else:
        total_sum = 0
        even_sum = 0

        for i in range(1, n + 1):
            total_sum = total_sum + i

            if i % 2 == 0:
                even_sum = even_sum + i

        print("Sum 1..n:", total_sum)
        print("Even sum 1..n:", even_sum)
except ValueError:
    print("Error: invalid input")


print("---------------SECOND PROBLEM-------------------")
"""
    Problem 2: Multiplication table with for 
    Description: 
    Se debe de realizar un bucle for para generar y mostrarle una table de multiplicar al usuario sabiendo
    que el usuario debe de poner que table desea y un limite hasta que numero quiere esa tabla haciendo que 
    lo vea con ayuda del bucle. 

    Inputs:
    - base_input
    - m_input

    Outputs:
    - base
    - i
    - result

    Validations:
    - base y m convertibles a int.
    - m >= 1; si no, "Error: invalid input".

    Test cases:
    1) Normal: 
    Enter base: 5
    Enter limit m: 4

    5 x 1 = 5
    5 x 2 = 10
    5 x 3 = 15
    5 x 4 = 20

    2) Border: 
    Enter base: 7
    Enter limit m: 1

    7 x 1 = 7

    3) Error: 
    Enter base: hola
    Enter limit m: 5

    Error: invalid input
"""

base_input = input("Enter base: ")
m_input = input("Enter limit m: ")

try:
    base = int(base_input)
    m = int(m_input)
    if m < 1:
        print("Error: invalid input")
  
    for i in range(1, m + 1):
        result = base * i
        print(f"{base} x {i} = {result}")
except:
    print("Error: invalid input")


print("---------------THIRD PROBLEM-------------------")
"""
    Problem 3: Average of numbers with while and sentinel
    Description: 
    Mediante el bucle for de van a leer uno por uno los valores que ingrese el usuario hasta que se ingrese
    un valor sentinela posteriormente calcular el promedio de los valores validos que se ingresaron y la 
    cantidad de los numeros que se leyeron. En dado caso que solo se ingrese un sentinela y ningun numero 
    sea valido se muestra error.

    Inputs:
    - value_input 

    Outputs:
    - count
    - average
    - total 

    Validations:
    - Cada lectura debe intentar convertirse a float.
    - Ignorar el sentinela en los cálculos.


    Test cases:
    1) Normal: 
    Enter number (-7 to stop): 5
    Enter number (-7 to stop): 3
    Enter number (-7 to stop): 2
    Enter number (-7 to stop): -7

    Count: 3
    Average: 3.3333333333333335

    2) Border: 
    Enter number (-7 to stop): -7

    Error: no data

    3) Error: 
    Enter number (-7 to stop): hola

    Error: invalid input
"""

SENTINEL = -7
count = 0
total = 0.0

while True:
    value_input = input("Enter number (-7 to stop): ")

    try:
        number = float(value_input)
    except:
        print("Error: invalid input")
        continue 

    if number == SENTINEL:
        break  
    total += number
    count += 1

if count == 0:
    print("Error: no data")
else:
    average = total / count
    print("Count:", count)
    print("Average:", average)


print("---------------FOURTH PROBLEM-------------------")
"""
    Problem 4: Password attempts with while
    Description:
    Basicamente es un un programa para dar acceso a un usuario ingresando una contraseña tu mismo defines 
    cual es la contraseña y pones un maximo de intentos si acierta pues muestras la bienvenida si no acierta
    y excede los intentos mostrar un mensaje de bloqueo. 

    Inputs:
    - password
    Outputs:
    - login success
    - account locked

    Validations:
    - MAX_ATTEMPTS > 0 (definido como constante en el código, por ejemplo 3).
    - Contar correctamente los intentos.


    Test cases:
    1) Normal: 
    Enter password: hola
    Enter password: 1234
    Enter password: Thepapus

    Login success
    2) Border: 
    Enter password: x
    Enter password: y
    Enter password: z
    Enter password: Thepapus

    Login success

    3) Error: 
    Enter password: 111
    Enter password: 222
    Enter password: 333
    Enter password: 444

    Account locked
"""

CORRECT_PASSWORD = "Thepapus"
MAX_ATTEMPTS = 4

attempts = 0
success = False

while attempts < MAX_ATTEMPTS:
    password = input("Enter password: ")

    if password == CORRECT_PASSWORD:
        print("Login success")
        success = True
        break
    else:
        attempts += 1

if not success:
    print("Account locked")

print("---------------FIFTH PROBLEM-------------------")
"""
    Problem 5: Simple menu with while
    Description:
    Realizar un meno de texto esto quiere decir que mediante el bucle while se va a repetir hasta que el 
    usuario eliga la opcion de salir tu puedes definir que debe que ingresar para que suceda cada opcion las
    acciones son mostrar un saludo, mostrar el valor actual del contador y incrementar el contador se vuelve a 
    mostrar el meno hasta que se ingrese la opcion de salida.

    Inputs:
    - option_input

    Outputs:
    -1) Show greeting
    2) Show current counter value
    3) Increment counter
    0) Exit

    Validations:
    - Normalizar option (por ejemplo, convertir a int con manejo de error).
    - Asegurar que sólo 0,1,2,3 sean aceptadas como válidas.


    Test cases:
    1) Normal: 
    Choose an option: 1
    Choose an option: 3
    Choose an option: 2
    Choose an option: 0

    Hi!
    Counter incremented by 1
    Counter: 1
    Say goodbye my boy

    2) Border: 
    Choose an option: 2
    Choose an option: 0

    Counter: 0
    Say goodbye my boy

    3) Error: 
    Choose an option: hola

    Error: invalid option
"""

counter = 0

while True:
    print("1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")
    print("0) Exit")

    option_input = input("Choose an option: ")

    try:
        option = int(option_input)
    except:
        print("Error: invalid option")
        continue

    if option == 1:
        print("Hi!")
    elif option == 2:
        print("Counter:", counter)
    elif option == 3:
        counter += 1
        print("Counter incremented by 1") 
    elif option == 0:
        print("Say goodbye my boy")
        break
    else:
        print("Error: invalid option")


print("---------------SIXTH PROBLEM-------------------")
"""
    Problem 6: Pattern printing with nested loops
    Description: 
    Mediante bucles for imprimir patrones de asteristos o distintos signos en forma de triangulos rectangulos 
    y se decido con "n" numeros que ingrese el usuario asi incrementa el numero de filas. Opcional imprimir un 
    segundo patron invertido.

    Inputs:
    - n_input

    Outputs:
    - line 

    Validations:
    - n convertible a int.
    - n >= 1; si no, "Error: invalid input".

    Test cases:
    1) Normal: 
    Enter n: 4

    *
    *
    **
    *
    **
    ***
    *
    **
    ***
    ****

    2) Border: 
    Enter n: 1

    *

    3) Error: 
    Enter n: hola

    Error: invalid input
"""

n_input = input("Enter n: ")

try:
    n = int(n_input)
except:
    print("Error: invalid input")
    exit()

if n < 1:
    print("Error: invalid input")
    exit()

for i in range(1, n + 1):
    line = ""
    for j in range(i):
        line += "*"
        print(line)

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
    REFERENCIAS:
    1) Python Software Foundation. (2024). The for statement.
    https://docs.python.org/3/reference/compound_stmts.html#the-for-statement
    2) Python Software Foundation. (2024). The while statement.
    https://docs.python.org/3/reference/compound_stmts.html#the-while-statement
    3) Python Software Foundation. (2024). 4. More Control Flow Tools.
    Incluye: for, while, break, continue, range().
    https://docs.python.org/3/tutorial/controlflow.html
    4) Python Software Foundation. (2024). range — Sequence of numbers.
    https://docs.python.org/3/library/functions.html#func-range
    5) Python For Loops-https://www.w3schools.com/python/python_for_loops.asp
"""

"""
    REPOSITORIO GIT HUB:
    https://github.com/Paulo-ram/homework_charly-
"""