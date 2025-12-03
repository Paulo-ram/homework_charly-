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

print("---------------FIRST PROBLEM-------------------")
"""
    Problem 1: Temperature converter and range flag  
    Description: 
    Este comando ayuda al usuario a convertir una temperatura en grados celsius
    (la cual es flotante) a Fahrenheit y Kelvin. Ademas se proporciona un dato 
    en booleano (true or false) que sea true si la temperatura ingresada es mayor 
    o igual a 30 y false si no es el caso.

    Inputs:
    - tempu_C

    Outputs:
    - temp_F
    - temp_K
    - booleano = is_high_temperature 

    Validations:
    - full_name no debe estar vacío después de strip().
    - Debe contener al menos dos palabras (por ejemplo, nombre y apellido).
    - No aceptar cadenas que sean solo espacios.


    Test cases:
    1) Normal: 
    Enter temperature in Celsius: 25


    Fahrenheit: 77.0
    Kelvin: 298.15
    High temperature: false

    2) Border: 
    Enter temperature in Celsius: -273.15

    Fahrenheit: -459.66999999999996
    Kelvin: 0.0
    High temperature: false

    3) Error: 
    Enter temperature in Celsius: -300

    Error: invalid input
    
"""
# TEMPS IN FLOAT 
try:
    temp_C = float(input("Enter temperature in Celsius: "))
except:
    print("Error: invalid input")
    temp_C = None
# PRINT THE ERROR 
if temp_C is not None:
    temp_K = temp_C + 273.15
# VALIDS TEMPERATURES 
    if temp_K < 0:
        print("Error: invalid input")
    else:
        temp_F = temp_C * 9/5 + 32
        is_high_temperature = (temp_C >= 30.0)

        print("Fahrenheit:", temp_F)
        print("Kelvin:", temp_K)
        print("High temperature:", str(is_high_temperature).lower())


print("---------------SECOND PROBLEM-------------------")
"""
    Problem 2:  Work hours and overtime payment
    Description: 
    El trbajador ingresa sus datos como lo son si hizo horas extra y su paga por
    hora y su paga normal que son hasta 40 horas (esas se indican con un flotante). 
    Las horas extra se pagan 150% de la tarifa normal y se debe generar un booleano 
    para indicar si hay horas extra o no.

    Inputs:
    - work_hours
    - hourly_rate 

    Outputs:
    - regular_pay
    - overtime_pay
    - total_pay 

    Validations:
    - email_text no vacío tras strip().
    - Contar cuántas veces aparece '@'.
    - Verificar que no haya espacios (no debe haber " " en email_text).


    Test cases:
    1) Normal: 
    Enter worked hours: 45
    Enter hourly rate: 100

    Regular pay: 4000.0
    Overtime pay: 750.0
    Total pay: 4750.0
    Has overtime: true

    2) Border: 
    Enter worked hours: 40
    Enter hourly rate: 120

    Regular pay: 4800.0
    Overtime pay: 0.0
    Total pay: 4800.0
    Has overtime: false

    3) Error: 
    Enter worked hours: -5
    Enter hourly rate: 100

    Error: invalid input

"""
# HOURS IN FLOAT AND THE RATE 
try:
    work_hours = float(input("Enter worked hours: "))
    hourly_rate = float(input("Enter hourly rate: "))
except:
    print("Error: invalid input")
    work_hours = -1
    hourly_rate = -1
# NO NEGATIVE NUMBERS 
if work_hours < 0 or hourly_rate <= 0:
    print("Error: invalid input")
else:
    regular_hours = min(work_hours, 40)
    overtime_hours = max(work_hours - 40, 0)
# CALCULATE 
    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.5
    total_pay = regular_pay + overtime_pay

    has_overtime = (work_hours > 40)

    print("Regular pay:", regular_pay)
    print("Overtime pay:", overtime_pay)
    print("Total pay:", total_pay)
    print("Has overtime:", str(has_overtime).lower())


