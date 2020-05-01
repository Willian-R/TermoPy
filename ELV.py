# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 17:41:19 2018

@author: Willian Belincanta Ribeiro
"""
import matplotlib.pyplot as grafico
from math import exp,log
import PressaodeSaturacao

x1Margules = []
y1Margules = []
PMargules = []
class Margules:
    def setA12(self,A12):
        self.__A12 = A12
    def getA12(self):
        return self.__A12
    def setA21(self,A21):
        self.__A21 = A21
    def getA21(self):
        return self.__A21
    def setvariacao(self,variacao):
        self.__variacao = variacao
    def getvariacao(self):
        return self.__variacao
    def setComposto1(self,composto1):
        self.__composto1 = composto1
    def getComposto1(self):
        return self.__composto1
    def setComposto2(self,composto2):
        self.__composto2 = composto2
    def getComposto2(self):
        return self.__composto2
    def setTemperatura(self,temperatura):
        self.__temperatura = temperatura
    def getTemperatura(self):
        return self.__temperatura
    
    def grafico(self):
        q = PressaodeSaturacao.Antoine()
        x1 = 0
        c1 = self.getComposto1()
        q.buscarAntoine(c1)
        t = self.getTemperatura()
        q.setTemperatura(t)
        q.pressaoSat()
        Psat = q.getPressao()
        P1sat = Psat
        c2 = self.getComposto2()
        q.buscarAntoine(c2)
        q.setTemperatura(t)
        q.pressaoSat()
        Psat = q.getPressao()       
        P2sat = Psat
        var = self.getvariacao()
        
        while x1<=1:
            if x1==0:
                gama1=0
            else:
                gama1 = exp(((1-x1)**2)*(self.getA12()+(2*(self.getA21()-self.getA12())*x1)))
            if x1==1:
                gama2=0
            else:
                gama2 = exp((x1**2)*(self.getA21()+(2*(self.getA12()-self.getA21())*(1-x1))))
            P = (x1*gama1*P1sat)+((1-x1)*gama2*P2sat)
            y1 = (x1*gama1*P1sat)/P
            x1Margules.append(x1)
            y1Margules.append(y1)
            PMargules.append(P)
            x1=x1+var
        grafico.plot(x1Margules,PMargules,'r',y1Margules,PMargules,'b')
        grafico.xlabel('x1,y1')
        grafico.ylabel('pressão')
        grafico.show()
        
x1Wilson = []
y1Wilson = []
PWilson = []
class Wilson:
    def setLambda12(self,lambda12):
        self.__lambda12 = lambda12
    def getLambda12(self):
        return self.__lambda12
    def setLambda21(self,lambda21):
        self.__lambda21 = lambda21
    def getLambda21(self):
        return self.__lambda21
    def setvariacao(self,variacao):
        self.__variacao = variacao
    def getvariacao(self):
        return self.__variacao
    def setComposto1(self,composto1):
        self.__composto1 = composto1
    def getComposto1(self):
        return self.__composto1
    def setComposto2(self,composto2):
        self.__composto2 = composto2
    def getComposto2(self):
        return self.__composto2
    def setTemperatura(self,temperatura):
        self.__temperatura = temperatura
    def getTemperatura(self):
        return self.__temperatura
    
    def grafico(self):
        w = PressaodeSaturacao.Antoine()
        x1 = 0
        c1 = self.getComposto1()
        w.buscarAntoine(c1)
        t = self.getTemperatura()
        w.setTemperatura(t)
        w.pressaoSat()
        Psat = w.getPressao()
        P1sat = Psat
        c2 = self.getComposto2()
        w.buscarAntoine(c2)
        w.setTemperatura(t)
        w.pressaoSat()
        Psat = w.getPressao()       
        P2sat = Psat
        var = self.getvariacao()
        while x1<=1:
            gama1 = exp(-log(x1+((1-x1)*self.getLambda12()))+((1-x1)*((self.getLambda12()/(x1+((1-x1)*self.getLambda12())))-(self.getLambda21()/((1-x1)+(x1*self.getLambda21()))))))
            gama2 = exp(-log((1-x1)+(x1*self.getLambda21()))-(x1*((self.getLambda12()/(x1+((1-x1)*self.getLambda12())))-(self.getLambda21()/((1-x1)+(x1*self.getLambda21()))))))
            P = (x1*gama1*P1sat)+((1-x1)*gama2*P2sat)
            y1 = (x1*gama1*P1sat)/P
            x1Wilson.append(x1)
            y1Wilson.append(y1)
            PWilson.append(P)
            x1=x1+var
        grafico.plot(x1Wilson,PWilson,'r',y1Wilson,PWilson,'b')
        grafico.xlabel('x1,y1')
        grafico.ylabel('pressão')
        grafico.show()