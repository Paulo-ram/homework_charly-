# MANEJO DE FUNCIONES EN PYTHON 

"""
    NOMBRE DEL ALUMNO: PAULO RAMIREZ ALVAREZ
    MAESTRO: CHARLY MERCURY
    MATRICULA: 2530384 
    GRUPO: 1-1 IM 
"""

"""
    RESUMEN EJECUTIVO: 

    Una función en Python es un bloque de código que realiza una tarea específica y sirve para 
    organizar, reutilizar y simplificar el programa. Los parámetros son los nombres que aparecen 
    en la definición de la función, mientras que los argumentos son los valores reales que enviamos 
    cuando la llamamos. Separar la lógica en funciones ayuda a evitar código repetido y hace más 
    fácil mantener y entender el programa. El valor de retorno permite que una función entregue un 
    resultado que puede usarse en otros cálculos, lo cual es mejor que solo imprimir porque da mayor 
    flexibilidad. Este documento cubrirá la descripción de cada problema, el diseño de funciones, sus 
    entradas y salidas, las validaciones necesarias y algunas pruebas básicas para asegurar que cada 
    función funciona correctamente.
"""

"""
    PRINCIPIOS Y BUENAS PRACTICAS: 
    Es buena práctica escribir funciones pequeñas que hagan solo una cosa, ya que eso facilita leer y 
    mantener el código. Siempre que notes que estás copiando y pegando lógica, conviene extraer esa parte 
    en una función para evitar repetición. Cuando sea posible, es útil crear funciones puras, es decir, 
    que con el mismo input siempre produzcan el mismo resultado y no dependan de variables externas. También 
    es importante documentar brevemente qué hace cada función y qué parámetros recibe. Finalmente, usar 
    nombres descriptivos como calculate_bmi o get_total_price ayuda a entender el código sin esfuerzo.
"""

print("---------------FIRST PROBLEM-------------------")
"""
    Problem 1: Rectangle area and perimeter 
    Description:
    En este codigo se deben de definir dos funciones las cuales nos van a ayudar a desarrollar el codigo 
    con exito una de ellas nos va a regresar el area de un rectangulo y otra que nos regresa el perimetro
    las funciones se deben de llamar dependiendo de su accion. 

    Inputs:
    - width
    - heigth 

    Outputs:
    - area
    - perimeter

    Validations:
    - width > 0
    - height > 0
    - Si alguna condición no se cumple, mostrar "Error: invalid input" y no llamar a las funciones.

    Test cases:
    1) Normal:
    # Input:
    Put width: 5
    Put height: 3

    # Output esperado:
    area: 15.0
    perimeter: 16.0
 
    2) Border: 
    # Input:
    Put width: 0.1
    Put height: 0.1

    # Output esperado:
    area: 0.010000000000000002
    perimeter: 0.4

    3) Error: 
    # Input:
    Put width: 0
    Put height: 5

    # Output esperado:
    0 cant be a data

"""
# Define calculate_area and calculate_perimeter functions
def calculate_area (width, height):
    return width* height
def calculate_perimeter (width, height):
    return (width+width+height+height)

width = 0
height = 0
# Input
try:
    width= float(input("Put width:"))
    height= float(input("Put height:"))
    if width>0 and height >0:
        try:   # Call functions and output results
            area = calculate_area(width, height)
            perimeter = calculate_perimeter(width, height)
            print(f"area: {area}")
            print(f"perimeter: {perimeter}")
        except:
            print("Invalid input")
    else:
        print("0 cant be a data")
except:
    print("Invalid input")

print("---------------SECOND PROBLEM-------------------")
"""
    Problem 2: Grade classifier 
    Description: 
    Aqui tenemos que desarrollar funciones la cual va a clasificar una puntuacion dependiendo de su 
    valor seria a,b,c o d se le debe de mostrar al usuario el cual va a ingresar su puntuacion y dada la
    puntuacion se le da su grado.

    Inputs:
    - score 

    Outputs:
    - score 
    - grade 

    Validations:
    - 0 <= score <= 100
    - Si no se cumple, mostrar "Error: invalid input" y no clasificar.

    Test cases:
    1) Normal: 
    # Input:
    85

    # Output esperado:
    Score: 85.0
    Category: B

    2) Border:
    # Input:
    90

    # Output esperado:
    Score: 90.0
    Category: A     # Justo en el límite
 
    3) Error: 
    # Input:
    -5

    # Output esperado:
    Error: invalid input
"""
# Define classify_grade function
def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

