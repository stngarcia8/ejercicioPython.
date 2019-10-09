# Archivo: clases_ingresos.py
# Clase para manipular el ingreso de datos.


import re
from datetime import datetime
from .enumeraciones.enum_msg import Msg


class Ingresos(object):

    # ingresaNumero(mensaje, minimo, maximo, patron)
    # Permite ingresar un número, indicando sus rangos minimos o maximos.
    # mensaje: texto a desplegar al solicitar el número.
    # minimo: valor mínimo permitido.
    # maximo: valor máximo permitido.
    # patron: expresión regular aplicada para la validación.
    # Permite realizar el ingreso de números.
    # retorna el numero ingresado como valor entero.
    def ingresaNumero(self, mensaje, minimo, maximo, patron):
        valor = 0
        if maximo == 0:
            rango = ", debe ser igual o mayor a {0}"
            rango = rango.format(str(minimo))
        else:
            rango = ", valores entre {0} y {1}"
            rango = rango.format(str(minimo), str(maximo))
        while True:
            print(mensaje, rango, end=": ")
            opcion = input()
            if not self.__validaExp(patron, opcion, Msg.NUMERO_INVALIDO):
                continue
            valor = int(opcion)
            if maximo == 0:
                if valor < minimo:
                    print(Msg.NUMERO_MENOR.format(str(minimo)))
                    continue
            else:
                if valor < minimo or valor > maximo:
                    print(Msg.NUMERO_FUERA_RANGO.format(
                        str(minimo), str(maximo)))
                    continue
            break
        return valor

    # __validaExp(patron, valor, msgError):
    # Valida que la expresión regular se aplica alvalor ingresado.
    # patron: expresión regular a validar.
    # valor: valorque será evaluado con la expresión regular.
    # msgError: mensaje de error a mostrar en caso de no cumplir el criterio evaluado.
    # Retorna true, siel valor cumple el criterio, false si no lo cumple.
    def __validaExp(self, patron, valor, msgError):
        if not patron:
            return True
        if not re.match(patron, valor):
            print(msgError)
            return False
        return True

    # ingresarCadena(campo, patron, requerido):
    # Permite realizar el ingreso de un campo en formato string.
    # campo: texto a desplegar en el ingreso.
    # patron: expresión regular que evaluará al campo.
    # requerido: indica si el campo es obligatorio (true), o si es opcional (false)
    # retorna la cadena de con el valor ingresado.
    def ingresarCadena(self, campo, patron, requerido):
        msgError = Msg.CADENA_INVALIDA.format(campo)
        while True:
            print("Ingrese", campo, end=": ")
            cadena = input()
            if requerido and len(cadena) == 0:
                print(Msg.CADENA_VACIA.format(campo))
                continue
            if not self.__validaExp(patron, cadena, msgError):
                continue
            break
        return cadena

    # ingresarCaracter(campo, listaOpc):
    # Permite ingresar el caracter de una lista de opciones.
    # campo: texto desplegado al ingresar el valor.
    # opciones: diccionario que contiene las opciones a desplegar.
    # retorna el caracter de la opción ingresada.
    def ingresarCaracter(self, campo, listaOpc):
        cadena = ""
        for clave, valor in listaOpc.items():
            cadena += "'{0}': {1}, ".format(clave, valor)
        while True:
            print("Ingrese {0} [{1}]".format(
                campo, cadena.rstrip(', ')), end=": ")
            opcion = input()
            if opcion.upper() not in listaOpc:
                print(Msg.VALOR_INVALIDO)
                print(cadena.rstrip(', '))
                continue
            break
        return opcion.upper()

    # ingresarFecha(mensaje, minimo, maximo, patron):
    # Permite realizar el ingreso de fechas, validando sus rangos de entrada.
    # mensaje: texto el cual desplegará para el ingreso.
    # mínimo: fecha mínima que será aceptada en el rango de ingreso.
    # maximo: fecha máxima que será aceptada en el ingreso.
    # patron: expresión regular que será aplicada al ingreso de la fecha.
    # retorna la fecha ingresada en formato "datetime"
    def ingresarFecha(self, mensaje, minimo, maximo, patron):
        fmt = '%d/%m/%Y'
        msgError = Msg.FECHA_INVALIDA
        fecMin = self.__obtenerFecha(minimo)
        fecMax = self.__obtenerFecha(maximo)
        rango = "" if len(minimo) == 0 else ", rango ["+datetime.strftime(
            fecMin, fmt) + "-"+datetime.strftime(fecMax, fmt)
        while True:
            print(mensaje, rango, end=": ")
            fecha = input()
            if not self.__validaExp(patron, fecha, msgError):
                continue
            valor = self.__obtenerFecha(fecha)
            if len(maximo) == 0:
                if valor < fecMin:
                    print(Msg.FECHA_MENOR.format(
                        datetime.strftime(fecMin, fmt)))
                    continue
            else:
                if valor < fecMin or valor > fecMax:
                    print(Msg.FECHA_FUERA_RANGO.format(datetime.strftime(
                        fecMin, fmt), datetime.strftime(fecMax, fmt)))
                    continue
            break
        return valor

    # __obtenerFecha(valFecha)
    # Permite asignar un tipo de dato fecha a la cadena ingresada.
    # valFecha: fecha a convertir a formato "datetime"
    # retorna la fecha en formato "datetime"
    def __obtenerFecha(self, valFecha):
        fmt = '%d/%m/%Y'
        fecha = datetime.strftime(datetime.now().date(), fmt)
        if len(valFecha) == 0:
            return datetime.strptime(fecha, fmt)
        return datetime.strptime(valFecha, fmt)