print("---------------THIRD PROBLEM-------------------")
"""
    Problem 3: Discount eligibility with booleans
    Description: 
    En este programa se busca determinar si un cliente es apto para un descuento
    o no con unas condiciones por ejemplo tiene que tener una compra superior a 
    1000.0 en productos. Tambien tiene descuento si es estudiante o senior.

    Inputs:
    - purchase_total

    Outputs:
    - discount_eligible
    - final_total 

    Validations:
    - phrase no vacía tras strip().
    - Longitud mínima razonable después de limpiar espacios (por ejemplo, al menos 3 caracteres).

    Test cases:
    1) Normal: 
    Enter purchase total: 500
    Is the customer a student? (YES/NO): YES
    Is the customer a senior? (YES/NO): NO

    Discount eligible: true
    Final total: 450.0

    2) Border: 
    Enter purchase total: 1000
    Is the customer a student? (YES/NO): NO
    Is the customer a senior? (YES/NO): NO

    Discount eligible: true
    Final total: 900.0

    3) Error: 
    Enter purchase total: abc
    Is the customer a student? (YES/NO): YES
    Is the customer a senior? (YES/NO): NO

    Error: invalid input

"""

# TOTAL IN FLOAT AND NO LETTERS
try:
    purchase_total = float(input("Enter purchase total: "))
except:
    print("Error: invalid input")
    purchase_total = -1

is_student_text = input("Is the customer a student? (YES/NO): ").upper()
is_senior_text = input("Is the customer a senior? (YES/NO): ").upper()
# NO NEGATIVE 
if purchase_total < 0:
    print("Error: invalid input")
elif is_student_text not in ("YES", "NO") or is_senior_text not in ("YES", "NO"):
    print("Error: invalid input")
# VALID THE INPUT IS CORRECT 
else:
    is_student = (is_student_text == "YES")
    is_senior = (is_senior_text == "YES")

    discount_eligible = (
        is_student or
        is_senior or
        (purchase_total >= 1000.0))
    # KWON IF THE CLIENT IS GOOD FOR THIS 
    if discount_eligible:
        final_total = purchase_total * 0.9
    else:
        final_total = purchase_total
        # PRINT THE OUTPODS 
    print("Discount eligible:", str(discount_eligible).lower())
    print("Final total:", final_total)


print("---------------FOURTH PROBLEM-------------------")
"""
    Problem 4: Basic statistics of three integers
    Description: 
    El usuario ingresa tres numeros valores enteros y calculas su suma, promedio
    y muestra el valor maximo y minimo. Se requiere un booleano para indicar si 
    es que los tres numeros son pares. 
    
    Inputs:
    - n1
    - n2 
    - n3 

    Outputs:
    - sum_value 
    - average_value 
    - max_value
    - min_value
    - all_evem

    Validations:
    - Verificar que los tres valores se puedan convertir a int.
    - No se requieren restricciones adicionales (se permiten negativos).

    Test cases:
    1) Normal: 
    Enter integer 1: 4
    Enter integer 2: 10
    Enter integer 3: 6

    Sum: 20
    Average: 6.666666666666667
    Max: 10
    Min: 4
    All even: true

    2) Border: 
    Enter integer 1: -1
    Enter integer 2: 0
    Enter integer 3: 2

    Sum: 1
    Average: 0.3333333333333333
    Max: 2
    Min: -1
    All even: false

    3) Error: 
    Enter integer 1: a
    Enter integer 2: 5
    Enter integer 3: 6

    Error: invalid input
    
"""
# NUMBERS INT 
try:
    n1 = int(input("Enter integer 1: "))
    n2 = int(input("Enter integer 2: "))
    n3 = int(input("Enter integer 3: "))
except:
    print("Error: invalid input")
    n1 = n2 = n3 = None
# ERROR TO FLOATS OR LETTERS 
if n1 is None:
    pass
else:
    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 0)
# CALCULATE AND PRINT THE RESULTS 
    print("Sum:", sum_value)
    print("Average:", average_value)
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", str(all_even).lower())

