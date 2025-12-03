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
    - initial_items_text
    - new_item
    - search_item

    Outputs:
    - Items list
    - Total items:
    - Found item:


    Validations:
    - Validar lista inicial vacía
    - Eliminar espacios y descartar ítems vacíos
    - Validar que new_item y search_item no estén vacíos

    Test cases:
    1) Normal:
    Enter initial items (separed by a comma): apple, banana, orange
    Enter new item: mango
    Enter item to search: banana

    Items list: ['apple', 'banana', 'orange', 'mango']
    Total items: 4
    Found item: true

    2) Border: 
    Enter initial items (separed by a comma): apple
    Enter new item: kiwi
    Enter item to search: apple

    Items list: ['apple', 'kiwi']
    Total items: 2
    Found item: true

    3) Error:
    Enter initial items (separed by a comma):
    Enter new item: kiwi
    Enter item to search: apple

    Error: invalid input

"""

initial_items_text = input("Enter initial items (separed by a comma): ").strip()
new_item = input("Enter new item: ").strip()
search_item = input("Enter item to search: ").strip()

# Validation for initial text
if initial_items_text == "":
    print("Error: invalid input")
else:
    # Convert text to list
    items_list = initial_items_text.split(",")
    
    # Del spaces
    cleaned_list = []
    for item in items_list:
        cleaned_item = item.strip()
        if cleaned_item != "":
            cleaned_list.append(cleaned_item)
    
    # Validate new and search items
    if new_item == "" or search_item == "":
        print("Error: invalid input")
    else:
        # Append new item
        cleaned_list.append(new_item)
        
        # Total items
        total_items = len(cleaned_list)
        
        # Check if search item exists
        is_in_list = search_item in cleaned_list
        
        # Output
        print("Items list:", cleaned_list)
        print("Total items:", total_items)
        print("Found item:", str(is_in_list).lower())



print("---------------SECOND PROBLEM-------------------")
"""
    Problem 2: Points and distances with tuples 
    Description: 
    Primero el usuario debe de ingresar unas coordenadas de dos puntos para 
    que con este programa calcular la distancia entre ambos puntos y asi crear
    una nueva tupla con el punto medio.

    Inputs:
    - x1 
    - x2 
    - y1
    - y2 

    Outputs:
    - point_a
    - point_b
    - distance
    - midpoint 

    Validations:
    - Verificar que las 4 entradas se puedan convertir a float.
    - No se requieren restricciones adicionales en el rango.

    Test cases:
    1) Normal: 
    Enter x1: 2
    Enter y1: 3
    Enter x2: 6
    Enter y2: 9

    Point A: (2.0, 3.0)
    Point B: (6.0, 9.0)
    Distance: 7.211102550927978
    Midpoint: (4.0, 6.0)

    2) Border: 
    Enter x1: 4
    Enter y1: 4
    Enter x2: 4
    Enter y2: 4

    Point A: (4.0, 4.0)
    Point B: (4.0, 4.0)
    Distance: 0.0
    Midpoint: (4.0, 4.0)

    3) Error: 
    Enter x1: 2
    Enter y1: hola
    Enter x2: 5
    Enter y2: 8

    Error: Invalid numeric input.

"""

try:
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
# Create tuples
    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

    midpoint = ((x1 + x2)/2, (y1 + y2)/2)
    # Output
    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", distance)
    print("Midpoint:", midpoint)
    # print error 
except ValueError:
    print("Error: Invalid numeric input.")



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
    - product_name
    - quantity_input 

    Outputs:
    - unit_price
    - quantity 
    - total_price

    Validations:
    - quantity > 0.
    - product_name no vacío tras strip().
    - Verificar si product_name está en el diccionario (clave).


    Test cases:
    1) Normal: 
    Enter product name (coke, eggs or chip's): eggs
    Enter quantity: 3

    Unit price: 25.0
    Quantity: 3
    Total: 75.0

    2) Border: 
    Enter product name (coke, eggs or chip's): coke
    Enter quantity: 1

    Unit price: 15.0
    Quantity: 1
    Total: 15.0

    3) Error: 
    Enter product name (coke, eggs or chip's): bread
    Enter quantity: 2

    Error: product not found

"""
# Create product catalog
product_prices = {"coke": 15.0, "eggs": 25.0, "chip's": 35.0}
# Read inputs
product_name = input("Enter product name (coke, eggs or chip's): ").strip()
quantity_input = input("Enter quantity: ")

