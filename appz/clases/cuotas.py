from datetime import timedelta


class Cuotas(object):
    def __init__(self, cuota=0, fecha='01/01/2018', monto=0, interes=0.0):
        self.__cuota = cuota
        self.__fecha = fecha+timedelta(days=(30*cuota))
        self.__monto = monto
        self.__interes = interes

    def getNumero(self):
        return self.__cuota

    def getFecha(self):
        return self.__fecha

    def getMonto(self):
        return self.__monto

    def getInteres(self):
        return self.__interes

    def getValorInteres(self):
        return int(self.getMonto() * self.getInteres())

    def GetTotalCuota(self):
        return (self.getMonto() + self.getValorInteres())

    def getEstado(self):
        return "Al día" if self.__interes == 0 else "Morosa"

    def esMorosa(self):
        return False if self.__interes == 0 else True

    def setNumero(self, cuota):
        self.__cuota = cuota

    def setFecha(self, fecha):
        self.__fecha = fecha

    def setMonto(self, monto):
        self.__monto = monto

    def setInteres(self, interes):
        self.__interes = interes

        def str(self):
            return "Cuota {0} pagada {1} monto ${2}.-".format(self.getNumero(), self.getFecha(), self.getMonto())
