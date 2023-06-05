class Producto:
    # atributos: id,nombre y precio
    def __init__(self,id,nombre,precio,stock=0):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f'Producto {self.id}: {self.nombre} - Precio: {self.precio:.2f} - Stock: {self.stock}'

    def modificar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
    
    def modificar_stock(self,cantidad):
        self.stock -= cantidad

def agregar_producto(lista,producto):
    lista.append(producto)

def modificar_producto(lista,id_prod,nuevo_precio):
    for producto in lista:
        if producto.id == id_prod:
            producto.modificar_precio(nuevo_precio)
            break


# Lista para almancer productos
lista_producto = []

# crear productos y agregarlos a la lista
prod1 = Producto(1,'Remeras', 5500, 10)
agregar_producto(lista_producto,prod1)

prod2 = Producto(2,'Pantalon', 8999.99,5)
agregar_producto(lista_producto,prod2)

prod3 = Producto(3,'Zapatos', 13459.85)
agregar_producto(lista_producto,prod3)

prod4 = Producto(4,'Zapatillas', 43459, 2)
agregar_producto(lista_producto,prod4)


for producto in lista_producto:
    print(producto)

modificar_producto(lista_producto,2,18555)

print('Lista con precios actualizados')
for producto in lista_producto:
    print(producto)
