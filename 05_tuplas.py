### Tuplas ### 

my_tuple = tuple()
my_other_tuple = ()

my_tuple =  (17, 1.77, "Néstor", "Berenguer", "Néstor")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError 

print(my_tuple.count("Néstor"))
print(my_tuple.index("Berenguer"))
print(my_tuple.index("Néstor"))
