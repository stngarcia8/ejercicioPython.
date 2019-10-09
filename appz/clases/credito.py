from datetime import datetime, timedelta
from .cuotas import Cuotas


class Credito(object):

    __interes = 0.15
    __cuotas = list()
    __fmt = '%d/%m/%Y'

    def __init__(self):
        self.__codigo = ""
        self.__fechaSolicitud = datetime.strptime('01/01/2018', self.__fmt)
        self.__fechaVencimiento = datetime.strptime('01/01/2018', self.__fmt)
        self.__montoSolicitado = 0
        self.__morosidad = False
        self.__extension = 0

    def getCodigo(self):
        return self.__codigo

    def getFechaSolicitud(self):
        return self.__fechaSolicitud

    def getFechaVencimiento(self):
        return self.__fechaVencimiento

    def getMonto(self):
        return self.__montoSolicitado

    def getMorosidad(self):
        return self.__morosidad

    def getCuotasPagadas(self):
        return len(self.__cuotas)

    def getCuotasMorosas(self):
        return len([c for c in self.__cuotas if c.esMorosa()])

    def getInteres(self):
        return self.__interes if self.getMorosidad() else 0

    def getCuotasPactadas(self):
        diferencia = int((self.getFechaVencimiento() -
                          self.getFechaSolicitud()).days)
        cuotas = int((diferencia/30))
        return cuotas

    def getExtension(self):
        return self.__extension

    def fuePagado(self):
        return True if self.getCuotasPactadas() == self.getCuotasPagadas() else False

    def estaPagando(self):
        if self.fuePagado():
            return False
        return True if self.getCuotasPagadas() > 0 else False

    def getValorCuota(self):
        return int(self.getMonto()/self.getCuotasPactadas())

    def getMontoCancelado(self):
        if not self.__cuotas:
            return 0
        return sum([c.getMonto() for c in self.__cuotas])

    def getCanceladoConMora(self):
        if not self.__cuotas:
            return 0
        return sum([c.getValorInteres() for c in self.__cuotas])

    def getListaCuotas(self):
        if not self.__cuotas:
            return
        print()
        print("{0:^80}".format("Lista de cuotas."))
        print("-".rjust(80, '-'))
        print("Cuota\tFecha\t\tMonto\t\tInterés\tValor interés\tTotal cancelado")
        print("-".rjust(80, '-'))
        for c in self.__cuotas:
            cad = "{0:^5}\t{1:%d/%m/%Y}\t${2:>10}.-\t{3:.2f}\t${4:>10}.-\t${5:>12}.-"
            cad = cad.format(c.getNumero(), c.getFecha(), c.getMonto(),
                             c.getInteres(), c.getValorInteres(),  c.GetTotalCuota())
            print(cad)
        print("-".rjust(80, '-'))
        print("Totales:\t\t${0:>10}.-\t\t${1:>10}.-\t${2:>10}.-".format(
            self.getMontoCancelado(), self.getCanceladoConMora(), self.getMontoCancelado()+self.getCanceladoConMora()))

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def setFechaSolicitud(self, fechaSolicitud):
        self.__fechaSolicitud = fechaSolicitud

    def setFechaVencimiento(self, fechaVencimiento):
        self.__fechaVencimiento = fechaVencimiento

    def setMonto(self, monto):
        self.__montoSolicitado = monto

    def setMorosidad(self, morosidad):
        self.__morosidad = morosidad

    def setCuotasPagadas(self, cuotasPagadas):
        miCuota = Cuotas(cuotasPagadas, self.__fechaSolicitud,
                         self.getValorCuota(), self.getInteres())
        self.__cuotas.append(miCuota)

    def setExtension(self, extension):
        self.__extension = extension
        self.__fechaVencimiento = self.__fechaVencimiento + \
            timedelta(days=(30*extension))

    def existe(self):
        return True if self.__codigo else False

    def checkCodigo(self, codigo):
        return True if self.getCodigo() == codigo else False

    def getEstadoCuota(self):
        miCuota = Cuotas(self.getCuotasPagadas()+1, self.__fechaSolicitud,
                         self.getValorCuota(), self.getInteres())
        print("Número de cuota a pagar: {0} ".format(miCuota.getNumero()))
        print("Valor cuota ${0}.-".format(miCuota.getMonto()))
        print("Interés a aplicar {0:.2f}% (${1}.-)".format(
            miCuota.getInteres(), miCuota.getValorInteres()))
        print("Total a pagar ${0}.-".format(miCuota.GetTotalCuota()))

    def getInfoCredito(self):
        print("{0:^80}".format("Estado del credito."))
        print("-".rjust(80, '-'))
        if self.getCuotasMorosas():
            print("Cuotas morosas:", self.getCuotasMorosas())
            print("Interés: {0:.2f}%\t\t\t Monto cancelado por mora ${1}.-".format(
                self.__interes, self.getCanceladoConMora()))
        print("Total cancelado ${0}.-\t Falta por cancelar ${1}.-".format(self.getMontoCancelado(),
                                                                          self.getMonto()-self.getMontoCancelado()))
        self.getListaCuotas()

    def getDatos(self):
        print("{0:^80}".format("Datos de credito"))
        print("-".rjust(80, '-'))
        print("Código: ", self.getCodigo(), sep="\t\t")
        print("Fecha solicitud {0:%d/%m/%Y} \t Fecha vencimiento {1:%d/%m/%Y} ".format(
            self.getFechaSolicitud(), self.getFechaVencimiento()))
        print("Monto ${0}.- \t\t Cuotas pactadas: {1}".format(
            self.getMonto(),  self.getCuotasPactadas()))
        print("Valor cuota ${0}.- \t\t Cuotas pagadas: {1}".format(
            self.getValorCuota(), self.getCuotasPagadas()))
        estado = "Moroso." if self.getMorosidad() else "Al día."
        extend = "No." if not self.getExtension(
        ) else "Sí, en {0} meses".format(self.getExtension())
        print("Estado {0}\t\t\t Extendido: {1}".format(estado, extend))
        if self.fuePagado():
            print("Credito finalizado!")
        print("-".rjust(80, '-'))
        print()

    def __str__(self):
        cadena = "Crédito {0:<6}, solicitado {1:%d/%m/%Y} monto ${2} termina el {3:%d/%m/%Y}"
        cadena.format(self.getCodigo(), self.getFechaSolicitud(
        ), self.getMonto(), self.getFechaVencimiento())
        return cadena