try:
    score = float(input("Enter score (0-100): "))
      # Validate score
    if 0 <= score <= 100:
        grade = classify_grade(score)
        print(f"Score: {score}")
        print(f"Category: {grade}")
    else:
        print("Error: invalid input")

except:
    print("Error: invalid input")

print("---------------THIRD PROBLEM-------------------")
"""
    Problem 3: List statistics function 
    Description: 
    El programa debe solicitar al usuario una serie de números escritos en una sola línea y separados 
    por comas. Con estos valores, el código debe construir una lista numérica válida. Una vez generada 
    la lista, se debe llamar a la función summarize_numbers(numbers_list), la cual recibe la lista y 
    devuelve un diccionario que contiene tres estadísticas fundamentaleS.
    
    Inputs:
    - numbers_text 

    Outputs:
    - min 
    - max
    - average

    Validations:
    - numbers_text no vacío tras strip().
    - Lista no vacía después de la conversión.
    - Todos los elementos deben poder convertirse a números; si alguno falla, mostrar "Error: invalid input".


    Test cases:
    1) Normal: 
    Enter numbers separated by commas: 10, 20, 30, 40

    Min: 10.0
    Max: 40.0
    Average: 25.0

    2) Border: 
    Enter numbers separated by commas: 15

    Min: 15.0
    Max: 15.0
    Average: 15.0

    3) Error: 
    Enter numbers separated by commas: 10, 20, hola, 40

    Error: invalid input
"""
# Define summarize_numbers function
def summarize_numbers(numbers_list):
    stats = {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }
    return stats


numbers_text = input("Enter numbers separated by commas: ")

if numbers_text.strip() == "":
    print("Error: invalid input")
else:   # Convert input to list of numbers
    try:
        parts = numbers_text.split(",")
        numbers_list = []

        for p in parts:
            number = float(p.strip())
            numbers_list.append(number)

        if len(numbers_list) == 0:
            print("Error: invalid input")
        else:   # Call summarize_numbers and output results
            stats = summarize_numbers(numbers_list)
            print(f"Min: {stats['min']}")
            print(f"Max: {stats['max']}")
            print(f"Average: {stats['average']}")

    except:
        print("Error: invalid input")

print("---------------FOURTH PROBLEM-------------------")
"""
    Problem 4: Apply discount list 
    Description: 
    El programa solicita una lista de precios y una tasa de descuento. Después usa la función 
    apply_discount(prices_list, discount_rate) para generar una nueva lista con los precios reducidos 
    sin modificar la original. Finalmente, muestra la lista original y la lista con descuento.
    
    Inputs:
    - prices_text
    - discount_text 

    Outputs:
    - prices_list 
    - discounted 

    Validations:
    - prices_text no vacío y lista resultante no vacía.
    - Todos los precios > 0.
    - 0 <= discount_rate <= 1; si no, "Error: invalid input".

    Test cases:
    1) Normal: 
    Enter prices separated by commas: 100, 200, 300
    Enter discount rate (0 to 1): 0.2

    Original prices: [100.0, 200.0, 300.0]
    Discounted prices: [80.0, 160.0, 240.0]

    2) Border: 
    Enter prices separated by commas: 50, 75
    Enter discount rate (0 to 1): 0

    Original prices: [50.0, 75.0]
    Discounted prices: [50.0, 75.0]

    3) Error: 
    Enter prices separated by commas:
    Enter discount rate (0 to 1): 0.3

    Error: invalid input
"""
# Define apply_discount function
def apply_discount(prices_list, discount_rate):
    discounted = []
    for price in prices_list:
        new_price = price * (1 - discount_rate)
        discounted.append(new_price)
    return discounted

prices_text = input("Enter prices separated by commas: ")
discount_text = input("Enter discount rate (0 to 1): ")

if prices_text.strip() == "":
    print("Error: invalid input")
else:  # Validate discount rate and prices
    try:
        discount_rate = float(discount_text)

        if discount_rate < 0 or discount_rate > 1:
            print("Error: invalid input")
        else:
            parts = prices_text.split(",")
            prices_list = []

            for p in parts:
                price = float(p.strip())
                if price <= 0:
                    raise ValueError
                prices_list.append(price)

            if len(prices_list) == 0:
                print("Error: invalid input")
            else:
                discounted = apply_discount(prices_list, discount_rate)
                # Output
                print(f"Original prices: {prices_list}")
                print(f"Discounted prices: {discounted}")

    except:
        print("Error: invalid input")

