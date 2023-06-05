
# # def modificar_valor(valor):
# #     valor= 10
# #     num = 25
# #     print('valor de funcion',valor)
# #     print('valor de num funcion',num)
# #     return valor

# # def saludar():
# #     print('Hola')


# # # Prog Principal
# # valor = 5
# # valor = modificar_valor(valor)
# # print('Valor:',valor)
# # print(num)

# # Tiene parametro opcional
# # El que tiene = es opcional
# def sumar(a,z=8,b=5):
#     sumar = a + b + z
#     print(sumar)

# # No tiene parametro opcional
# # Tengo que pasar todos los parametros
# def sumar2(a,x,b):
#     sumar = a + b + x
#     print(sumar) 

# sumar(5,1)
# sumar2(5,4,3)

# parametros mutables e inmutables
# Parametros mutables, una lista o un diccionario
# parametros inmutables, un entero o una cadena 

# def modificar_lista(lista):
#     lista.append(4)

# # Prog principal
# lista = [1,2,3]
# modificar_lista(lista)
# print(lista)

# Funciones lambda/anonimas
# def doble(x):
#     return x*2
# doble = lambda x: x*2
# print(doble(5))


# funciones con retorno de multiples valores
def dividir(a,b):
    cociente = a // b
    resto = a % b
    return cociente, resto

resultado = dividir(10,3)
print(resultado) #(3,1)
