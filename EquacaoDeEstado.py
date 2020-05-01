# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 12:13:46 2018

@author: Willian Belincanta Ribeiro
"""
from abc import ABCMeta,abstractmethod
import numpy
R = 8.314
puras = [#composto,fator acentrico, Tc, Pc, Zc,Vc
        ['metano',0.012,190.6,45.99,0.286,98.6],
        ['etano',0.1,305.3,48.72,0.279,145.5],
        ['propano',0.152,369.8,42.48,0.276,200],
        ['n-butano',0.2,425.1,37.96,0.274,255],
        ['n-pentano',0.252,469.7,33.7,0.7,313],
        ['n-hexano',0.301,507.6,30.25,0.266,371],
        ['n-heptano',0.35,540.2,27.4,0.261,428],
        ['n-octano',0.4,568.7,24.9,0.256,486],
        ['n-nonano',0.444,594.6,22.9,0.252,544],
        ['n-decano',0.492,617.7,21.1,0.247,600],
        ['isobutano',0.181,408.1,36.48,0.282,262.7],
        ['isooctano',0.302,544,25.68,0.266,468],
        ['ciclopentano',0.196,511.8,45.02,0.273,258],
        ['ciclo-hexano',0.21,553.6,40.73,0.273,308],
        ['metilciclopentano',0.23,532.8,37.85,0.272,319],
        ['metilciclohexano',0.235,572.2,34.71,0.269,368],
        ['etileno',0.087,282.3,50.4,0.281,131],
        ['propileno',0.14,365.6,46.65,0.289,188.4],
        ['1-buteno',0.191,420,40.43,0.277,239.3],
        ['cis-2-buteno',0.205,435.6,42.43,0.273,233.8],
        ['trans-2-buteno',0.218,428.6,41,0.275,237.7],
        ['1-hexeno',0.28,504,31.4,0.265,354],
        ['isobutileno',0.194,417.9,40,0.275,239.9],
        ['1,3-butadieno',0.19,425.2,42.77,0.267,220.4],
        ['ciclo-hexeno',0.212,560.4,43.5,0.272,291],
        ['acetileno',0.187,308.3,61.39,0.271,113],
        ['benzeno',0.21,562.2,48.98,0.271,259],
        ['tolueno',0.262,591.8,41.06,0.264,316],
        ['etilbenzeno',0.303,617.2,36.06,0.263,374],
        ['cumeno',0.326,631.1,32.09,0.261,427],
        ['o-xileno',0.31,630.3,37.34,0.263,369],
        ['m-xileno',0.326,617.1,35.36,0.259,376],
        ['p-xileno',0.322,616.2,35.11,0.26,379],
        ['estireno',0.297,636,38.4,0.256,352],
        ['naftaleno',0.302,748.4,40.51,0.269,413],
        ['bifenil',0.365,789.3,38.5,0.295,502],
        ['formaldeído',0.282,408,65.9,0.223,115],
        ['acetaldeído',0.291,466,55.5,0.221,154],
        ['acetato de metila',0.331,506.6,47.5,0.257,228],
        ['acetato de etila',0.366,523.3,38.8,0.255,286],
        ['acetona',0.307,508.2,47.01,0.233,209],
        ['metiletilcetona',0.323,535.5,41.5,0.249,267],
        ['éter dietílico',0.281,466.7,36.4,0.263,280],
        ['éter metil-t-butílico',0.266,497.1,34.3,0.273,329],
        ['metanol',0.564,512.6,80.97,0.224,118],
        ['etanol',0.645,513.9,61.48,0.24,167],
        ['1-propanol',0.622,536.8,51.75,0.254,219],
        ['1-butanol',0.594,563.1,44.23,0.26,275],
        ['1-hexanol',0.579,611.4,35.1,0.263,381],
        ['2-propanol',0.668,508.3,47.62,0.248,220],
        ['fenol',0.444,694.3,61.3,0.243,229],
        ['etileno glicol',0.487,719.7,77,0.246,191],
        ['ácido acético',0.467,592,57.86,0.211,179.7],
        ['ácido n-butírico',0.681,615.7,40.64,0.232,291.7],
        ['ácido benzóico',0.603,751,44.7,0.246,344],
        ['acetonitrila',0.338,545.5,48.3,0.184,173],
        ['metilamina',0.281,430.1,74.6,0.321,154],
        ['etilamina',0.285,456.2,56.2,0.307,207],
        ['nitrometano',0.348,588.2,63.1,0.223,173],
        ['tetracloreto de carbono',0.193,556.4,45.6,0.272,276],
        ['clorofórmio',0.222,536.4,54.72,0.293,239],
        ['diclorometano',0.199,510,60.8,0.265,185],
        ['cloreto de metila',0.153,416.3,66.8,0.276,143],
        ['cloreto de etila',0.19,460.4,52.7,0.275,200],
        ['clorobenzeno',0.25,632.4,45.2,0.265,308],
        ['tetrafluoroetano',0.327,374.2,40.6,0.258,198],
        ['argônio',0,150.9,48.98,0.291,74.6],
        ['criptônio',0,209.4,55.02,0.288,91.2],
        ['xenônio',0,289.7,58.4,0.286,118],
        ['hélio',-0.39,5.2,2.28,0.302,57.3],
        ['hidrogênio',-0.216,33.19,13.13,0.305,64.1],
        ['oxigênio',0.022,154.6,50.43,0.288,73.4],
        ['nitrogênio',0.038,126.2,34,0.289,89.2],
        ['ar',0.035,132.2,37.45,0.289,84.8],
        ['cloro',0.069,417.2,77.1,0.265,124],
        ['monóxido de carbono',0.048,132.9,34.99,0.299,93.4],
        ['dióxido de carbono',0.224,304.2,73.83,0.274,94],
        ['dissulfeto de carbono',0.111,552,79,0.275,160],
        ['sulfeto de hidrogênio',0.094,373.5,89.63,0.284,98.5],
        ['dióxido de enxofre',0.245,430.8,78.84,0.269,122],
        ['trióxido de enxofre',0.424,490.9,82.1,0.255,127],
        ['óxido nítrico',0.583,180.2,64.8,0.251,58],
        ['óxido nitroso',0.141,309.6,72.45,0.274,97.4],
        ['cloreto de hidrogênio',0.132,324.7,83.1,0.249,81],
        ['cianeto de hidrogênio',0.41,456.7,53.9,0.197,139],
        ['água',0.345,647.1,220.55,0.229,55.9],
        ['amônia',0.253,405.7,112.8,0.242,72.5],
        ['ácido nítrico',0.714,520,68.9,0.231,145],
        ['ácido sulfúrico',0,924,64,0.147,177]]

class EquacaoDeEstado:
#Classe para uso das equações de estado para cálculo de pressão ou volume
    __metaclass__=ABCMeta
    #pressao em Pascal
    def getPressao(self):
        return self.__pressao
    def setPressao(self,pressao):
        self.__pressao = pressao
    #Temperatura em Kelvin
    def getTemperatura(self):
        return self.__temperatura
    def setTemperatura(self,temperatura):
        self.__temperatura = temperatura
    #Volume molar em m³/mol
    def getVolumeMolar(self):
        return self.__volumemolar
    def setVolumeMolar(self,volumemolar):
        self.__volumemolar = volumemolar
    #Temperatura crítica em Kelvin
    def getTemperaturaCritica(self):
        return self.__temperaturacritica
    def setTemperaturaCritica(self,temperaturacritica):
        self.__temperaturacritica = temperaturacritica
    #Pressão crítica em pascal
    def getPressaoCritica(self):
        return self.__pressaocritica
    def setPressaoCritica(self,pressaocritica):
        self.__pressaocritica = pressaocritica
    def getFatorAcentrico(self):
        return self.__fatoracentrico
    def setFatorAcentrico(self,fatoracentrico):
        self.__fatoracentrico = fatoracentrico
    #Volume molar crítico em m³/mol
    def getVolumeMolarCritico(self):
        return self.__volumemolarcritico
    def setVolumeMolarCritico(self,volumemolarcritico):
        self.__volumemolarcritico = volumemolarcritico
    def getFatorCompCritico(self):
        return self.__fatorcompcritico
    def setFatorCompCritico(self,fatorcompcritico):
        self.__fatorcompcritico = fatorcompcritico
    def getSim(self):
        return self.sim
    def buscarPuras(self,composto):
            for p in puras:
                if composto==p[0]:
                    self.setFatorAcentrico(p[1])
                    self.setTemperaturaCritica(p[2])
                    self.setPressaoCritica(p[3]*1e5)
                    self.setFatorCompCritico(p[4])
                    self.setVolumeMolarCritico(p[5]*0.000001)
                    self.sim = 1
                    break
                else:
                    self.sim = 0
    @abstractmethod
    #Pressão em Pascal
    def calcularPressao(self):
        pass
    @abstractmethod
    #Volume Molar em m³/mol
    def calcularVolumeMolar(self):
        pass
    
class GasIdeal(EquacaoDeEstado):
    def calcularPressao(self):
        self.setPressao((R*self.getTemperatura())/self.getVolumeMolar())
    def calcularVolumeMolar(self):
        self.setVolumeMolar((R*self.getTemperatura())/self.getPressao())

class Virial(EquacaoDeEstado):
    def calcularPressao(self):
        Tr = self.getTemperatura()/self.getTemperaturaCritica()
        B0 = 0.083 - (0.422/(Tr**1.6))
        B1 = 0.139 - (0.172/(Tr**4.2))
        B = ((B0 + (self.getFatorAcentrico()*B1))*R*self.getTemperaturaCritica())/self.getPressaoCritica()
        self.setPressao((R*self.getTemperatura())/(self.getVolumeMolar()-B))
    def calcularVolumeMolar(self):
        Tr = self.getTemperatura()/self.getTemperaturaCritica()
        B0 = 0.083 - (0.422/(Tr**1.6))
        B1 = 0.139 - (0.172/(Tr**4.2))
        B = ((B0 + (self.getFatorAcentrico()*B1))*R*self.getTemperaturaCritica())/self.getPressaoCritica()
        self.setVolumeMolar(((R*self.getTemperatura())/self.getPressao())+B)

class VDW(EquacaoDeEstado):
    def calcularPressao(self):
        a = (27*R*R*self.getTemperaturaCritica()*self.getTemperaturaCritica())/(64*self.getPressaoCritica())
        b = (R*self.getTemperaturaCritica())/(8*self.getPressaoCritica())
        self.setPressao(((R*self.getTemperatura())/(self.getVolumeMolar()-b))-(a/(self.getVolumeMolar()*self.getVolumeMolar())))
    def calcularVolumeMolar(self):
        a = (27*R*R*self.getTemperaturaCritica()*self.getTemperaturaCritica())/(64*self.getPressaoCritica())
        b = (R*self.getTemperaturaCritica())/(8*self.getPressaoCritica())
        A = self.getPressao()
        B = -((self.getPressao()*b)+(R*self.getTemperatura()))
        C = a
        D = -(a*b)
        eq = [A,B,C,D]
        Raizes.raizes(eq)
        
class RK(EquacaoDeEstado):
    def calcularPressao(self):
        a = (0.42748*R*R*(self.getTemperaturaCritica()**2.5))/self.getPressaoCritica()
        b = (0.08664*R*self.getTemperaturaCritica())/self.getPressaoCritica()
        self.setPressao(((R*self.getTemperatura())/(self.getVolumeMolar()-b))-(a/(self.getVolumeMolar()*(self.getVolumeMolar()+b)*(self.getTemperatura()**0.5))))
    def calcularVolumeMolar(self):
        a = (0.42748*R*R*(self.getTemperaturaCritica()**2.5))/self.getPressaoCritica()
        b = (0.08664*R*self.getTemperaturaCritica())/self.getPressaoCritica()
        A = self.getPressao()
        B = -(R*self.getTemperatura())
        C = (a/(self.getTemperatura()**0.5))-(R*self.getTemperatura()*b)-(b*b*self.getPressao())
        D = -((a*b)/(self.getTemperatura()**0.5))
        eq = [A,B,C,D]
        Raizes.raizes(eq)

class SRK(EquacaoDeEstado):
    def getA(self):
        return self.a
    def getB(self):
        return self.b
    def setA(self,a):
        self.a = a
    def setB(self,b):
        self.b = b
    def calcularPressao(self):
        Tr = self.getTemperatura()/self.getTemperaturaCritica()
        kappa = 0.480 + (1.574*self.getFatorAcentrico()) - (0.176*self.getFatorAcentrico()*self.getFatorAcentrico())
        alfa = (1+(kappa*(1-(Tr**0.5))))**2
        self.setA((0.42748*R*R*self.getTemperaturaCritica()*self.getTemperaturaCritica()*alfa)/self.getPressaoCritica())
        self.setB((0.08664*R*self.getTemperaturaCritica())/self.getPressaoCritica())
        self.setPressao(((R*self.getTemperatura())/(self.getVolumeMolar()-self.getB()))-(self.getA()/(self.getVolumeMolar()*(self.getVolumeMolar()+self.getB()))))
    def calcularVolumeMolar(self):
        Tr = self.getTemperatura()/self.getTemperaturaCritica()
        kappa = 0.480 + (1.574*self.getFatorAcentrico()) - (0.176*self.getFatorAcentrico()*self.getFatorAcentrico())
        alfa = (1+(kappa*(1-(Tr**0.5))))**2
        self.setA((0.42748*R*R*self.getTemperaturaCritica()*self.getTemperaturaCritica()*alfa)/self.getPressaoCritica())
        self.setB((0.08664*R*self.getTemperaturaCritica())/self.getPressaoCritica())
        A = self.getPressao()
        B = -(R*self.getTemperatura())
        C = (self.getA() - (R*self.getTemperatura()*self.getB())-(self.getB()*self.getB()*self.getPressao()))
        D = -(self.getA()*self.getB())
        eq = [A,B,C,D]
        Raizes.raizes(eq)
        
class PR(EquacaoDeEstado):
    def calcularPressao(self):
        Tr = self.getTemperatura()/self.getTemperaturaCritica()
        kappa = 0.37464 + (1.54226*self.getFatorAcentrico()) - (0.26992*self.getFatorAcentrico()*self.getFatorAcentrico())
        alfa = (1+(kappa*(1-(Tr**0.5))))**2
        a = (0.45724*R*R*self.getTemperaturaCritica()*self.getTemperaturaCritica()*alfa)/self.getPressaoCritica()
        b = (0.07780*R*self.getTemperaturaCritica())/self.getPressaoCritica()
        self.setPressao(((R*self.getTemperatura())/(self.getVolumeMolar()-b))-(a/((self.getVolumeMolar()*(self.getVolumeMolar()+b))+(b*(self.getVolumeMolar()-b)))))
    def calcularVolumeMolar(self):
        Tr = self.getTemperatura()/self.getTemperaturaCritica()
        kappa = 0.37464 + (1.54226*self.getFatorAcentrico()) - (0.26992*self.getFatorAcentrico()*self.getFatorAcentrico())
        alfa = (1+(kappa+(1-(Tr**0.5))))**2
        a = (0.45724*R*R*self.getTemperaturaCritica()*self.getTemperaturaCritica()*alfa)/self.getPressaoCritica()
        b = (0.07780*R*self.getTemperaturaCritica())/self.getPressaoCritica()
        A = -self.getPressao()
        B = (R*self.getTemperatura())-(self.getPressao()*b)
        C = (2*R*self.getTemperatura()*b) - (a) + (3*b*b*self.getPressao())
        D = -(b*b*b*self.getPressao()) - (R*self.getTemperatura()*b*b) + (a*b)
        eq = [A,B,C,D]
        Raizes.raizes(eq)

class Raizes:
#classe para encontrar as raízes das equações cúbicas de estado para o volume molar
    def raizes(equacao):
        raiz = numpy.roots(equacao)
        if (raiz.imag[0]!=0) or (raiz.imag[1]!=0) or (raiz.imag[2]!=0):
            for p,e in enumerate(raiz.imag):
                if e == 0:
                    print()
                    print(f'{raiz.real[p]:.3e} m³/mol')
        else:
            if raiz.real[0]>raiz.real[1] and raiz.real[0]>raiz.real[2]:
                maior = raiz.real[0]
            elif raiz.real[1]>raiz.real[0] and raiz.real[1]>raiz.real[2]:
                maior = raiz.real[1]
            elif raiz.real[2]>raiz.real[0] and raiz.real[2]>raiz.real[1]:
                maior = raiz.real[2]
            if raiz.real[0]<raiz.real[1] and raiz.real[0]<raiz.real[2]:
                menor = raiz.real[0]
            elif raiz.real[1]<raiz.real[0] and raiz.real[1]<raiz.real[2]:
                menor = raiz.real[1]
            elif raiz.real[2]<raiz.real[0] and raiz.real[2]<raiz.real[1]:
                menor = raiz.real[2]
            print()
            print(f'{maior:.3e} m³/mol - vapor saturado')
            print(f'{menor:.3e} m³/mol - líquido saturado')