from dni import *


class CuentaCorriente:
    def __init__(
        self, nombre="", apellido="", direccion="", telefono="", nif="", saldo=0.0
    ):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.nif = Dni(nif)
        self.saldo = saldo

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def getApellido(self):
        return self.apellido

    def setDireccion(self, direccion):
        self.direccion = direccion

    def getDireccion(self):
        return self.direccion

    def setTelefono(self, telefono):
        self.telefono = telefono

    def getTelefono(self):
        return self.telefono

    def setNif(self, nif):
        self.nif = nif

    def getNif(self):
        return self.nif

    def setSaldo(self, saldo):
        self.saldo = saldo

    def getSaldo(self):
        return self.saldo

    def retirarDinero(self, cantidadRetirada):
        dineroRestante = self.getSaldo() - cantidadRetirada
        self.setSaldo(dineroRestante)
        return (cantidadRetirada, dineroRestante)

    def ingresarDinero(self, cantidadIngresada):
        dineroTotal = self.getSaldo() + cantidadIngresada
        self.setSaldo(dineroTotal)
        return (cantidadIngresada, dineroTotal)

    def checkNif(self):
        self.nif.checkNif()

    def consultarCuenta(self):
        print(
            "Cuenta Corriente de:",
            self.getNombre(),
            self.getApellido(),
            "\nDNI: ",
            self.getNif(),
        )
        print(
            "Direccion de domicilio:",
            self.getDireccion(),
            "\nTelefono:",
            self.getTelefono(),
        )
        print("Saldo Disponible:", self.getSaldo())

    def saldoNegativo(self):
        return self.getSaldo() > 0
