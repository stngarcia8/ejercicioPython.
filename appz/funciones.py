# Archivo: funciones.py
# Funciones de uso comun.

import os
from .clase_ingresos import Ingresos


# cls():
# Limpiar pantalla.
def cls():
    if os.name in ("ce", "nt", "dos"):
        os.system("cls")
    else:
        os.system("clear")


# titulo([titulo]):
# Muestra un titulo en pantalla.
def titulo(titulo):
    cls()
    if not titulo:
        return
    print("{0:^80}".format(titulo.upper()))
    print("{0:^80}".format("-".rjust(len(titulo), '-')))
    print()


# pressEnter([mensaje]): Espera la pulsación de la tecla < ENTER >
# mostrando u mensaje(opcional).
def pressEnter(mensaje=""):
    print()
    if len(mensaje) > 0:
        print(mensaje)
    print("Presione <ENTER> para continuar...", end="")
    input()


# leee(campo, requerido, patron):
# Solicita el ingreso de información por teclado.
# campo: texto a mostrar en el ingreso.
# requerido: true si el campo es obligatorio, false si es opcional
# patron: expresion regular que sera apllicada a la validación.
# retorna el valor ingresado como cadena de texto.
def leee(campo, requerido, patron):
    miIngreso = Ingresos()
    return miIngreso.ingresarCadena(campo, patron, requerido)


# selecciona(campo, opciones):
# Permite ingresar una selección por pantalla.
# campo: texto para indicar que será seleccionado.
# opciones: diccionario con las opciones disponibles.
# retorna la opcion seleccionada como un caracter en cadena de texto.
def selecciona(campo, opciones):
    miIngreso = Ingresos()
    return miIngreso.ingresarCaracter(campo, opciones)


# leeNro(campo, minVal, maxVal, patron):
# campo: texto que indica el campo a ingresar.
# minVal: valor mínimo que aceptara el campo.
# maxVal : valor máximo que aceptara el campo.
# patron: expresion regular que será aplicado al ingreso del numero.
# retorna el numero ingresado.
def leeNro(campo, minVal, maxVal, patron):
    miIngreso = Ingresos()
    return miIngreso.ingresaNumero(campo, minVal, maxVal, patron)
