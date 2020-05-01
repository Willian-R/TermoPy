# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 18:02:43 2018

@author: Willian Belincanta Ribeiro
"""
import EquacaoDeEstado,PressaodeSaturacao
import numpy
from math import log,exp
R = 8.314
class CoefFugacidadePuras:
    def setComposto(self,composto):
        self.__composto = composto
    def getComposto(self):
        return self.__composto
    def setPressao(self,pressao):
        self.__pressao = pressao
    def getPressao(self):
        return self.__pressao
    def setTemperatura(self,temperatura):
        self.__temperatura = temperatura
    def getTemperatura(self):
        return self.__temperatura
    
    def calcularFugacidade(self):
        q = EquacaoDeEstado.SRK()
        w = PressaodeSaturacao.LeeKeslerSat()
        
        q.buscarPuras(self.getComposto())
        w.buscarLee(self.getComposto())
        q.setTemperatura(self.getTemperatura())
        w.setTemperatura(self.getTemperatura())
        q.setVolumeMolar(1)
        q.calcularPressao()
        w.pressaoSat()
        Psat = w.getPressao()
        Alinha = (q.getA()*self.getPressao())/(R*R*self.getTemperatura()*self.getTemperatura())
        Blinha = (q.getB()*self.getPressao())/(R*self.getTemperatura())
        CoefA = 1
        CoefB = -1
        CoefC = Alinha-Blinha-(Blinha**2)
        CoefD = -(Alinha*Blinha)
        eq = [CoefA,CoefB,CoefC,CoefD]
        raiz = numpy.roots(eq)
        if (raiz.imag[0]!=0) or (raiz.imag[1]!=0) or (raiz.imag[2]!=0):
            for p,e in enumerate(raiz.imag):
                if e == 0:
                    Z = raiz.real[p]
        elif self.getPressao()<Psat:
            if raiz.real[0]>raiz.real[1] and raiz.real[0]>raiz.real[2]:
                Z = raiz.real[0]
            elif raiz.real[1]>raiz.real[0] and raiz.real[1]>raiz.real[2]:
                Z = raiz.real[1]
            elif raiz.real[2]>raiz.real[0] and raiz.real[2]>raiz.real[1]:
                Z = raiz.real[2]
        else:
            if raiz.real[0]<raiz.real[1] and raiz.real[0]<raiz.real[2]:
                Z = raiz.real[0]
            elif raiz.real[1]<raiz.real[0] and raiz.real[1]<raiz.real[2]:
                Z = raiz.real[1]
            elif raiz.real[2]<raiz.real[0] and raiz.real[2]<raiz.real[1]:
                Z = raiz.real[2]
        fi = exp(Z-1-log(Z-Blinha)-((Alinha/Blinha)*log((Z+Blinha)/Z)))
        print(f'{fi:.3f}')

class CoefFugacidadeMisturas:
    def setComposto1(self,composto1):
        self.__composto1 = composto1
    def getComposto1(self):
        return self.__composto1
    def setComposto2(self,composto2):
        self.__composto2 = composto2
    def getComposto2(self):
        return self.__composto2
    def setPressao(self,pressao):
        self.__pressao = pressao
    def getPressao(self):
        return self.__pressao
    def setTemperatura(self,temperatura):
        self.__temperatura = temperatura
    def getTemperatura(self):
        return self.__temperatura
    def setFracaoMolar1(self,fracaomolar1):
        self.__fracaomolar1 = fracaomolar1
    def getFracaoMolar1(self):
        return self.__fracaomolar1
    def setFracaoMolar2(self,fracaomolar2):
        self.__fracaomolar2 = fracaomolar2
    def getFracaoMolar2(self):
        return self.__fracaomolar2
    
    def calcularFugacidade(self):
        o = EquacaoDeEstado.EquacaoDeEstado()
        
        #propriedades puras para o composto 1
        o.buscarPuras(self.getComposto1())
        omega1 = o.getFatorAcentrico()
        tc1 = o.getTemperaturaCritica()
        zc1 = o.getFatorCompCritico()
        vc1 = o.getVolumeMolarCritico()
        pc1 = o.getPressaoCritica()
        tr1 = self.getTemperatura()/tc1
        B01 = 0.083-(0.422/(tr1**1.6))
        B1_1 = 0.139-(0.172/(tr1**4.2))
        B11 = ((R*tc1)/pc1)*(B01+(omega1*B1_1))
        
        #propriedades puras para o composto 2
        o.buscarPuras(self.getComposto2())
        omega2 = o.getFatorAcentrico()
        tc2 = o.getTemperaturaCritica()
        zc2 = o.getFatorCompCritico()
        vc2 = o.getVolumeMolarCritico()
        pc2 = o.getPressaoCritica()
        tr2 = self.getTemperatura()/tc2
        B02 = 0.083-(0.422/(tr2**1.6))
        B1_2 = 0.139-(0.172/(tr2**4.2))
        B22 = ((R*tc2)/pc2)*(B02+(omega2*B1_2))
        
        #propriedades puras para a mistura
        omega12 = (omega1+omega2)/2
        tc12 = (tc1*tc2)**0.5
        zc12 = (zc1+zc2)/2
        vc12 = (((vc1**(1/3))+(vc2**(1/3)))/2) **3
        pc12 = (zc12*R*tc12)/vc12
        tr12 = self.getTemperatura()/tc12
        B012 = 0.083-(0.422/(tr12**1.6))
        B112 = 0.139-(0.172/(tr12**4.2))
        B12 = ((R*tc12)/pc12)*(B012+(omega12*B112))
        
        delta = (2*B12)-(B11)-(B22)
        
        fi1 = exp((self.getPressao()/(R*self.getTemperatura()))*(B11+((self.getFracaoMolar2()**2)*delta)))
        fi2 = exp((self.getPressao()/(R*self.getTemperatura()))*(B22+((self.getFracaoMolar1()**2)*delta)))
        print(f'{fi1:.3f}')
        print(f'{fi2:.3f}')