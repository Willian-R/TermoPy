# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 22:12:00 2018

@author: Willian Belincanta Ribeiro
"""
import EquacaoDeEstado,PressaodeSaturacao
import numpy
from math import sqrt,log
R = 8.314
cpideal = [
        ['metano',1.702,9.081,-2.164,0],
        ['etano',1.131,19.225,-5.561,0],
        ['propano',1.213,28.785,-8.824,0],
        ['n-butano',1.935,36.915,-11.402,0],
        ['iso-butano',1.677,37.853,-11.945,0],
        ['n-pentano',2.464,45.351,-14.111,0],
        ['n-hexano',3.025,53.722,-16.791,0],
        ['n-heptano',3.570,62.127,-19.486,0],
        ['n-octano',4.108,70.567,-22.208,0],
        ['etileno',1.424,14.394,-4.392,0],
        ['propileno',1.637,22.706,-6.915,0],
        ['1-buteno',1.967,31.630,-9.873,0],
        ['1-penteno',2.691,39.753,-12.447,0],
        ['1-hexeno',3.220,48.189,-15.157,0],
        ['1-hepteno',3.768,56.588,-17.847,0],
        ['1-octeno',4.324,64.960,-20.521,0],
        ['acetaldeído',1.693,17.978,-6.158,0],
        ['acetileno',6.132,1.952,0,-1.299],
        ['benzeno',-0.206,39.064,-13.301,0],
        ['1,3-butadieno',2.734,26.786,-8.882,0],
        ['ciclo-hexano',-3.876,63.249,-20.928,0],
        ['etanol',3.518,20.001,-6.002,0],
        ['etilbenzeno',1.124,55.380,-18.476,0],
        ['óxido de etileno',-0.385,22.463,-9.296,0],
        ['formaldeído',2.264,7.022,-1.877,0],
        ['metanol',2.211,12.216,-3.450,0],
        ['estireno',2.050,50.192,-16.662,0],
        ['tolueno',0.290,47.052,-15.716,0],
        ['ar',3.355,0.575,0,-0.016],
        ['amônia',3.578,3.020,0,-0.186],
        ['bromo',4.493,0.056,0,-0.154],
        ['monóxido de carbono',3.376,0.557,0,-0.031],
        ['dióxido de carbono',5.457,1.045,0,-1.157],
        ['dissulfeto de carbono',6.311,0.805,0,-0.906],
        ['cloro',4.442,0.089,0,-0.344],
        ['hidrogênio',3.249,0.422,0,0.083],
        ['dissulfeto de hidrogênio',3.931,1.490,0,-0.232],
        ['cloreto de hidrogênio',3.156,0.623,0,0.151],
        ['cianeto de hidrogênio',4.736,1.359,0,-0.725],
        ['nitrogênio',3.280,0.593,0,0.040],
        ['óxido nitroso',5.328,1.214,0,-0.928],
        ['óxido nítrico',3.387,0.629,0,0.014],
        ['dióxido de nitrogênio',4.982,1.195,0,-0.792],
        ['tetraóxido de dinitrogênio',11.660,2.257,0,-2.787],
        ['oxigênio',3.639,0.506,0,-0.227],
        ['dióxido de enxofre',5.699,0.801,0,-1.015],
        ['trióxido de enxofre',8.060,1.056,0,-2.028],
        ['água',3.470,1.450,0,0.121]]

class PropriedadesResiduais:
    def setComposto(self,composto):
        self.__composto = composto
    def getComposto(self):
        return self.__composto
    #Pressão em Pascal
    def getPressaoInicial(self):
        return self.__pressaoinicial
    def setPressaoInicial(self,pressaoinicial):
        self.__pressaoinicial = pressaoinicial
    def getPressaoFinal(self):
        return self.__pressaofinal
    def setPressaoFinal(self,pressaofinal):
        self.__pressaofinal = pressaofinal
    #Temperatura em Kelvin
    def getTemperaturaInicial(self):
        return self.__temperaturainicial
    def setTemperaturaInicial(self,temperaturainicial):
        self.__temperaturainicial = temperaturainicial
    def getTemperaturaFinal(self):
        return self.__temperaturafinal
    def setTemperaturaFinal(self,temperaturafinal):
        self.__temperaturafinal = temperaturafinal
    def setEquipamento(self,equipamento):
        self.__equipamento = equipamento
    def getEquipamento(self):
        return self.__equipamento
    
    def calcularResidual(self):
        n = EquacaoDeEstado.SRK()
        u = PressaodeSaturacao.LeeKeslerSat()
        n.buscarPuras(self.getComposto())
        u.buscarLee(self.getComposto())
        
        #calcula propriedade residual na entrada
        n.setTemperatura(self.getTemperaturaInicial())
        u.setTemperatura(self.getTemperaturaInicial())
        n.setVolumeMolar(1)
        u.pressaoSat()
        n.calcularPressao()
        Psat = u.getPressao()
        Alinha = (n.getA()*self.getPressaoInicial())/(R*R*self.getTemperaturaInicial()*self.getTemperaturaInicial())
        Blinha = (n.getB()*self.getPressaoInicial())/(R*self.getTemperaturaInicial())
        CoefA = 1
        CoefB = -1
        CoefC = Alinha-Blinha-(Blinha**2)
        CoefD = -(Alinha*Blinha)
        eq = [CoefA,CoefB,CoefC,CoefD]
        raiz = numpy.roots(eq)
        if (raiz.imag[0]!=0) or (raiz.imag[1]!=0) or (raiz.imag[2]!=0):
            for p,e in enumerate(raiz.imag):
                if e == 0:
                    Zinicial = raiz.real[p]
        elif self.getPressaoInicial()<Psat:
            if raiz.real[0]>raiz.real[1] and raiz.real[0]>raiz.real[2]:
                Zinicial = raiz.real[0]
            elif raiz.real[1]>raiz.real[0] and raiz.real[1]>raiz.real[2]:
                Zinicial = raiz.real[1]
            elif raiz.real[2]>raiz.real[0] and raiz.real[2]>raiz.real[1]:
                Zinicial = raiz.real[2]
        else:
            if raiz.real[0]<raiz.real[1] and raiz.real[0]<raiz.real[2]:
                Zinicial = raiz.real[0]
            elif raiz.real[1]<raiz.real[0] and raiz.real[1]<raiz.real[2]:
                Zinicial = raiz.real[1]
            elif raiz.real[2]<raiz.real[0] and raiz.real[2]<raiz.real[1]:
                Zinicial = raiz.real[2]
        Tr = self.getTemperaturaInicial()/n.getTemperaturaCritica()
        da = ((-0.42748*R*R*n.getTemperaturaCritica())/n.getPressaoCritica())*((1+(n.getFatorAcentrico()*(1-sqrt(Tr))*n.getFatorAcentrico()))/sqrt(Tr))
        HrInicial = (R*self.getTemperaturaInicial()*(Zinicial-1))+((((self.getTemperaturaInicial()*da)-n.getA())/n.getB())*log((Zinicial+Blinha)/Zinicial))
        SrInicial = (R*log(Zinicial-Blinha))+((da/n.getB())*log((Zinicial+Blinha)/Zinicial))
        
        #calcula propriedade residual na saída
        n.setTemperatura(self.getTemperaturaFinal())
        u.setTemperatura(self.getTemperaturaFinal())
        n.setVolumeMolar(1)
        u.pressaoSat()
        n.calcularPressao()
        Psat = u.getPressao()
        Alinha = (n.getA()*self.getPressaoFinal())/(R*R*self.getTemperaturaFinal()*self.getTemperaturaFinal())
        Blinha = (n.getB()*self.getPressaoFinal())/(R*self.getTemperaturaFinal())
        CoefA = 1
        CoefB = -1
        CoefC = Alinha-Blinha-(Blinha**2)
        CoefD = -(Alinha*Blinha)
        eq = [CoefA,CoefB,CoefC,CoefD]
        raiz = numpy.roots(eq)
        if (raiz.imag[0]!=0) or (raiz.imag[1]!=0) or (raiz.imag[2]!=0):
            for p,e in enumerate(raiz.imag):
                if e == 0:
                    Zfinal = raiz.real[p]
        elif self.getPressaoInicial()<Psat:
            if raiz.real[0]>raiz.real[1] and raiz.real[0]>raiz.real[2]:
                Zfinal = raiz.real[0]
            elif raiz.real[1]>raiz.real[0] and raiz.real[1]>raiz.real[2]:
                Zfinal = raiz.real[1]
            elif raiz.real[2]>raiz.real[0] and raiz.real[2]>raiz.real[1]:
                Zfinal = raiz.real[2]
        else:
            if raiz.real[0]<raiz.real[1] and raiz.real[0]<raiz.real[2]:
                Zfinal = raiz.real[0]
            elif raiz.real[1]<raiz.real[0] and raiz.real[1]<raiz.real[2]:
                Zfinal = raiz.real[1]
            elif raiz.real[2]<raiz.real[0] and raiz.real[2]<raiz.real[1]:
                Zfinal = raiz.real[2]
        Tr = self.getTemperaturaFinal()/n.getTemperaturaCritica()
        da = (-(0.42748*R*R*n.getTemperaturaCritica())/n.getPressaoCritica())*((1+(n.getFatorAcentrico()*(1-sqrt(Tr))*n.getFatorAcentrico()))/sqrt(Tr))
        HrFinal = (R*self.getTemperaturaFinal()*(Zfinal-1))+((((self.getTemperaturaFinal()*da)-n.getA())/n.getB())*log((Zfinal+Blinha)/Zfinal))
        SrFinal = (R*log(Zfinal-Blinha))+((da/n.getB())*log((Zfinal+Blinha)/Zfinal))
        
        #cálculo propriedade comportamento ideal
        for e in cpideal:
            if self.getComposto()==e[0]:
                A = e[1]
                B = e[2]*(1e-3)
                C = e[3]*(1e-6)
                D = e[4]*(1e5)
        HIdeal = R*((A*(self.getTemperaturaFinal()-self.getTemperaturaInicial()))+((B*((self.getTemperaturaFinal()**2)-(self.getTemperaturaInicial()**2)))/2)+((C*((self.getTemperaturaFinal()**3)-(self.getTemperaturaInicial()**3)))/3)-(D*((self.getTemperaturaFinal()**(-1))-(self.getTemperaturaInicial()**(-1)))))
        varentalpia = HrInicial+HIdeal+HrFinal
        SIdeal = ((R*((A*(self.getTemperaturaFinal()-self.getTemperaturaInicial()))+((B*((self.getTemperaturaFinal()**2)-(self.getTemperaturaInicial()**2)))/2)+((C*((self.getTemperaturaFinal()**3)-(self.getTemperaturaInicial()**3)))/3)-(D*((self.getTemperaturaFinal()**(-1))-(self.getTemperaturaInicial()**(-1))))))/(self.getTemperaturaFinal()-self.getTemperaturaInicial()))-(R*log(self.getPressaoFinal()/self.getPressaoInicial()))
        varentropia = SrInicial+SIdeal+SrFinal
        
        print(f'W = {varentalpia:.3f} J/mol')
        if (self.getEquipamento()==1 and varentalpia<0) or (self.getEquipamento()==2 and varentalpia>0):
            print('\033[4;31mViola a 1ª lei da termodinâmica')
        else:
            print(f'S = {varentropia:.3f} J/mol.K')
            if varentropia<0:
                print('Processo impossível')
            elif varentropia==0:
                print('Processo possível reversível ')
            else:
                print('Processo possível irreversível')