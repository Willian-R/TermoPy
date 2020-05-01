# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 22:06:33 2018

@author: Willian Belincanta Ribeiro
"""

from math import exp,log
antoine = [#composto,A,B,C
            ['acetona',14.3145,2756.22,228.06],
            ['ácido acético',15.0717,3580.8,224.65],
            ['acetonitrila',14.895,3413.1,250.523],
            ['benzeno',13.7819,2726.81,217.572],
            ['iso-butano',13.8254,2181.79,248.87],
            ['n-butano',13.6608,2154.7,238.789],
            ['1-butanol',15.3144,3212.43,182.739],
            ['2-butanol',15.1989,3026.03,186.5],
            ['iso-butanol',14.6047,2740.95,166.67],
            ['tert-butanol',14.8445,2658.29,177.65],
            ['tetracloreto de carbono',14.0572,2914.23,232.148],
            ['clorobenzeno',13.8635,3174.78,211.7],
            ['1-clorobutano',13.7965,2723.73,218.265],
            ['clorofórmio',13.7324,2548.74,218.552],
            ['ciclo-hexano',13.6568,2723.44,220.618],
            ['ciclopentano',13.9727,2653.9,234.51],
            ['n-decano',13.9748,3442.76,193.858],
            ['diclorometano',13.9891,2463.93,223.24],
            ['éter dietílico',14.0735,2511.29,231.2],
            ['1,4-dioxano',15.0967,3579.78,240.337],
            ['n-eicosano',14.4575,4680.46,132.1],
            ['etanol',16.8958,3795.17,230.918],
            ['etilbenzeno',13.9726,3259.93,212.3],
            ['etileno glicol',15.7567,4187.46,178.65],
            ['n-heptano',13.8622,2910.26,216.432],
            ['n-hexano',13.8193,2696.04,224.317],
            ['metanol',16.5785,3638.27,239.5],
            ['acetato de metila',14.2456,2662.78,219.69],
            ['metiletilcetona',14.1334,2838.24,218.69],
            ['nitrometano',14.7513,3331.7,227.6],
            ['n-nonano',13.9854,3311.19,202.694],
            ['iso-octano',13.6703,2896.31,220.767],
            ['n-octano',13.9346,3123.13,209.635],
            ['n-pentano',13.7667,2451.88,232.014],
            ['fenol',14.4387,3507.8,175.4],
            ['1-propanol',16.1154,3483.67,205.807],
            ['2-propanol',16.6796,3640.2,219.61],
            ['tolueno',13.932,3056.96,217.625],
            ['água',16.3872,3885.7,230.17],
            ['o-xileno',14.0415,3358.79,212.041],
            ['m-xileno',14.1387,3381.81,216.12],
            ['p-xileno',14.0579,3331.45,214.627]]

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
        ['metilciclo-hexano',0.235,572.2,34.71,0.269,368],
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

class Antoine:
#Classe para cálculo da pressão de saturação a partir de Antoine
    def setA(self,A):
        self.__A = A
    def getA(self):
        return self.__A
    def setB(self,B):
        self.__B = B
    def getB(self):
        return self.__B
    def setC(self,C):
        self.__C = C
    def getC(self):
        return self.__C
    #Temperatura em Celsius
    def setTemperatura(self,temperatura):
        self.__temperatura = temperatura
    def getTemperatura(self):
        return self.__temperatura
    def setPressao(self,pressao):
        self.__pressao = pressao
    def getPressao(self):
        return self.__pressao
    def Sim(self):
        return self.sim
    #método para buscar valores na matriz antoine
    def buscarAntoine(self,composto):
            for p in antoine:
                if composto == p[0]:
                    self.setA(p[1])
                    self.setB(p[2])
                    self.setC(p[3])
                    self.sim = 1
                    break
                else:
                    self.sim = 0
    #Pressão em kPa
    def pressaoSat(self):
        self.setPressao(exp(self.getA()-(self.getB()/(self.getTemperatura()+self.getC()))))

class LeeKeslerSat:
#classe para cálculo da pressão de saturação a partir de Lee-Kesler
    #Temperatura em Kelvin
    def setTemperatura(self,temperatura):
        self.__temperatura = temperatura
    def getTemperatura(self):
        return self.__temperatura
    #Temperatura crítica em Kelvin
    def setTemperaturaCritica(self,temperaturacritica):
        self.__temperaturacritica = temperaturacritica
    def getTemperaturaCritica(self):
        return self.__temperaturacritica
    def setPressao(self,pressao):
        self.__pressao = pressao
    def getPressao(self):
        return self.__pressao
    #Pressão crítica em Pascal
    def setPressaoCritica(self,pressaocritica):
        self.__pressaocritica = pressaocritica
    def getPressaoCritica(self):
        return self.__pressaocritica
    def setFatorAcentrico(self,fatoracentrico):
        self.__fatoracentrico = fatoracentrico
    def getFatorAcentrico(self):
        return self.__fatoracentrico
    def Sim(self):
        return self.sim
    #método para buscar valores na matriz puras
    def buscarLee(self,composto):
            for p in puras:
                if composto==p[0]:
                    self.setFatorAcentrico(p[1])
                    self.setTemperaturaCritica(p[2])
                    self.setPressaoCritica(p[3]*1e5)
                    self.sim = 1
                    break
                else:
                    self.sim = 0
    #Pressão em Pascal
    def pressaoSat(self):
        Tr = self.getTemperatura()/self.getTemperaturaCritica()
        lnPr0 = 5.92714 - (6.09648/Tr) - (1.28862*log(Tr)) + (0.169347*(Tr**6))
        lnPr1 = 15.2518 - (15.6875/Tr) - (13.4721*log(Tr)) + (0.43577*(Tr**6))
        Pr = exp(lnPr0 + (self.getFatorAcentrico()*lnPr1))
        self.setPressao(Pr*self.getPressaoCritica())