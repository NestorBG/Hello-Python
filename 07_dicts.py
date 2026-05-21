### Diccionarios ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Néstor", "Apellido":"Berenguer", "Edad":17, 1:"Python"}

my_dict = {
    "Nombre":"Néstor", 
    "Apellido":"Berenguer", 
    "Edad":17, 
    "Lenguajes": {"Python", "HTML", "Java"},
    1:1.77
    }

print(my_dict)
print(my_other_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedro" #? Cambiar valor a elemento
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Calle RamonyCajal"
print(my_dict)

del my_dict["Calle"] #? Eliminar elemento
print(my_dict) 

print("Berenguer" in my_dict) #! Aquí estamos buscando por clave no por valor, FALSE 
print("Apellido" in my_dict) #? TRUE 

print(my_dict.items()) #? Te da un listado de todos los elementos
print(my_dict.keys()) #? Aquí solo te devuelve el nombre de las llaves 
print(my_dict.values()) #? Y aquí solo el valor que llevan dentro las llaves

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys(my_list) #* Te crea un diccionario vacio, sin los datos
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, ("Néstor", "Berenguer"))
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))

print(list(my_new_dict)) #? Aquí solo tenemos las claves
print(tuple(my_new_dict))
print(set(my_new_dict))