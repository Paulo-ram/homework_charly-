# PROBLEMA UNICO DE PYTHON SERIE FIBONACCI 

"""
    NOMBRE DEL ALUMNO: PAULO RAMIREZ ALVAREZ
    MAESTRO: CHARLY MERCURY
    MATRICULA: 2530384 
    GRUPO: 1-1 IM 
"""

"""
    RESUMEN EJECUTIVO: 
    La serie de Fibonacci es una secuencia donde cada número se obtiene sumando los dos anteriores, empezando 
    por 0 y 1. Calcular la serie hasta un número de términos n significa generar los primeros n valores de esa 
    secuencia. Mi programa leerá el valor de n que ingrese el usuario, validará que sea un número entero positivo 
    y luego generará la serie completa. De esta forma garantiza que el usuario reciba correctamente la cantidad 
    de términos solicitados.
"""

print("---------------FIBONACCI SERIES-------------------")
"""
    PROBLEM : Fibonacci series up to n terms
    Description: 
    Se realiza la serie fibonacci mediante 
    Inputs:
    - num 

    Outputs:
    - sum 

    Validations:
    - n debe poder convertirse a entero.
    - n >= 1.
    - (Opcional) n <= 50 para evitar series demasiado grandes; si no se cumple, mostrar "Error: invalid input".
    - Si la validación falla, NO calcular la serie.

    Test cases:
    1) Normal: 
    How many values do you want?: 10

    Welcome to the fibonacci sequence
    This is the fibonacci serie
    0
    1
    1
    2
    3
    5
    8
    13
    21
    34

    2) Border:
    How many values do you want?: 1

    Welcome to the fibonacci sequence
    This is the fibonacci serie
    0
 
    3) Error: 
    How many values do you want?: 40

    Welcome to the fibonacci sequence
    <class 'ValueError'>

"""
# Fibonacci series calculation
print("Welcome to the fibonacci sequence")
try: 
    num = int(input("How many values do you want?: "))
    if num>=1 and num<=35:
        a = 0
        b = 1
        sum = 0 
        count = 1 
        # print fibonacci series
        print("This is the fibonacci serie")
        while(count<=num):
            print(sum)
            count+=1
            a=b
            b=sum
            sum=a+b
    else:
        print(ValueError)
except: 
    print(ValueError) 

"""
    CONCLUSION:
    El uso de un bucle facilitó mucho la generación de la serie de Fibonacci, porque permitió repetir el 
    cálculo de cada término sin escribir instrucciones adicionales para cada número. Gracias al bucle, 
    la serie se construye de forma ordenada, eficiente y escalable, sin importar cuántos términos se pidan. 
    También es importante manejar correctamente los casos especiales cuando n = 1 y n = 2, ya que los 
    primeros valores de la serie son fijos y no siguen la lógica general de sumar los dos anteriores; 
    ignorar esto podría generar errores o resultados incorrectos. Además, esta misma lógica puede reutilizarse 
    en otros programas que necesiten procesos repetitivos basados en valores previos, como simulaciones, 
    cálculos matemáticos, análisis de secuencias o generación de patrones numéricos más complejos.

"""


"""
    REFERENCIAS:
    1) Real Python. (2023). How to Generate the Fibonacci Sequence in Python.
    https://realpython.com/fibonacci-sequence-python/
    2) Real Python. (2023). How to Generate the Fibonacci Sequence in Python.
    https://realpython.com/fibonacci-sequence-python/
    3) Khan Academy. Fibonacci Sequence Overview.
    https://www.khanacademy.org/math/algebra/sequences/fibonacci-sequence

"""

"""
    REPOSITORIO GIT HUB:
    https://github.com/Paulo-ram/homework_charly-
"""