print("---------------FIFTH PROBLEM-------------------")
"""
    Problem 5: Greeting functions with default parametres 
    Description: 
    El programa define la función greet(name, title=""), que construye un saludo usando un nombre y, 
    opcionalmente, un título. Si el título está presente, se coloca antes del nombre; si no, solo se 
    usa el nombre. El código principal debe llamar la función tanto con argumentos posicionales como 
    con argumentos nombrados y mostrar el mensaje final: "Hello, <full_name>!"
   
    Inputs:
    - name_input
    - title_input 

    Outputs:
    - greeting_message 

    Validations:
    - name no vacío tras strip().
    - title puede estar vacío, pero si no lo está, también se normaliza con strip(). 

    Test cases:
    1) Normal: 
    Enter name: Paulo
    Enter title (optional): Mr.

    Greeting: Hello, Mr. Paulo!

    2) Border:
    Enter name: Ana
    Enter title (optional):

    Greeting: Hello, Ana!
 
    3) Error: 
    Enter name:
    Enter title (optional): Señor

    Error: invalid input
"""
# Define greet function
def greet(name, title=""):
    name = name.strip()
    title = title.strip()

    if title == "":
        full_name = name
    else:
        full_name = f"{title} {name}"

    return f"Hello, {full_name}!"

name_input = input("Enter name: ").strip()
title_input = input("Enter title (optional): ").strip()
 # Validate name
if name_input == "":
    print("Error: invalid input")
else:
    greeting_message = greet(name_input, title_input)
    # Output greeting
    print(f"Greeting: {greeting_message}")

print("---------------SIXTH PROBLEM-------------------")
"""
    Problem 6: Factorial function 
    Description: 
    El programa debe definir una función factorial(n) que calcule el factorial de un número entero 
    n usando un método elegido (iterativo o recursivo), aclarando esa elección en comentarios. En 
    el código principal se debe leer o definir n, validar que sea un número adecuado (entero y no negativo), 
    llamar a la función factorial(n) y finalmente mostrar el resultado al usuario.
    
    Inputs:
    - value_text 

    Outputs:
    - result factorial 

    Validations:
    - n entero.
    - n >= 0.
    - Opcional: limitar n a un máximo razonable (por ejemplo n <= 20) para evitar números 
    demasiado grandes; si no se cumple, mostrar "Error: invalid input".


    Test cases:
    1) Normal: 
    Enter n: 5

    n: 5
    Factorial: 120

    2) Border: 
    Enter n: 0

    n: 0
    Factorial: 1

    3) Error: 
    Enter n: -3

    Error: invalid input
"""
 # Iterative approach to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
  # Input
value_text = input("Enter n: ")
 # Validate n
try:
    n = int(value_text)

    if n < 0 or n > 20:
        print("Error: invalid input")
    else:   # Calculate and output factorial
        result = factorial(n)
        print(f"n: {n}")
        print(f"Factorial: {result}")

except:
    print("Error: invalid input") 

"""
    CONCLUSION:
    Las funciones me ayudaron a organizar mejor el código, separando tareas en bloques claros y 
    reutilizables. Aprendí que usar return es más útil que solo imprimir, porque permite guardar 
    resultados, combinarlos y hacer pruebas fácilmente. También noté que los parámetros y valores 
    por defecto hacen que una misma función pueda adaptarse a diferentes situaciones sin reescribirla. 
    Encapsular lógica en funciones resultó especialmente cómodo en cálculos repetidos y validaciones 
    que se usan varias veces. Finalmente, comprendí la diferencia entre la lógica principal, que 
    coordina el flujo del programa, y las funciones de apoyo, que resuelven tareas específicas y 
    mantienen el código más limpio.
"""


"""
    REFERENCIAS:
    1) Python Software Foundation. (2024). User-Defined Functions.
    https://docs.python.org/3/reference/compound_stmts.html#function-definitions
    2) Python Software Foundation. (2024). 4.6. Defining Functions.
    https://docs.python.org/3/tutorial/controlflow.html#defining-functions
    3) Python Software Foundation. (2024). Function Definitions — Arguments.
    https://docs.python.org/3/reference/expressions.html#calls
    4) Python Software Foundation. (2024). Built-in Functions.
    https://docs.python.org/3/library/functions.html
    5) Python Software Foundation. (2024). Lambda Expressions.
    https://docs.python.org/3/reference/expressions.html#lambda

"""

"""
    REPOSITORIO GIT HUB:
    https://github.com/Paulo-ram/homework_charly-
"""