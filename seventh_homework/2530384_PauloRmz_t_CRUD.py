# PROBLEMA UNICO CRUD EN PYTHON

"""
    NOMBRE DEL ALUMNO: PAULO RAMIREZ ALVAREZ
    MAESTRO: CHARLY MERCURY
    MATRICULA: 2530384 
    GRUPO: 1-1 IM 
"""

"""
    RESUMEN EJECUTIVO: 
    Un CRUD es un programa que permite gestionar datos mediante cuatro acciones: Create (crear), Read (leer), 
    Update (actualizar) y Delete (eliminar). Se usa un diccionario o una lista de diccionarios porque facilita 
    organizar y acceder a la información rápidamente. Utilizar funciones ayuda a separar cada parte del CRUD, 
    hacer el código más claro y evitar repeticiones. El programa incluye un menú principal y permite realizar 
    todas las operaciones: creación, lectura, actualización, eliminación y también mostrar el listado completo 
    de elementos.
"""

print("---------------CRUD PROBLEM-------------------")
"""
    Problem: In-memory CRUD manager with functions  

    Descripción:
    Se debe de realizar el CRUD (Create, Read, Update, Delete) utilizando funciones y un diccionario o lista de diccionarios 
    para almacenar los datos en memoria. El programa debe permitir al usuario crear, leer, actualizar y eliminar elementos, 
    así como listar todos los elementos almacenados. Se debe implementar un menú principal para seleccionar las operaciones.
    
    Inputs:

    - options
    - item_id 
    - name
    - price 
    - quantity

    Outputs:
    
    - Confirmation messages for each operation (e.g., "Item created", "Item updated", "Item deleted").
    - Error messages for invalid inputs (e.g., "Error: invalid input", "Item not found").
    - List of all items when requested.

    Validations:
    - Menu option must be valid (1-5, 0 to exit).
    - item_id must not be empty. 
    - Numeric fields must be valid numbers and greater than or equal to 0.
    - Disallow creating an item with an id that is already in use (or document tu decisión).
    - For READ/UPDATE/DELETE, if the id does not exist, show "Item not found".

    Test cases:
    1) Normal: 

    1) Create  2) Read  3) Update 4) Delete 5) List 0) Exit
    Choose your option: 1 
    ID: 142536
    Name: Milk
    Price: 12.5
    Quantity: 1
    Item created

    1) Create  2) Read  3) Update 4) Delete 5) List 0) Exit
    Choose your option: 2
    ID: 142536
    {'name': 'Milk', 'price': 12.5, 'quantity': 1}

    1) Create  2) Read  3) Update 4) Delete 5) List 0) Exit
    Choose your option: 4
    ID: 142536
    Item deleted

    2) Border: 
    
    1) Create  2) Read  3) Update 4) Delete 5) List 0) Exit
    Choose your option: 1
    ID: a
    Name: Bread 
    Price: 15.5
    Quantity: 2

    Item created

    1) Create  2) Read  3) Update 4) Delete 5) List 0) Exit
    Choose your option: 1

    ID: A1
    Name: Water
    Price: 10
    Quantity: 0

    Item created

    3) Error: 

    1) Create  2) Read  3) Update 4) Delete 5) List 0) Exit
    Choose your option: 6
    Error: invalid input

    1) Create  2) Read  3) Update 4) Delete 5) List 0) Exit
    Choose your option: 1
    ID: 14
    Name: qa
    Price: awe
    Quantity: q
    Error: invalid input

"""

# ----------- FUNCIONES CRUD -----------

def create_item(data, item_id, name, price, quantity):
    if item_id in data:
        return False
    data[item_id] = {"name": name, "price": price, "quantity": quantity}
    return True

def read_item(data, item_id):
    return data.get(item_id)

def update_item(data, item_id, name, price, quantity):
    if item_id not in data:
        return False
    data[item_id] = {"name": name, "price": price, "quantity": quantity}
    return True

def delete_item(data, item_id):
    return data.pop(item_id, None) is not None

def list_items(data):
    if not data:
        print("There are no items.")
    else:
        for i, d in data.items():
            print(f"ID: {i} | {d}")

# VALIDATIONS 

def val_float(v):
    try: v=float(v); return v if v>=0 else None
    except: return None

def val_int(v):
    try: v=int(v); return v if v>=0 else None
    except: return None

# PRINCIPAL MENU 

print("Welcome to the HEB packet page") 

def main():
    items = {}
    while True:
        print("\n1) Create  2) Read  3) Update 4) Delete 5) List 0) Exit")
        option = input("Choose your option: ").strip()

        if option == "0":
            print("LEAVING..."); break
        
        if option not in {"1","2","3","4","5"}:
            print("Error: invalid input"); continue

        if option == "1":  # CREATE
            item_id = input("ID: ").strip()
            if not item_id: print("Error: invalid input"); continue
            name = input("Name: ")
            price = val_float(input("Price: "))
            quantity = val_int(input("Quantity: "))
            if price is None or quantity is None:
                print("Error: invalid input"); continue
            print("Item created" if create_item(items, item_id, name, price, quantity)
                  else "Error: ID already exists")

        elif option == "2":  # READ
            item = read_item(items, input("ID: ").strip())
            print(item if item else "Item not found")

        elif option == "3":  # UPDATE
            item_id = input("ID: ").strip()
            if item_id not in items:
                print("Item not found"); continue
            name = input("New name: ")
            price = val_float(input("New price: "))
            quantity = val_int(input("New quantity: "))
            if price is None or quantity is None:
                print("Error: invalid input"); continue
            update_item(items, item_id, name, price, quantity)
            print("Item updated")

        elif option == "4":  # DELETE
            print("Item deleted" if delete_item(items, input("ID: ").strip())
                  else "Item not found")

        elif option == "5":  # LIST
            print("Items list:")
            list_items(items)
            print("End of list")

if __name__ == "__main__":
    main()


"""
    CONCLUSION:
    El uso de funciones facilitó mucho la implementación del CRUD porque permitió separar la lógica en partes claras 
    y manejables. Utilizar un diccionario o una lista de diccionarios hizo más sencillo organizar, buscar y actualizar 
    los datos de forma eficiente. Durante el desarrollo surgieron problemas de validación, como entradas vacías o valores 
    incorrectos, y estos se resolvieron agregando verificaciones y mensajes de error. Este CRUD podría crecer hacia un 
    sistema más completo incorporando almacenamiento en archivos, uso de formatos como JSON o incluso conectándolo a una 
    base de datos para manejar información de manera profesional.

"""


"""
    REFERENCIAS:
    1) Real Python. (2024). Using SQLite Databases in Python.
    (Contiene ejemplos CRUD completos)
    https://realpython.com/python-sqlite-sql-databases/
    2) Programiz. Python File I/O (Create, Read, Write, Delete)
    https://www.programiz.com/python-programming/file-operation
    3) Django Software Foundation. (2024). Django Docs – Model CRUD Operations
    https://docs.djangoproject.com/en/dev/topics/db/queries/

"""

"""
    REPOSITORIO GIT HUB:
    https://github.com/Paulo-ram/homework_charly-
"""