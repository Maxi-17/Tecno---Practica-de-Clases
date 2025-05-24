from CuentaBancaria import CuentaBancaria

# cuenta1 = CuentaBancaria("Gabriel",333333,'1990/02/03',15000)

# print(cuenta1.obtener_edad())


class CuentaAhorro(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self.__tasa_interes = 0.001

    def calcular_interes(self):
        return self._saldo * self.__tasa_interes

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(f"Se ha depositado {monto} a la cuenta de ahorro de {self._nombre_titular}, saldo: {self.obtener_saldo()}")
        else:
            print("El monto a depositar debe ser mayor a 0")

    def extraer(self, monto):
        if monto <= self._saldo:
            self._saldo -= monto
            print(f"Se extrajo {monto} de la cuenta de ahorro de {self._nombre_titular}, saldo actual: {self.obtener_saldo()}")
        else:
            print("No tiene saldo suficiente para esta operacion")

# Código de prueba

cuenta_ahorro = CuentaAhorro("Pepe", 17171717, '1982/07/17', 33000)

edad = cuenta_ahorro.obtener_edad()
cuenta_ahorro.depositar(7000)
cuenta_ahorro.extraer(1500)
interes = cuenta_ahorro.calcular_interes()

edad, cuenta_ahorro.obtener_saldo(), interes