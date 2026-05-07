### Operadores Aritméticos ###

print (3 + 4)
print (3 - 4)
print (3 * 4)
print (3 / 4) 
print (10 % 3) 
print (10 // 3) 
print (10 ** 3)

print("Hola " + "Python " + "¿Qué tal?")
print("Hola " + str(5))
print("Hola " * 5)
print("Hola " * (2 ** 3))

my_float = 2.5 * 2
print("Hola " * int(my_float))

### Operadores Comparativos ###

print (3 > 4)
print (3 < 4)
print (3 >= 4)
print (3 <= 4)
print (3 == 4)
print (3 != 4)

#! Aquí no comprueba la cantidad de carácteres, comprueba la ordenación alfabética
print ("Hola" > "Python")
print ("Hola" < "Python")
print ("Hola" >= "Python")
print (len("Hola") >= len("Python")) #? Aquí si compruebo por el número de caracteres
print ("Hola" <= "Python")
print ("Hola" == "Hola")
print ("Hola" != "Python")

### Operadores Lógicos ### 

print (3 > 4 and "Hola" > "Python") # &&
print (3 > 4 or "Hola" > "Python") # ||
print (3 < 4 and "Hola" < "Python") 
print (3 < 4 or "Hola" < "Python") 
print (3 < 4 or "Hola" > "Python" and 4 == 4) 
print (not(3 > 4))