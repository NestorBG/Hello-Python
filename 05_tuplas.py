### Tuplas ### 

my_tuple = tuple()
my_other_tuple = ()

my_tuple =  (17, 1.77, "Néstor", "Berenguer", "Néstor")
my_other_tuple = (35, 17, 30,)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#* print(my_tuple[4]) IndexError
#* print(my_tuple[-6]) IndexError 

print(my_tuple.count("Néstor")) #? Cuenta cuantos elementos hay iguales
print(my_tuple.index("Berenguer")) #? Dime el índice donde está el elemento
print(my_tuple.index("Néstor")) #? Si hay varios dice el primero que haya

#! my_tuple[1] = 1,80 No deja ni cambiar ni añadir datos

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6]) #? Slice 

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "NesttorBG"
my_tuple.insert (1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))
