### Listas ###      

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [17, 1.77, "Néstor", "Berenguer"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0]) # Para imprimir el elemento de la lista que indiques
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_list.count(30))
#print(my_other_list[4]) IndexError
#print(my_other_list[-5]) IndexError

age, heigh, name, surname = my_other_list
print(name)

name, heigh, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

print(my_list + my_other_list)
#print(my_list - my_other_list)

my_other_list.append("NesttorBG") #Añade al final un elemento
print(my_other_list)

my_other_list.insert(1, "rojo")  # Añade donde tu quieras el elemento
print(my_other_list)

my_other_list[1] = "azul" # Sustituir valores
print(my_other_list)

my_other_list.remove("azul") # Elimina el elemento
print(my_other_list)

my_list.remove(30) #Si el elemento está repetido elimina el primero
print(my_list)

print(my_list.pop()) # Elimina el último elemento
print(my_list)

my_pop_element = my_list.pop(2) # Elimina el elemento que indiques
print(my_pop_element)
print(my_list)

del my_list[2] # borrar elementos y elimina elementos aunque no sepas el elemento que es 
print(my_list)

my_new_list = my_list.copy() # ha copiado el objeto literalmente 

my_list.clear()
print(my_list)

my_new_list.reverse() # Le da la vuelta a la lista literalmente 
print(my_new_list) 

my_new_list.sort() # ordena la lista de mayor a menor y mediante tipos de variable
print(my_new_list)

print(my_new_list[1:3])

my_list = "Hola Python" # Cambia de tipo de lista a str
print(my_list)
print(type(my_list))