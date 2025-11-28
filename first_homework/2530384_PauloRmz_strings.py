# MANEJOS DE STRING EN PYTHON 
"""
    NOMBRE DEL ALUMNO: PAULO RAMIREZ ALVAREZ
    MAESTRO: CHARLY MERCURY
    MATRICULA: 2530384 
    GRUPO: 1-1 IM 
"""

"""
    String: 
    En python una cadena de texto o un string es un tipo de dato fundamental para la realizacion 
    de codigos estos permiten representar informacion alfanumerica como palabras, frases, nombres 
    direcciones de correo etc. Se describen entre comillas pueden ser dobles o simples.
    Una caracteristica importante de los string es que son imutables quiere decir que al momento 
    de ser creado este no se puede modificar directamente. Python genera una nueva cadena pero no 
    altera la original.

    "Hola"
    "Paulo Ramírez"
    "1234"

    Operaciones basicas con strings:
    Al momento de trabajar con strings en python existen diversas operaciones estas facilidan la 
    manipulacion de strings y el trabajar con ellas en codigos por ejemplo:

    "Hola " + "mundo"  sirve para concatenar dos strings 

    len("python")  # 6 te dice la longitud de tu string

    text = "programación"
    text[0:5]   # 'progr' esto extrae subcadenas

    Al igual se pueden manipular en su tamaño o separarlos:

    .lower(),   Todo lo que contenga el string lo convierte en letras minusculas

    .upper(), Todo lo que contenga el string lo convierte en letras mayusculas

    .strip(),  Elimina espacios en blanco al principio y al final del texto 

    .replace(), Reemplaza todas las ocurrencias de un texto por otro 

    .split(),  Este comando divide el string y las convierte en listas

    .join() Concatena los elementos de una lista en un solo string y usa un separador 

    La importancia de validar y normalizar la entrada: 
    En muchos de los sistemas es indispensable validar si los datos se ingresaron de manera 
    correcta ya que al momento de llegar a la industria te van a dar ciertos parametros que 
    el usuario debera ingresar correctamente para poder continuar con la manipulacion de la 
    entrada esto garantiza que la informacion sea confiable. 
    Por ejemplo, validar un correo implica verificar que incluya el símbolo “@” y un dominio 
    correcto; validar un nombre evita caracteres numéricos no deseados; validar una contraseña 
    garantiza que tenga una longitud mínima o ciertos caracteres especiales. Por otro lado, la 
    normalización se encarga de dejar el texto en un formato estándar que facilite su almacenamiento
     y comparación.
    Acciones básicas como convertir a minúsculas con .lower(), eliminar espacios sobrantes con 
    .strip(), reemplazar acentos o normalizar mayúsculas ayudan a evitar inconsistencias como 
    duplicados, falta de coincidencias o problemas de búsqueda.

    ¿Que incluye el documento? 
    Este documento explica cómo manejar texto en Python: valida y limpia entradas, define qué 
    datos recibe y qué resultados debe generar, y muestra ejemplos con código usando métodos 
    como .lower(), .upper(), .strip(), .replace(), .split(), .join(), .find(), .startswith() y 
    .endswith() para resolver problemas comunes de procesamiento de texto.

"""

"""
    ================== NOTAS IMPORTANTES SOBRE STRINGS ==================
    - Los strings en Python son inmutables: cualquier modificación crea una nueva cadena.
    - Siempre es buena práctica normalizar entradas con strip() y lower() antes de compararlas.
    - Evitar "números mágicos" en slicing; documentar claramente qué parte del texto se está extrayendo.
    - Usar métodos de string (replace, split, join, startswith, etc.) en lugar de reescribir lógica básica.
    - Diseñar validaciones claras: primero verificar que el texto no esté vacío y luego validar su formato.
    - Mantener el código legible: nombres de variables descriptivos y mensajes de error comprensibles.
     ======================================================================
"""


