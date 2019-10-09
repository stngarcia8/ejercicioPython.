from .credito import Credito


class Persona(object):

    def __init__(self):
        self.__rut = ""
        self.__nombre = ""
        self.__mail = ""
        self.__tipo = ""
        self.__credito = Credito()

    def getRut(self):
        return self.__rut

    def getNombre(self):
        return self.__nombre

    def getMail(self):
        return self.__mail

    def getTipo(self):
        if self.__tipo == "N":
            return "Cliente normal"
        if self.__tipo == "P":
            return "Cliente preferencial"
        return ""

    def getCredito(self):
        return self.__credito

    def setRut(self, rut):
        self.__rut = rut

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setMail(self, mail):
        self.__mail = mail

    def setTipo(self, tipo):
        self.__tipo = tipo

    def setCredito(self, credito):
        self.__credito = credito

    def existe(self):
        return False if len(self.getRut()) == 0 else True

    def conCredito(self):
        return False if len(self.getCredito().getCodigo()) == 0 else True

    def getDatos(self):
        print("{0:^80}".format("Datos del cliente."))
        print("-".rjust(80, '-'))
        self.__verCliente()
        self.__verCredito()
        print()

    def __verCliente(self):
        print("Nombre: {0:<35} \t Rut: {1:<10}".format(
            self.getNombre(), self.getRut()))
        print("Email: {0:<35} \t Tipo: {1}".format(
            self.getMail(), self.getTipo()))
        print("-".rjust(80, '-'))

    def __verCredito(self):
        if self.conCredito():
            print()
            self.getCredito().getDatos()
        else:
            print("Cliente sin credito asociado.")

    def __str__(self):
        return self.getNombre()+" "+self.getTipo()