print("---------------FIFTH PROBLEM-------------------")
"""
    Problem 5: Loan eligibility
    Description: 
    Se busca que el derechohabiente ingrese sus datos para saber si es 
    acreedor de un prestamo. Tiene que ingresar su ingreso mensual, pagos 
    mensuales de deuda y su puntaje de crédito. Ciertos parametros son necesarios 
    para ser elegible.

    Inputs:
    - monthly_income
    - monthly_debt
    - credit_score 

    Outputs:
    - debt_ratio
    - eligible 

    Validations:
    - monthly_income > 0.0 (evitar división entre cero).
    - monthly_debt >= 0.0
    - credit_score >= 0
    - Si no se cumple, mostrar "Error: invalid input".

    Test cases:
    1) Normal:
    Enter monthly income: 10000
    Enter monthly debt: 3000
    Enter credit score: 700

    Debt ratio: 0.3
    Eligible: true

    2) Border:
    Enter monthly income: 8000
    Enter monthly debt: 3500
    Enter credit score: 640

    Debt ratio: 0.4375
    Eligible: false
 
    3) Error: 
    Enter monthly income: -5000
    Enter monthly debt: 2000
    Enter credit score: 700

    Error: invalid input    
"""
# BECOME THE INPUTS FLOATS OR INT 
try:
    monthly_income = float(input("Enter monthly income: "))
    monthly_debt = float(input("Enter monthly debt: "))
    credit_score = int(input("Enter credit score: "))
except:
    print("Error: invalid input")
    monthly_income = -1
# PRINT THE ERROR IN THE CASES 
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
# PRINT THE RESULTS 

print("---------------SIXTH PROBLEM-------------------")
"""
    Problem 6: Body Mass Index (BMI) and category flag
    Description: 
    Programa para calcular el inidice de masa corporal del usuario al momento que
    el usuario ingrese su peso y altura se van a operar como datos flotantes apartir 
    de ahi con los parametro mediante boleanos se indica si sobre pasa si es muy bajo
    o normal.  

    Inputs:
    - weigth_kg
    - heigth_M

    Outputs:
    - bmi_out
    - boolean = (
            is_underweigth,
            is_normal,
            is_overweigth
            )

    Validations:
    - weight_kg > 0.0
    - height_m > 0.0
    - Si no se cumple, mostrar "Error: invalid input".

    Test cases:
    1) Normal: 
    Enter weight in kg: 70
    Enter height in meters: 1.75

    BMI: 22.86
    Underweight: false
    Normal: true
    Overweight: false

    2) Border: 
    Enter weight in kg: 50
    Enter height in meters: 1.70
    
    BMI: 17.3
    Underweight: true
    Normal: false
    Overweight: false

    3) Error: 
    Enter weight in kg: -10
    Enter height in meters: 1.75

    Error: invalid input
"""

try:
    weight_kg = float(input("Enter weight in kg: "))
    height_M = float(input("Enter height in meters: "))
except:
    print("Error: invalid input")
    weight_kg = -1

if weight_kg <= 0 or height_M <= 0:
    print("Error: invalid input")
else:
    bmi = weight_kg / (height_M * height_M)
    bmi_out = round(bmi, 2)

    is_underweight = (bmi < 18.5)
    is_normal = (bmi >= 18.5 and bmi < 25.0)
    is_overweight = (bmi >= 25.0)

    print("BMI:", bmi_out)
    print("Underweight:", str(is_underweight).lower())
    print("Normal:", str(is_normal).lower())
    print("Overweight:", str(is_overweight).lower())


"""
    CONCLUSION:
    Los enteros y flotantes se usan juntos en muchos cálculos reales, como salarios, 
    promedios o intereses. Las comparaciones generan valores booleanos que permiten 
    tomar decisiones mediante estructuras if. Validar rangos es esencial para evitar 
    errores lógicos y prevenir situaciones críticas como dividir entre cero. Además, 
    el uso de condiciones combinadas con and, or y not permite crear reglas más precisas 
    y adaptadas a diferentes casos. Estos mismos patrones aparecen en problemas de nómina, 
    descuentos, préstamos y cualquier situación donde intervengan números y reglas de decisión. 
    En conjunto, aprender cómo interactúan estos elementos ayuda a construir programas más 
    seguros y confiables.
"""

"""
    REFERENCIAS:
    1) Python Software Foundation. (2024). Numeric Types — int, float, complex.
    https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
    2) Python Software Foundation. (2024). math — Mathematical functions.
    https://docs.python.org/3/library/math.html
    3) Python Software Foundation. (2024). random — Generate pseudo-random numbers.
    https://docs.python.org/3/library/random.html
    4) Python Software Foundation. (2024). decimal — Decimal fixed point arithmetic.
    https://docs.python.org/3/library/decimal.html
    5) Python Software Foundation. (2024). fractions — Rational numbers.
    https://docs.python.org/3/library/fractions.html

"""

"""
    REPOSITORIO GIT HUB:
    https://github.com/Paulo-ram/homework_charly-
"""