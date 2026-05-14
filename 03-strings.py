### Strings ###

my_string = "Mi string"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + ", " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea "
print(my_new_line_string)

my_tab_string = "Este es un String\tcon tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String con \\n escapado"
print(my_scape_string)

#? Formateo

name, surname, age = "Néstor", "Berenguer", 17

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) 
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

#? Desempaqueado de caracteres
language= "Python"
a, b, c, d, e, f = "Python" 
print(a)
print(b)

#? Division

language_slice = language [1:3] # Del 1 al 3 pero sin coger el 3
print(language_slice)

language_slice = language [1:] #Del 1 hasta que acabe 
print(language_slice)

language_slice = language [-2] #La segunda desde el final 
print(language_slice)

language_slice = language [0:6:2] #La segunda desde el final 
print(language_slice)

#? Reverse

reversed_language = language [::-1] # Te lo imprime todo al reves
print(reversed_language)

#? Funciones

print(language.capitalize()) # Primera en mayúscula
print(language.upper()) # en mayúscula todo 
print(language.count("t")) # Cuantas veces tiene ese caracter 
print(language.isnumeric()) # pregunta si es númerico
print("1".isnumeric()) # Es númerico aun que sea un String
print(language.lower()) # Todas minúsculas 
print(language.upper().isupper) 