"""
    Problem 1: FULL NAME FORMATTER 
    Description: 
    Este programa tiene como objetivo que el usuario ingrese el nombre completo de una persona 
    mediante una sola cadena lo que se tiene que realizar es normalizar el texto y mostrar el
    nombre ya formateado en Title caso y las iniciales.

    Inputs:
    - full_name # una sola cadena 

    Outputs:
    - formatted_name
    - initials

    Validations:
    - No puede contener menos de dos palabras ya que no se puede 
    continuar con el formateo.
    - No aceptar espacios en blanco porque no va a tener con algo que
    trabajar 

    Test cases:
    1) Normal: 
    maría jose perez

    Formatted name: María Jose Perez
    Initials: M.J.P.

    2) Border: 
       ana   

    Error: invalid input. It cannot be less than two words.

    3) Error: 
    ""

    Error: invalid input. No blank spaces allowed.
"""
# the user enters their name
full_name = input("Enter yotu full name please: ")

# validate full name solo si contiene espacios 
if full_name.strip() == "":

    # print error for empty input
    print("Error: invalid input. No blank spaces allowed.")
elif len(full_name.strip()) < 2:

    # print error for insufficient words 
    print("Error: invalid input. It cannot be less than two words.")
else:
    # Clean and standardize the text
    formatted_name = " ".join(full_name.strip().title().split())
    
    # generate initials
    initials = ".".join([part[0].upper() for part in formatted_name.split()]) + '.'
    
    print(f"Formatted name: {formatted_name}")
    print(f"Initials: {initials}")



"""
    Problem 2: E-MAIL VALIDATOR 
    Description:
    Se tiene como objetivo en este programa que el usuario ingrese su email y valide 
    que si sea un email mediante el signo "@" y el "." tambien proporcionar el dominio 
    del correo. 


    Inputs:
    - email
    Outputs:
    - valid or not 
    - part2 (domain)

    Validations:
    - No espacios vacios 
    - Que contenga el @ y el .


    Test cases:
    1) Normal:
    email = "paulormzal@gmail.com"


    Valid email: true
    Domain: gmail.com

    2) Border:
    email = "paulo@gmail"

    Valid email: false

    3) Error: 
    email = "   "

    Error: invalid input. You cannot enter only spaces.

"""

# input email
email = input("Enter email address: ")

# validate email structure
if email.strip() == "":

    # print error for empty input 
    print("Error: invalid input. You cannot enter only spaces.")
elif email.count('@') != 1 or " " in email:

    # print invalid email
    print("Valid email: false") 
else:

    # split email into parts
    part1, part2 = email.split("@")

    # validate domain part
    if "." in part2:

        # outpods
        print("Valid email: true")
        print(f"Domain: {part2}")
    else:

        # print invalid email
        print("Valid email: false")



"""
    Problem 3: Palindrome checker
    Description: 
    Este problema tiene como objetivo determinar si una frase es palindromo quiere decir que 
    se lee igual de izquierda a derecha y viceversa ignorando los espacios y si es mayuscula 
    o minuscula.

    Inputs:
    - phrase 
    Outputs:
    - palindrome
    - normal_phrase 

    Validations:
    - phrase no vacia 

    Test cases:
    1) Normal: 
    phrase = "Anita lava la tina"

    Is palindrome: True
    Normalized phrase: anitalavalatina

    2) Border: 
    phrase = "a"

    Is palindrome: True
    Normalized phrase: a

    3) Error: 
    phrase = "     "

    Error: invalid input. You cannot enter only spaces.
"""

# input phrase
phrase = input("Enter a phrase: ")

# validate phrase
if phrase.strip() == "":

    # print error for empty input
    print("Error: invalid input. You cannot enter only spaces.")   
else:

    # normalize phrase
    normal_phrase = "".join(phrase.strip().lower().split())
    
    # check if palindrome
    palindrome = normal_phrase == normal_phrase[::-1]
    
    # outputs 
    print("Is palindrome:" + str(palindrome))
    print(f"Normalized phrase: {normal_phrase}")

"""
    Problem 4: Sentence word stats 
    Description: 
    El usuario ingresa una oracion se normaliza y separa para mostrarle como 
    salida al usuario su numero total de palabras, su primer palabra. su ultima
    palabra y la palabra mas corta y larga.

    Inputs:
    - 

    Outputs:
    - 

    Validations:
    - La oracion no debe de estar vacio tras usar .strip()
    - La entrada debe contener por lo menos una palabra 
    valida.

    Test cases:
    1) Normal:
    sentence = "Hola esta es una oración de prueba"

    Word count:7
    Frist word:Hola
    Last word:prueba
    Shortest word:es
    Longest word:oración
    
    2) Border: 
    sentence = "Programación"

    Word count:1
    Frist word:Programación
    Last word:Programación
    Shortest word:Programación
    Longest word:Programación

    3) Error: 
    sentence = "      "

    Error: invalid input. You cannot enter only spaces.

"""

