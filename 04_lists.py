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
print(my_other_list.count("Nestor"))
#print(my_other_list[4]) IndexError
#print(my_other_list[-5]) IndexError