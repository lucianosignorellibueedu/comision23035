# cadena = 'Hola, Mundo!'

# upper(): Convierte a mayuscula
# lower(): Convierte a minuscula
# split(): Divide la cadena de caracteres 
# strip(): elimina los espacios en blanco al principio y final
#len(): retorna la longitud

# print("Upper", cadena.upper())
# print("lower", cadena.lower())
# print("split", cadena.split(','))
# print("strip", cadena.strip())
# print("LEN", len(cadena))
# print("Rebanada",cadena[6:11])
# cadena = '-'.join(cadena)
# print(cadena)
# cadena = 'Hola, Mundo!'
# pos= cadena.find("Mundo")
# print(pos) # 6
# posrfind= cadena.rfind("Mundo")
# print(posrfind) # 6

# nombre = 'Luciano'
# edad = 30
# print(f'Mi nombre es: {nombre} y tengo {edad} años.')


# # LISTAS
# lista = [1,4,3,5,6,2,3]

# lista.append(9)

# print(lista)

# lista.remove(3)

# print(lista)
# lista.sort()
# print(lista)

# print(lista[3])

# # Mostrar un elemento de derecha a izquierda
# print(lista[-2])

# nombres = ['Juan','Maria','Luisa','Pedro','Roman']
# n1, n2, n3, n4, n5 = nombres
# print(n1) #print(nombres[0])
# print(n2) #print(nombres[1])
# print(n3)
# # insert(<pos>, <elemento>) inserta
# nombres.insert(4,'Marcos')
# print(nombres)
# # pop(<posición>)
# nombres.pop(1)
# print(nombres)

# print(nombres)
# nombres.sort(reverse=True)
# print(nombres)
# nombres.clear()



# DICCIONARIOS
# Los diccionarios son colecciones no ordenadas de pares clave-valor. Puedes acceder a los valores utilizando las claves. Algunos métodos comunes de los diccionarios incluyen:
# keys(): Devuelve una lista con todas las claves del diccionario.
# values(): Devuelve una lista con todos los valores del diccionario.
# items(): Devuelve una lista de tuplas (clave, valor) que representan los pares clave-valor del diccionario.

diccionario = {"nombre": "Juan", "edad": 30}
claves = diccionario.keys()
print(claves)  # ['nombre', 'edad']

valores = diccionario.values()
print(valores)  # ['Juan', 30]

items = diccionario.items()
print(items)  # [('nombre', 'Juan'), ('edad', 30)]

# Iterar sobre las claves y valores de un diccionario
diccionario = {"nombre": "Juan", "edad": 30}
for clave, valor in diccionario.items():
    print(clave, valor)

# Comprobar si una clave existe en un diccionario
if "nombre" in diccionario:
    print("La clave 'nombre' existe en el diccionario")

# Obtener el valor de una clave o un valor predeterminado si la clave no existe
valor = diccionario.get("apellido", "Desconocido")
print(valor) 


# # Tuplas:
# # Las tuplas son colecciones ordenadas e inmutables de elementos. No puedes modificar los elementos de una tupla después de su creación. Algunos métodos comunes de las tuplas incluyen:
# # count(): Devuelve el número de veces que aparece un elemento en la tupla.
# # index(): Devuelve el índice de la primera aparición de un elemento en la tupla.



tupla = (1, 2, 3, 1, 4)
conteo = tupla.count(1)
print(conteo)  # 2

indice = tupla.index(3)
print(indice)  # 2


# # Conjuntos:
# # Los conjuntos son colecciones no ordenadas y sin elementos duplicados. Puedes realizar operaciones como unión, intersección y diferencia entre conjuntos. Algunos métodos comunes de los conjuntos incluyen:
# # add(): Agrega un elemento al conjunto.
# # remove(): Elimina un elemento del conjunto.
# # union(): Devuelve un nuevo conjunto que es la unión de dos conjuntos.
# # intersection(): Devuelve un nuevo conjunto que es la intersección de dos conjuntos.
# # difference(): Devuelve un nuevo conjunto que es la diferencia entre dos conjuntos.

conjunto = {1, 2, 3}
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

conjunto1.add(6)
print(conjunto1)  # {1, 2, 3, 6}

conjunto1.remove(2)
print(conjunto1)  # {1, 3, 6}

union = conjunto1.union(conjunto2)
print(union)  # {1, 3, 4, 5, 6}

interseccion = conjunto1.intersection(conjunto2)
print(interseccion)  # {3}

diferencia = conjunto1.difference(conjunto2)
print(diferencia)  # {1, 6}