#Def de clase base Cliente
class Cliente:
    def __init__(self,nombre,saldo=0):
        self.nombre = nombre
        self.saldo = saldo

    def depositar(self,monto):
        self.saldo += monto
        print('Deposito realizado')
    
    def consultar_saldo(self):
        print(f'Saldo: {self.saldo}')
    
    def extraer(self,monto):
        try:
                self.saldo -=monto
                print(f'Extraccion realizada, su saldo actual: {self.saldo}')
        except ValueError as e:
            print(e)
        finally:
            print('Operacion realizada con exito')

#Cliente VIP  hereda de cliente
class ClienteVIP(Cliente):
    def __init__(self, nombre, saldo=0,limite_credito = 0):
        super().__init__(nombre, saldo)
        self.limite_credito = limite_credito
    
    def extraer(self, monto):
        if self.saldo + self.limite_credito >= monto:
            self.saldo -= monto
            print('Extraccion exitosa', self.saldo)
        else:
            print('Saldo insuficiente')

#Clase Cuenta Conjunta
class CuentaConjunta:
    def __init__(self,clientes):
        self.clientes = clientes
        self.saldo = 0

    def depositar(self,monto):
        self.saldo += monto
        print('Deposito realizado')
    
    def consultar_saldo(self):
        print(f'Saldo: {self.saldo}')
    
    def extraer(self,monto):
        if self.saldo >= monto:
            self.saldo -=monto
            print(f'Extraccion realizada, su saldo actual: {self.saldo}')
        else:
            print('Saldo insuficiente')


#Crear Clientes
print('Cliente Pedro')
cliente1 = Cliente('Pedro')
cliente1.depositar(100)
cliente1.extraer('500')
cliente1.consultar_saldo()

#Crear un cliente VIP
# print('-----------Cliente VIP MARIA---------')
# cliente2 = ClienteVIP('Maria', saldo=50000, limite_credito=25000)
# cliente2.depositar(32000)
# cliente2.consultar_saldo()
# cliente2.extraer(83000)
# cliente2.extraer(83000)



#Cuenta conjunto entre dos clientes
# print('Cuenta Conjunto')
# cuenta_conjunto = CuentaConjunta([cliente1,cliente2])
# cuenta_conjunto.depositar(5000)
# cuenta_conjunto.consultar_saldo()
# cuenta_conjunto.extraer(5000)