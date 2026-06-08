### Condicionales ###

my_condition = False

if my_condition: #? Si no se cumple la condición no se ejecuta el if, normalmente un true
    print("Se ejecuta la condición del if")

my_condition = 5*3

if my_condition == 10:
    print("Se ejecuta la condición del segundo if")

if my_condition > 10 and my_condition < 20:
    print("es mayor que 10 y menor que 20")
elif my_condition == 1:
        print("es igual a 1")
else:
    print("es menor o igual que 10 o mayor o igual que 20")


print("es menor o igual que 10 o mayor o igual que 20")

print("La ejecución continúa")

my_string = "Mi cadena de texto"

if not my_string:
    print("My cadena de texto no es vacía") 

if my_string == ("Mi cadena de textoo"):
    print("Estas cadenas de texto coinciden")  
