# MANEJOS DE STRING EN PYTHON 
"""
    NOMBRE DEL ALUMNO: PAULO RAMIREZ ALVAREZ
    MAESTRO: CHARLY MERCURY
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
    Se tiene como objetivo en este programa 

    Inputs:
    - ...

    Outputs:
    - ...

    Validations:
    - ...

    Test cases:
    1) Normal: ...
    2) Border: ...
    3) Error: ...

"""


"""
    Problem X: <short title>
    Description: 2–4 lines explaining what the program does.

    Inputs:
    - ...

    Outputs:
    - ...

    Validations:
    - ...

    Test cases:
    1) Normal: ...
    2) Border: ...
    3) Error: ...

"""


"""
    Problem X: <short title>
    Description: 2–4 lines explaining what the program does.

    Inputs:
    - ...

    Outputs:
    - ...

    Validations:
    - ...

    Test cases:
    1) Normal: ...
    2) Border: ...
    3) Error: ...

"""


"""
    Problem X: <short title>
    Description: 2–4 lines explaining what the program does.

    Inputs:
    - ...

    Outputs:
    - ...

    Validations:
    - ...

    Test cases:
    1) Normal: ...
    2) Border: ...
    3) Error: ...

"""


"""
    Problem X: <short title>
    Description: 2–4 lines explaining what the program does.

    Inputs:
    - ...

    Outputs:
    - ...

    Validations:
    - ...

    Test cases:
    1) Normal: ...
    2) Border: ...
    3) Error: ...

"""


"""
    CONCLUSION:
    La verdad me quedo mucho con la importancia de 

"""


"""
    REFRENCIAS:

"""

"""
    REPOSITORIO GIT HUB:

"""
