# Variables

my_string_variable = "Este es mi String"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_srt_variable = str(my_int_variable)
print(my_int_to_srt_variable)
print(type(my_int_to_srt_variable))

my_bool_variable = True
print(my_bool_variable)

print(my_string_variable, my_int_to_srt_variable, my_bool_variable)
print("Este es el valor de: ", my_bool_variable)

#Algunas funciones del sistema
print(len(my_string_variable)) # Cuenta los carácteres 

# Variables en una sola línea
name, surname, alias, age = "Néstor", "Berenguer", "Nesttorbg", 17
print ("Me llamo",name, surname, "Tengo", age,"años Y mi alias es:", alias)

# Inputs
""""
firs_name= input("¿Cuál es tu nombre? ")
edad = input("¿Cuántos años tienes? ")

print(name)
print(age)
"""

#Cambiando el tipo de variable
name = 17
age = "Nestor"
print(name)
print(age)

#Forzar el tipo de variable
address: str = "Mi dirección"
address = 32
print(type(address))