try: # Convert quantity to int
    quantity = int(quantity_input)

    if product_name == "":
        print("Error: product name cannot be empty.")
    elif quantity <= 0:
        print("Error: quantity must be greater than 0.")
    else:
        if product_name in product_prices:
            unit_price = product_prices[product_name]
            total_price = unit_price * quantity
            # Output
            print("Unit price:", unit_price)
            print("Quantity:", quantity)
            print("Total:", total_price)
        else:
            print("Error: product not found")
        # print error
except ValueError:
    print("Error: quantity must be a number.")


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
    - student_name

    Outputs:
    - grades_list
    - average
    - is_passed 

    Validations:
    - student_name no vacío tras strip().
    - Verificar si student_name es una clave en el diccionario.
    - Verificar que la lista de calificaciones no esté vacía antes de calcular el promedio.

    Test cases:
    1) Normal: 
    Enter student name (yomerito, geragod, vitor): geragod

    Grades: [100.0, 98.0, 80.0]
    Average: 92.66666666666667
    Passed: True

    2) Border:
    Enter student name (yomerito, geragod, vitor): vitor

    Grades: [55.0, 65.0, 50.0]
    Average: 56.666666666666664
    Passed: False
 
    3) Error: 
    Enter student name (yomerito, geragod, vitor): pedrito

    Error: student not found
"""
# Create student grades dictionary
student_grades = {"yomerito": [95.0, 85.0, 92.0], "geragod": [100.0, 98.0, 80.0],
"vitor": [55.0, 65.0, 50.0]}

student_name = input("Enter student name (yomerito, geragod, vitor): ").strip().lower()
 # Validate student name
if student_name == "":
    print("Error: no student name")
else:
    if student_name in student_grades:
        grades_list = student_grades[student_name]

        if len(grades_list) == 0:
            print("Error: this student has no grades.")
        else:
            average = sum(grades_list) / len(grades_list)
            is_passed = average >= 70.0
            # Output
            print("Grades:", grades_list)
            print("Average:", average)
            print("Passed:", is_passed)
    else:
        print("Error: student not found")


print("---------------FIFTH PROBLEM-------------------")
"""
    Problem 5: Word frequency counter
    Description: 
    Contar la frcuencia de cada palabra en una oracion se usan listas y diccionarios
    con la palabra y su frecuencia. Debe de leer una oracion y se normaliza convirtiendola
    en minuscula se separa en una lista y construye un diccionario de frecuencias. Se le
    muestra al usuario el diccionario y la palabra mas frecuente.

    Inputs:
    - sentence 

    Outputs:
    - words_list 
    - freq_dict
    - most_common_word

    Validations:
    - sentence no vacía tras strip().
    - Manejar signos de puntuación simples si el estudiante decide hacerlo (documentar su decisión, por ejemplo usando replace()).
    - Verificar que la lista de palabras no esté vacía.

    Test cases:
    1) Normal: 
    Enter a sentence: Hello world, hello again!

    Words list: ['hello', 'world', 'hello', 'again']
    Frequencies: {'hello': 2, 'world': 1, 'again': 1}
    Most common word: hello

    2) Border: 
    Enter a sentence: ...Hello???

    Words list: ['hello']
    Frequencies: {'hello': 1}
    Most common word: hello

    3) Error: 
    Enter a sentence: 

    Error: there isn't a sentence.
