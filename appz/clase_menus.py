# Archivo: clases_menus.py
# Clase que genera el menú de opciones.


from .accionesCliente import ingresarCliente, cambiarTipo, pagarCuota, extenderCredito
from .accionesCliente import AsignaCredito, cambiaMorosidad, mostrarCancelado
from .accionesCreditos import ingresaCredito
from .clases.credito import Credito
from .clases.persona import Persona
from .enumeraciones.enum_regexp import Exp
from .funciones import titulo, leeNro


class Menus(object):

    # __opciones()
    # Muestra las opciones del menú
    def __opciones(self):
        titulo("Opciones disponibles.")
        print("1. Crear crédito.")
        print("2. Datos de cliente.")
        print("3. Cambiar tipo de cliente.")
        print("4. Asignar el crédito al cliente.")
        print("5. Cambiar estado del credito.")
        print("6. Pagar cuota.")
        print("7. Obtener meses de gracia.")
        print("8. Obtener el total a pagar.")
        print("0. Salir")
        print()


# mostrarMenu()
# Muestra el menú en pantalla y ejecuta las acciones desplegadas.
    def mostrarMenu(self):
        cliente = Persona()
        credito = Credito()
        opcion = 1
        while opcion:
            self.__opciones()
            opcion = leeNro("Ingrese su opción", 0, 8, Exp.NUMERO)
            if opcion == 1:
                ingresaCredito(credito)
            if opcion == 2:
                ingresarCliente(cliente)
            if opcion == 3:
                cambiarTipo(cliente)
            if opcion == 4:
                AsignaCredito(cliente, credito)
            if opcion == 5:
                cambiaMorosidad(cliente)
            if opcion == 6:
                pagarCuota(cliente)
            if opcion == 7:
                extenderCredito(cliente)
            if opcion == 8:
                mostrarCancelado(cliente)
            if opcion == 0:
                print("Eso fue todo, chao!")
                break
