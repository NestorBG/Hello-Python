### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #! Inicialmente es un diccionario 

my_other_set = {"Néstor", "Berenguer", 17}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("NesttorBG")

print(my_other_set) #? Un set no es una estructura ordenada

my_other_set.add("NesttorBG") #? Un set no admite repetidos

print(my_other_set)

print("Berenguer" in my_other_set) #* comprueba si está el elemento en el set
print("Puta" in my_other_set)

my_other_set.remove("Berenguer")
print(my_other_set)

my_other_set.clear()
print(my_other_set)

del my_other_set
#* print(my_other_set) No va a estar definido porque nos lo hemos cargado 

my_set = {"Néstor", "Berenguer", 17}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"CSS", "JAVA", "PYTHON"}

my_new_set = my_set.union(my_other_set).union({"HTML", "JavaScript"}) #? Como una suma de sets
print(my_new_set)

print(my_new_set.difference(my_set))