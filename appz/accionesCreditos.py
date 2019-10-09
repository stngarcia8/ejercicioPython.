from datetime import datetime, timedelta
from .funciones import titulo, pressEnter
from .clase_ingresos import Ingresos
from .enumeraciones.enum_regexp import Exp


def ingresaCredito(credito):
    __cabecera(credito)
    __leerDatos(credito)
    pressEnter("El crédito ha sido creado.")


def __cabecera(credito):
    if credito.existe():
        titulo("")
        credito.getDatos()
    else:
        titulo("Ingresar crédito.")


def __leerDatos(credito):
    miIngreso = Ingresos()
    credito.setCodigo(__leeCodigo(miIngreso))
    credito.setFechaSolicitud(__leeFechaSolicitud(miIngreso))
    credito.setFechaVencimiento(__leeFechaVencimiento(
        miIngreso, credito.getFechaSolicitud()))
    credito.setMonto(____leeMonto(miIngreso))


def __leeCodigo(miIngreso):
    campo = "Código crédito"
    requerido = True
    patron = Exp.CODIGO
    return miIngreso.ingresarCadena(campo, patron, requerido)


def __leeFechaSolicitud(miIngreso):
    campo = "fecha de solicitud"
    patron = Exp.FECHA
    return miIngreso.ingresarFecha(campo, "", "", patron)


def __leeFechaVencimiento(miIngreso, fechaInicio):
    campo = "fecha de vencimiento"
    fechaInicial = datetime.strftime(
        fechaInicio+timedelta(days=(30*12)), '%d/%m/%Y')
    fechaFinal = datetime.strftime(
        fechaInicio+timedelta(days=(30*120)), '%d/%m/%Y')
    patron = Exp.FECHA
    return miIngreso.ingresarFecha(campo, fechaInicial, fechaFinal, patron)


def ____leeMonto(miIngreso):
    campo = "monto solicitado"
    patron = Exp.NUMERO
    return miIngreso.ingresaNumero(campo, 6000000, 0, patron)
