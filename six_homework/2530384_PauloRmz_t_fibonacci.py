# PROBLEMA UNICO DE PYTHON SERIE FIBONACCI 

"""
    NOMBRE DEL ALUMNO: PAULO RAMIREZ ALVAREZ
    MAESTRO: CHARLY MERCURY
    MATRICULA: 2530384 
    GRUPO: 1-1 IM 
"""

"""
    REUMEN EJECUTIVO: 

"""

print("---------------FIBONACCI SERIES-------------------")
"""
    PROBLEM : Fibonacci series up to n terms
    Description: 

    Inputs:
    - num 

    Outputs:
    - sum 

    Validations:
    - 

    Test cases:
    1) Normal: 
    2) Border: 
    3) Error: 

"""

print("Welcome to the fibonacci sequence")
try: 
    num = int(input("How many values do you want?: "))
    if num>1 and num<35:
        a = 0
        b = 1
        sum = 0 
        count = 1
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


"""


"""
    REFRENCIAS:
    1) 
    2) 
    3) 

"""

"""
    REPOSITORIO GIT HUB:

"""