# input sentence
sentence = input("Enter a sentence: ")

# validate sentence
if sentence.strip() == "":

    # print error for empty input
    print("Error: invalid input. You cannot enter only spaces.")

else:

    # normalize sentence
    normal_sentense = sentence.strip()

    # separate 
    words = normal_sentense.split()

    # outpods 
    print("Word count:"+ str(len(words)))
    print("Frist word:"+ words[0])
    print("Last word:"+ words[-1])
    print("Shortest word:"+ min(words, key=len))
    print("Longest word:"+ max(words, key=len))

"""
    Problem 5: Password strength classifier
    Description: 
    Este programa tiene como objetivo clasificar contraseñas como "weak", "medium o "strong" 
    segun reglas minimas y se pueden afinar segun sea fuerte o mediana de eso dependera que 
    tantas reglas tenga la contraseña 

    Inputs:
    - password  

    Outputs:
    - "Password strength: weak"
    - "Password strength: medium"
    - "Password strength: strong"

    Validations:
    - No aceptar que la contraseña este vacia 
    - Verificar la longitud 

    Test cases:
    1) Normal: 

    2) Border: 

    3) Error: 


"""

# input password
password = (input("Enter a password: "))
password.strip()

if password == "":

    # print error for empty input
    print("Error: invalid input. You cannot enter only spaces.")
elif len(password) < 8 and password.islower() or password.isdigit():
    print("Password strength: weak") #outpod
elif len(password) >= 8 and any(password.islower() 
    for c in password) and any(password.isupper() 
        for c in password) and any(password.isdigit() 
            for c in password) and any(not c.isalnum() 
                for c in password):
    print("Password strength: Strong")
else: # outpod
    print("Password strength: Medium")
        # out pod 
"""
    Problem 6: Product label formatter
    Description: 
    El cliente ingresa el nombre y precio de un producto se genera una etiqueta
    en una sola linea debe de contener exactamente 30 caracteres. Si es mas corta
    se rellenan los espacion pero si es mas larga se recorta hasta los 30 exactos.

    Inputs:
    - product_name
    - price_value 

    Outputs:
    - label 

    Validations:
    - No se encuentre vacio el product_name
    - El precio debe poder convertirse en positivo 

    Test cases:
    1) Normal: 
    name product :Manzana
    price product :12.5

    Product: Manzana
    Price: 12.5
    Label: "Manzana............$  12.50"

    2) Border: 
    name product :Agua
    price product :0

    Product: Agua
    Price: 0
    Label: "Agua................$   0.00"


    3) Error: 
    name product :Chocolate
    price product :-4.99

    Error: invalid input. The price must be a positive number.


"""

product_name = input("name product :")
price_value = (str(input("price product :")))

if product_name.strip() == "":
    print("Error: invalid input. You cannot enter only spaces.")
else:
    try:
        price_float = float(price_value)
        if price_float < 0:
            raise ValueError("Negative price")
        
        label = f"{product_name.strip():.<20}${price_float:>7.2f}"
        # outpods 
        print(f"Product: {product_name}")
        print(f"Price: {price_value}")
        print(f'Label: "{label}"')
    except ValueError:
        print("Error: invalid input. The price must be a positive number.")

"""
    CONCLUSION:
    La verdad me quedo mucho con la importancia de los string para procesar correctamente 
    la entrada y la salida de datos en cualquier programa. Las funciones como lower, strip,
    split y join son convenientes al momento de querer limpiar, normalizar y reorganizar el
    texto para evitar errores. La importancia de normalizar radica en que cualquier diferencia
    por mas minima que sea puede alterar completamente el resultado de nuestro codigo. El diseño
    de las validaciones nos evita que el programa reciba datos inutiles para su realizacion y se 
    pueden detectar errores con facilidad y solo se procesen entradas correctas y utiles. La 
    inmutabilidad de los string significa que cualquier modificacion que se le haga al string genera
    una nueva cadena sin modificar la original. Además, el uso de slices permite extraer partes 
    específicas del texto de manera controlada, siempre que se definan bien los índices.
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
