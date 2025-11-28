# MANEJO DE NUMEROS Y BOOLEANOS EN PYTHON 

"""
    NOMBRE DEL ALUMNO: PAULO RAMIREZ ALVAREZ
    MAESTRO: CHARLY MERCURY
    MATRICULA: 2530384 
    GRUPO: 1-1 IM 
"""

"""
    RESUMEN EJECUTIVO:
    Los tipos int y float en Python representan números, pero se diferencian
    en que los int son valores enteros y los float permiten trabajar con 
    decimales. Un booleano puede ser True o False y suele obtenerse mediante 
    comparaciones como >, < o ==, permitiendo que el programa tome decisiones 
    según las condiciones evaluadas. Validar rangos es importante para evitar 
    errores lógicos y asegurar que los datos sean adecuados, así como prevenir 
    situaciones críticas como intentar dividir entre cero. Este documento explica 
    cada problema desarrollado, describe el diseño de entradas y salidas, detalla 
    las validaciones aplicadas y muestra cómo se usan enteros, flotantes y booleanos 
    para controlar la lógica de ejecución.

"""

"""
    BUENAS PRACTICAS: 
    Es importante utilizar tipos de datos apropiados, como int para contadores y float
    para valores con decimales. También conviene evitar repetir expresiones complejas
    y, en su lugar, almacenar resultados intermedios en variables para mejorar la claridad 
    del código. Antes de realizar cualquier operación, se deben validar los datos, asegurándose
    de que valores como horas o salarios no sean negativos. Además, es fundamental usar nombres 
    de variables descriptivos y mensajes claros para el usuario. Finalmente, se debe documentar 
    cómo se interpretan los valores booleanos dentro del programa, explicando qué representa True 
    y qué representa False en cada contexto operativo.

"""

"""
    Problem 1: Temperature converter and range flag  
    Description: 
    Este comando ayuda al usuario a convertir una temperatura en grados celsius
    (la cual es flotante) a Fahrenheit y Kelvin. Ademas se proporciona un dato 
    en booleano (true or false) que sea true si la temperatura ingresada es mayor 
    o igual a 30 y false si no es el caso.
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

try:
    temp_c = float(input("Enter temperature in Celsius: "))
except:
    print("Error: invalid input")
    temp_c = None

if temp_c is not None:
    temp_k = temp_c + 273.15

    if temp_k < 0:
        print("Error: invalid input")
    else:
        temp_f = temp_c * 9/5 + 32
        is_high_temperature = (temp_c >= 30.0)

        print("Fahrenheit:", temp_f)
        print("Kelvin:", temp_k)
        print("High temperature:", str(is_high_temperature).lower())


"""
    Problem 2:  Work hours and overtime payment
    Description: 
    El trbajador ingresa sus datos como lo son si hizo horas extra y su paga por
    hora y su paga normal que son hasta 40 horas (esas se indican con un flotante). 
    Las horas extra se pagan 150% de la tarifa normal y se debe generar un booleano 
    para indicar si hay horas extra o no.

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

try:
    work_hours = float(input("Enter worked hours: "))
    hourly_rate = float(input("Enter hourly rate: "))
except:
    print("Error: invalid input")
    work_hours = -1
    hourly_rate = -1

if work_hours < 0 or hourly_rate <= 0:
    print("Error: invalid input")
else:
    regular_hours = min(work_hours, 40)
    overtime_hours = max(work_hours - 40, 0)

    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.5
    total_pay = regular_pay + overtime_pay

    has_overtime = (work_hours > 40)

    print("Regular pay:", regular_pay)
    print("Overtime pay:", overtime_pay)
    print("Total pay:", total_pay)
    print("Has overtime:", str(has_overtime).lower())



"""
    Problem 3: Discount eligibility with booleans
    Description: 
    En este programa se busca determinar si un cliente es apto para un descuento
    o no con unas condiciones por ejemplo tiene que tener una compra superior a 
    1000.0 en productos. Tambien tiene descuento si es estudiante o senior.

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

try:
    purchase_total = float(input("Enter purchase total: "))
except:
    print("Error: invalid input")
    purchase_total = -1

is_student_text = input("Is the customer a student? (YES/NO): ").upper()
is_senior_text = input("Is the customer a senior? (YES/NO): ").upper()

if purchase_total < 0:
    print("Error: invalid input")
elif is_student_text not in ("YES", "NO") or is_senior_text not in ("YES", "NO"):
    print("Error: invalid input")
else:
    is_student = (is_student_text == "YES")
    is_senior = (is_senior_text == "YES")

    discount_eligible = (
        is_student or
        is_senior or
        (purchase_total >= 1000.0))

    if discount_eligible:
        final_total = purchase_total * 0.9
    else:
        final_total = purchase_total

    print("Discount eligible:", str(discount_eligible).lower())
    print("Final total:", final_total)


"""
    Problem 4: Basic statistics of three integers
    Description: 
    El usuario ingresa tres numeros valores enteros y calculas su suma, promedio
    y muestra el valor maximo y minimo. Se requiere un booleano para indicar si 
    es que los tres numeros son pares. 
    
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

try:
    n1 = int(input("Enter integer 1: "))
    n2 = int(input("Enter integer 2: "))
    n3 = int(input("Enter integer 3: "))
except:
    print("Error: invalid input")
    n1 = n2 = n3 = None

if n1 is None:
    pass
else:
    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 0)

    print("Sum:", sum_value)
    print("Average:", average_value)
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", str(all_even).lower())

"""
    Problem 5: Loan eligibility
    Description: 
    Se busca que el derechohabiente ingrese sus datos para saber si es 
    acreedor de un prestamo. Tiene que ingresar su ingreso mensual, pagos 
    mensuales de deuda y su puntaje de crédito. Ciertos parametros son necesarios 
    para ser elegible.

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

try:
    monthly_income = float(input("Enter monthly income: "))
    monthly_debt = float(input("Enter monthly debt: "))
    credit_score = int(input("Enter credit score: "))
except:
    print("Error: invalid input")
    monthly_income = -1

if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
    print("Error: invalid input")
else:
    debt_ratio = monthly_debt / monthly_income
    eligible = (
        monthly_income >= 8000.0 and
        debt_ratio <= 0.4 and
        credit_score >= 650
    )

    print("Debt ratio:", debt_ratio)
    print("Eligible:", str(eligible).lower())

"""
    Problem 6: Body Mass Index (BMI) and category flag
    Description: 
    Programa para calcular el inidice de masa corporal del usuario 
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