"""

sentence = input("Enter a sentence: ").strip()
# Validate sentence
if sentence == "":
    print("Error: there isn't a sentence.")
else:
    clean_text = sentence.lower()
    clean_text = clean_text.replace(".", "")
    clean_text = clean_text.replace(",", "")
    clean_text = clean_text.replace("!", "")
    clean_text = clean_text.replace("?", "")
 # Split into words
    words_list = clean_text.split()

    if len(words_list) == 0:
        print("Error: no words found.")
    else:
        freq_dict = {}

        for word in words_list:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1

        # FIND THE COMMUN WORD
        most_common_word = ""
        highest_count = 0

        for word in freq_dict:
            if freq_dict[word] > highest_count:
                highest_count = freq_dict[word]
                most_common_word = word
        # Output
        print("Words list:", words_list)
        print("Frequencies:", freq_dict)
        print("Most common word:", most_common_word)


print("---------------SIXTH PROBLEM-------------------")
"""
    Problem 6: Simple contact book
    Description: 
    Se tiene como objetivo implementar un mini libro de contactos con ayuda de un diccionario
    tiene que tener el nombre del contacto y su telefono. Se tiene que leer una accion son tres
    add, search y delete en si agregar buscar y eliminar y mostrar un mensaje de resultado 
    dependiendo de la operacion que el usuario desea realizar. 

    Inputs:
    - action_name
    - name
    - phone

    Outputs:
    - ADD
    - SEARCH
    - DELETE

    Validations:
    - Validación de la acción ingresada
    - Validación del nombre del contacto
    - Validación del teléfono (solo cuando se usa ADD)
    - Validación de existencia del contacto (SEARCH y DELETE)

    Test cases:
    1) Normal: 
    Enter action (ADD, SEARCH, DELETE): SEARCH
    Enter contact name (AMLO, Juniorh, vegetta): AMLO

    Phone: 8345625310

    2) Border: 
    Enter action (ADD, SEARCH, DELETE): ADD
    Enter contact name (AMLO, Juniorh, vegetta): Goku
    Enter phone number: 1234567890

    Contact saved: Goku 1234567890

    3) Error: 
    Enter action (ADD, SEARCH, DELETE): CALL

    Error: invalid action.
"""
# Create contact book dictionary
contacts = {
    "AMLO": "8345625310",
    "Juniorh": "8346569217",
    "vegetta": "8347777777"
}

action_text = input("Enter action (ADD, SEARCH, DELETE): ").strip().upper()
# Validate action
if action_text not in ["ADD", "SEARCH", "DELETE"]:
    print("Error: invalid action.")
else:
    name = input("Enter contact name (AMLO, Juniorh, vegetta): ").strip()

    if name == "":
        print("Error: name cannot be empty.")
    else:
        if action_text == "ADD":
            phone = input("Enter phone number: ").strip()

            if phone == "":
                print("Error: phone cannot be empty.")
            else:
                contacts[name] = phone
                print("Contact saved:", name, phone)

        elif action_text == "SEARCH":
            if name in contacts:
                print("Phone:", contacts[name])
            else:
                print("Error: contact not found")
  
        elif action_text == "DELETE":
            if name in contacts:
                contacts.pop(name)
                print("Contact deleted:", name)
            else:
                print("Error: you need learn to write correct")

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
    REFERENCIAS:
    1) Python Software Foundation. (2024). List — Sequence Type.
    https://docs.python.org/3/tutorial/introduction.html#lists
    2) Python Software Foundation. (2024). Mutable Sequence Types — list.
    https://docs.python.org/3/library/stdtypes.html#list
    3) Python Software Foundation. (2024). Tuples — Sequence Type.
    https://docs.python.org/3/library/stdtypes.html#tuple
    4) Python Software Foundation. (2024). 5.3 Tuples and Sequences.
    https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
    5) Python Software Foundation. (2024). Mapping Types — dict.
    https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

"""

"""
    REPOSITORIO GIT HUB:
    https://github.com/Paulo-ram/homework_charly-
"""