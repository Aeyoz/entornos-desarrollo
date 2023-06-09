import pytest
import dni
from cuentaCorriente import *

DNI_STR = "45678123G"
OTHER_DNI_STR = "12478496B"

new_dni = dni.Dni(cadena=DNI_STR)
nombre = "pepe"
apellidos = "morales gonzalez"
direccion = "callejon las cañadas"
tel = "123456789"
saldo = 1.5
new_cuenta_corriente = CuentaCorriente(
    nombre, apellidos, direccion, tel, DNI_STR, saldo
)


def test_dni_attributes():
    assert new_dni.dni == DNI_STR
    assert new_dni.sano == False


def test_getDni():
    assert new_dni.getDni() == DNI_STR


def test_set_dni(cadena=OTHER_DNI_STR, restart_cadena=DNI_STR):
    new_dni.setDni(cadena)
    assert new_dni.dni == cadena
    new_dni.setDni(restart_cadena)


def test_setSano(value=True):
    new_dni.setSano(value)
    assert new_dni.sano == value


def test_check_Longitud():
    assert new_dni.checkLongitud() is True


def test_check_Longitud_when_its_wrong():
    new_dni.setDni("422586")
    assert new_dni.checkLongitud() is False
    new_dni.setDni(DNI_STR)


def test_check_Numero():
    assert new_dni.checkNumero() is True


def test_check_Letra():
    assert new_dni.checkLetra() is True


def test_check_Dni():
    new_dni.checkDni()
    assert new_dni.sano == True


def test_cuenta_corriente_attributes():
    assert new_cuenta_corriente.nombre == nombre
    assert new_cuenta_corriente.apellido == apellidos
    assert new_cuenta_corriente.direccion == direccion
    assert new_cuenta_corriente.telefono == tel
    assert new_cuenta_corriente.saldo == saldo
    assert new_cuenta_corriente.nif.dni == DNI_STR


def test_setNombre(nombre="José Luis"):
    new_cuenta_corriente.setNombre(nombre)
    assert new_cuenta_corriente.nombre == nombre


def test_getNombre(nombre="José Luis"):
    assert new_cuenta_corriente.getNombre() == nombre
    assert new_cuenta_corriente.getNombre() == new_cuenta_corriente.nombre


def test_setApellido(apellido="Hernández García"):
    new_cuenta_corriente.setApellido(apellido)


def test_getApellido(apellido="Hernández García"):
    assert new_cuenta_corriente.getApellido() == apellido
    assert new_cuenta_corriente.getApellido() == new_cuenta_corriente.apellido


def test_setDireccion(direccion="Camino el gallo"):
    new_cuenta_corriente.setDireccion(direccion)
    assert new_cuenta_corriente.direccion == direccion


def test_getDireccion(direccion="Camino el gallo"):
    assert new_cuenta_corriente.getDireccion() == direccion
    assert new_cuenta_corriente.getDireccion() == new_cuenta_corriente.direccion


def test_setTelefono(tel="546812348"):
    new_cuenta_corriente.setTelefono(tel)
    assert new_cuenta_corriente.telefono == tel


def test_getTelefono(tel="546812348"):
    assert new_cuenta_corriente.telefono == tel
    assert new_cuenta_corriente.getTelefono() == new_cuenta_corriente.telefono


def test_setNif():
    new_cuenta_corriente.nif.setDni(OTHER_DNI_STR)
    assert new_cuenta_corriente.nif.dni == OTHER_DNI_STR


def test_getNif():
    assert new_cuenta_corriente.nif.dni == OTHER_DNI_STR
    assert new_cuenta_corriente.nif.getDni() == OTHER_DNI_STR


def test_getSaldo():
    assert new_cuenta_corriente.getSaldo() == saldo


def test_setSaldo(nuevo_saldo=20):
    new_cuenta_corriente.setSaldo(nuevo_saldo)
    assert new_cuenta_corriente.saldo == nuevo_saldo


def test_retirarSaldo(substracted_credit=10):
    account_credit_amount = new_cuenta_corriente.saldo
    new_cuenta_corriente.retirarDinero(substracted_credit)
    new_amount = account_credit_amount - substracted_credit
    assert new_cuenta_corriente.saldo == new_amount


def test_ingresarDinero():
    initial_quantity = new_cuenta_corriente.saldo
    added_quantity = 20
    new_cuenta_corriente.ingresarDinero(added_quantity)
    total_quantity = initial_quantity + added_quantity
    assert new_cuenta_corriente.saldo == total_quantity


def test_saldo_negativo():
    assert new_cuenta_corriente.saldoNegativo() is True
    new_cuenta_corriente.retirarDinero(41)
    assert new_cuenta_corriente.saldoNegativo() is False


def test_consultarCuenta():
    acount_string_representation = """"""
    assert new_cuenta_corriente.consultarCuenta() == acount_string_representation
