from abc import ABC, abstractmethod

#class producto abrstacto
class Producto(ABC):
    def __init__(self,nombre,descripcion,categoria):
        self._nombre = nombre
        self._descripcion = descripcion
        self._categoria = categoria
    
    @property
    def nombre(self):
        return self._nombre

    @property
    def descripcion(self):
        return self._descripcion
    
    @property
    def categoria(self):
        return self._categoria
    
    @abstractmethod
    def calcular_precio(self):
        pass

#Clase cliente
class Cliente:
    def __init__(self,nombre,nro_socio,forma_pago) -> None:
        self._nombre = nombre
        self._nro_socio = nro_socio
        self._forma_pago = forma_pago

    @property
    def nombre(self):
        return self._nombre

    @property
    def nro_socio(self):
        return self._nro_socio

    @property
    def forma_pago(self):
        return self._forma_pago

#Clase del Carrito de compras
class CarritoDeCompras:
    def __init__(self,cliente):
        self._cliente = cliente
        self._productos = [] 
    
    def agregar_producto(self,producto):
        self._productos.append(producto)

    def calcular_total(self):
        total = 0
        try:
            for producto in self._productos:
                total += producto.calcular_precio()
            if self._cliente.forma_pago == 'efectivo':
                total *= 0.9 #aplicamos un descuento
        except Exception as e:
            print(f'Error al calcular el total del carrito: {e}')
            total = None
        finally:
            return total

#Clase ProductoAlimenticio que hereda de Producto
class ProductoAlimienticio(Producto):
    def __init__(self, nombre, descripcion, categoria,precio, fecha_vecimiento):
        super().__init__(nombre, descripcion, categoria)
        self._precio = precio
        self._fecha_vencimiento = fecha_vecimiento

    @property
    def precio(self):
        return self._precio

    def calcular_precio(self):
        if self._precio < 0:
            raise ValueError('El precio no puede ser negativo')
        return self._precio

#Clase ProductoElectronico que hereda de Producto

class ProductoElectronico(Producto):
    def __init__(self, nombre, descripcion, categoria,precio,garantia):
        super().__init__(nombre, descripcion, categoria)
        self._precio = precio
        self._garatia = garantia
    
    @property
    def precio(self):
        return self._precio

    def calcular_precio(self):
        #Todo: Precio para efectivo y otro precio para cuotas
        return self._precio

#Prog Principal

#Crear clientes
cliente1 = Cliente('Ana Gomez', 123,'efectivo')
cliente2 = Cliente('Mario Luis', 233,'tarjeta')

#crear productos
prod1 = ProductoAlimienticio('Leche','Leche descremada','alimento',-399,'2024-01-01')

prod2 = ProductoElectronico('Celular','Es un telefono inteligente','electronica',90000,'1 año')

#Crear el carrito de compras para el cliente 1
carrito1 = CarritoDeCompras(cliente1)
carrito1.agregar_producto(prod1)
carrito1.agregar_producto(prod2)
total1 = carrito1.calcular_total()

#Crear el carrito de compras para el cliente 2
carrito2 = CarritoDeCompras(cliente2)
carrito2.agregar_producto(prod1)
carrito2.agregar_producto(prod2)
total2 = carrito2.calcular_total()

print(f'Total a pagar Cliente 1: ${total1}')
print(f'Total a pagar Cliente 2: ${total2}')








        

