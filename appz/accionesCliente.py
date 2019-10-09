import copy
from .enumeraciones.enum_regexp import Exp
from .enumeraciones.enum_opciones import Opciones
from .funciones import pressEnter, titulo, leee, selecciona, leeNro


def ingresarCliente(cliente):
    titulo("Ingresar cliente.")
    __cabecera(cliente, None, False)
    __leerDatos(cliente)
    pressEnter("El cliente ha sido creado.")


def __cabecera(cliente, credito, muestraCredito):
    if cliente.existe():
        cliente.getDatos()
    if credito and muestraCredito:
        credito.getDatos()


def __leerDatos(cliente):
    cliente.setNombre(leee("nombre", True, Exp.NOMBRE))
    cliente.setRut(leee("rut", True, Exp.RUT))
    cliente.setMail(leee("e-mail", False, Exp.EMAIL))
    cliente.setTipo(selecciona("tipo", Opciones.Tipo))


def cambiarTipo(cliente):
    titulo("Cambio de tipo de cliente.")
    __cabecera(cliente, None, False)
    if not cliente.existe():
        pressEnter("No se ha ingresado un cliente para cambiar su tipo.")
        return
    cliente.setTipo(selecciona("tipo", Opciones.Tipo))
    pressEnter("El tipo de cliente ha sido cambiado.")


def AsignaCredito(cliente, credito):
    titulo("Asignación de credito a cliente.")
    __cabecera(cliente, credito, True)
    if not cliente.existe() or not credito.existe():
        pressEnter(__msgAsignacion(cliente, credito))
        return
    if cliente.getCredito().checkCodigo(credito.getCodigo()):
        pressEnter("El cliente ya posee el crédito.")
        return
    if cliente.getCredito().estaPagando():
        pressEnter("Cliente esta pagando el crédito, no puede asignar otro.")
        return
    miOpcion = selecciona("opción", Opciones.Asigna)
    if miOpcion == "N":
        pressEnter("El crédito no se asocio.")
        return
    cliente.setCredito(copy.copy(credito))
    pressEnter("Crédito fue asociado al cliente.")


def __msgAsignacion(cliente, credito):
    if not cliente.existe() and not credito.existe():
        return"No hay cliente ni crédito ingresado."
    if not cliente.existe():
        return "No hay un cliente ingresado."
    if not credito.existe():
        return "No hay un crédito ingresado."
    return""


def cambiaMorosidad(cliente):
    titulo("Cambiar el estado del crédito.")
    if not __verificaCliente(cliente):
        return
    miOpcion = selecciona("opción", Opciones.Estado)
    credito = cliente.getCredito()
    credito.setMorosidad(False if miOpcion == "A" else True)
    pressEnter("El estado del crédito del cliente ha cambiado.")


def __verificaCliente(cliente):
    if not cliente.existe():
        pressEnter("No hay cliente ingresado")
        return False
    cliente.getDatos()
    if not cliente.getCredito().existe():
        pressEnter("El cliente no tiene un crédito asociado")
        return False
    return True


def pagarCuota(cliente):
    while True:
        titulo("Pagar cuota de credito.")
        if not __verificaCliente(cliente):
            break
        cuota = cliente.getCredito().getCuotasPagadas()
        if cliente.getCredito().fuePagado():
            pressEnter("Cliente finalizo el crédito, venda otro altiro!!")
            break
        cliente.getCredito().getEstadoCuota()
        opcion = selecciona("opción", Opciones.Pago)
        if opcion == "X":
            break
        cuota = cuota+1
        cliente.getCredito().setCuotasPagadas(cuota)


def mostrarCancelado(cliente):
    titulo("Mostrar montos cancelados")
    if not __verificaCliente(cliente):
        return
    cliente.getCredito().getInfoCredito()
    pressEnter("")


def extenderCredito(cliente):
    titulo("Extender crédito.")
    if not __verificaCliente(cliente):
        return
    if cliente.getCredito().getExtension():
        pressEnter("El crédito del cliente ya ha sido extendido.")
        return
    extension = leeNro("meses de extensión", 5, 12, Exp.NUMERO)
    cliente.getCredito().setExtension(extension)
    pressEnter("El  crédito fue extendido en {0} meses".format(extension))
