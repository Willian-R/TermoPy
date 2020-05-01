# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 12:55:47 2018

@author: Willian Belincanta Ribeiro
"""
import PressaodeSaturacao,EquacaoDeEstado,CoeficienteDeFugacidade,PropriedadesResiduais,ELV
print('=-'*30)
print('{:^55}'.format('TermoPy'))
print('=-'*30)
while True:
    print('''Menu
      1 - Pressão de Saturação
      2 - Equações de Estado
      3 - Aplicações em equipamentos
      4 - Coeficiente de Fugacidade
      5 - Equilíbrio Líquido-vapor
      0 - Sair''')
    opc = int(input('Escolha uma opção: '))
    if opc==1:
        print('=-'*30)
        print('{:^55}'.format('Pressão de Saturação'))
        print('=-'*30)
        print('''
              1 - Antoine
              2 - Lee-Kesler
              qualquer tecla para voltar para o menu''')
        opc2 = int(input('Opção: '))
        if opc2 == 1:
            print('=-'*30)
            print('{:^55}'.format('Pressão de Saturação - Antoine'))
            print('=-'*30)
            a = PressaodeSaturacao.Antoine()
            composto = str(input('Composto: ')).strip().lower()
            a.buscarAntoine(composto)
            if a.Sim()!=0:
                temperatura = float(input('Temperatura (ºC): '))
                a.setTemperatura(temperatura)
                a.pressaoSat()
                print(f'{a.getPressao():.3f} kPa')
                print()
            else:
                print('\033[1;37;41mComposto não encontrado')
        elif opc2 == 2:
            print('=-'*30)
            print('{:^55}'.format('Pressão de Saturação - Lee-Kesler'))
            print('=-'*30)
            b = PressaodeSaturacao.LeeKeslerSat()
            composto = str(input('Composto: ')).strip().lower()
            b.buscarLee(composto)
            if b.Sim()!=0:
                temperatura = float(input('Temperatura (K): '))
                b.setTemperatura(temperatura)
                b.pressaoSat()
                print(f'{b.getPressao():.3f} Pa')
                print()
            else:
                print('\033[1;37;41mComposto não encontrado')
        resp = str(input('\033[mDeseja continuar? [S/N] ')).upper()
    elif opc==2:
        print('=-'*30)
        print('{:^55}'.format('Equações de Estado'))
        print('=-'*30)
        print('''
              1 - Gás Ideal
              2 - 2º Coeficiente do Virial
              3 - van der Waals
              4 - Redlich-Kwong
              5 - Soave-Redlich-Kwong
              6 - Peng-Robinson
              qualquer tecla para voltar para o menu''')
        opc2 = int(input('Opção: '))
        if opc2==1:
            print('=-'*30)
            print('{:^55}'.format('Gás Ideal'))
            print('=-'*30)
            print('''
              1 - Pressão
              2 - Volume Molar
              qualquer tecla para voltar para o menu''')
            opc3 = int(input('Opção: '))
            g = EquacaoDeEstado.GasIdeal()
            if opc3==1:
                print('=-'*30)
                print('{:^55}'.format('Equação de Estado - Gás Ideal - Pressão'))
                print('=-'*30)
                composto = str(input('Composto: ')).strip().lower()
                temperatura = float(input('Temperatura (K): '))
                volumemolar = float(input('Volume molar (m³/mol): '))
                g.buscarPuras(composto)
                g.setTemperatura(temperatura)
                g.setVolumeMolar(volumemolar)
                g.calcularPressao()
                print(f'Pressão: {g.getPressao():.3f} Pa')
                print()
            elif opc3==2:
                print('=-'*30)
                print('{:^55}'.format('Equação de Estado - Gás Ideal - Volume Molar'))
                print('=-'*30)
                composto = str(input('Composto: ')).strip().lower()
                temperatura = float(input('Temperatura (K): '))
                pressao = float(input('Pressão (Pa): '))
                g.buscarPuras(composto)
                g.setTemperatura(temperatura)
                g.setPressao(pressao)
                g.calcularVolumeMolar()
                print(f'Volume molar: {g.getVolumeMolar():.3e} m³/mol')
                print()
        elif opc2==2:
            print('=-'*30)
            print('{:^55}'.format('2º Coeficiente do Virial'))
            print('=-'*30)
            print('''
              1 - Pressão
              2 - Volume Molar
              qualquer tecla para voltar para o menu''')
            opc3 = int(input('Opção: '))
            h = EquacaoDeEstado.Virial()
            if opc3 == 1:
                print('=-'*30)
                print('{:^55}'.format('Equação de Estado - 2º Coeficiente do Virial - Pressão'))
                print('=-'*30)
                composto = str(input('Composto: ')).strip().lower()
                h.buscarPuras(composto)
                if h.getSim()!=0:
                    temperatura = float(input('Temperatura (K): '))
                    volumemolar = float(input('Volume molar (m³/mol): '))
                    h.setTemperatura(temperatura)
                    h.setVolumeMolar(volumemolar)
                    h.calcularPressao()
                    print(f'Pressão: {h.getPressao():.3f} Pa')
                    print()
                else:
                    print('\033[1;37;41mComposto não encontrado')
            elif opc3 == 2:
                print('=-'*30)
                print('{:^55}'.format('Equação de Estado - 2º Coeficiente do Virial - Volume Molar'))
                print('=-'*30)
                composto = str(input('Composto: ')).strip().lower()
                h.buscarPuras(composto)
                if h.getSim()!=0:
                    temperatura = float(input('Temperatura (K): '))
                    pressao = float(input('Pressão (Pa): '))
                    h.setTemperatura(temperatura)
                    h.setPressao(pressao)
                    h.calcularVolumeMolar()
                    print(f'Volume molar: {h.getVolumeMolar():.3e} m³/mol')
                    print()
                else:
                    print('\033[1;37;41mComposto não encontrado')
        elif opc2==3:
            print('=-'*30)
            print('{:^55}'.format('van der Waals'))
            print('=-'*30)
            print('''
              1 - Pressão
              2 - Volume Molar
              qualquer tecla para voltar para o menu''')
            opc3 = int(input('Opção: '))
            i = EquacaoDeEstado.VDW()
            if opc3 == 1:
                print('=-'*30)
                print('{:^55}'.format('Equação de Estado - van der Waals - Pressão'))
                print('=-'*30)
                composto = str(input('Composto: ')).strip().lower()
                i.buscarPuras(composto)
                if i.getSim()!=0:
                    temperatura = float(input('Temperatura (K): '))
                    volumemolar = float(input('Volume molar (m³/mol): '))
                    i.setTemperatura(temperatura)
                    i.setVolumeMolar(volumemolar)
                    i.calcularPressao()
                    print(f'Pressão: {i.getPressao():.3f} Pa')
                    print()
                else:
                    print('\033[1;37;41mComposto não encontrado')
            elif opc3 == 2:
                print('=-'*30)
                print('{:^55}'.format('Equação de Estado - van der Waals - Volume Molar'))
                print('=-'*30)
                composto = str(input('Composto: ')).strip().lower()
                i.buscarPuras(composto)
                if i.getSim()!=0:
                    temperatura = float(input('Temperatura (K): '))
                    pressao = float(input('Pressão (Pa): '))
                    i.setTemperatura(temperatura)
                    i.setPressao(pressao)
                    i.calcularVolumeMolar()
                    print()
                else:
                    print('\033[1;37;41mComposto não encontrado')
        elif opc2==4:
            print('=-'*30)
            print('{:^55}'.format('Redlich-Kwong'))
            print('=-'*30)
            print('''
              1 - Pressão
              2 - Volume Molar
              qualquer tecla para voltar para o menu''')
            opc3 = int(input('Opção: '))
            j = EquacaoDeEstado.RK()
            if opc3 == 1:
                print('=-'*30)
                print('{:^55}'.format('Equação de Estado - Redlich-Kwong - Pressão'))
                print('=-'*30)
                composto = str(input('Composto: ')).strip().lower()
                temperatura = float(input('Temperatura (K): '))
                volumemolar = float(input('Volume molar (m³/mol): '))
                j.buscarPuras(composto)
                j.setTemperatura(temperatura)
                j.setVolumeMolar(volumemolar)
                j.calcularPressao()
                print(f'Pressão: {j.getPressao():.3f} Pa')
                print()
            elif opc3 == 2:
                print('=-'*30)
                print('{:^55}'.format('Equação de Estado - Redlich-Kwong - Volume Molar'))
                print('=-'*30)
                composto = str(input('Composto: ')).strip().lower()
                temperatura = float(input('Temperatura (K): '))
                pressao = float(input('Pressão (Pa): '))
                j.buscarPuras(composto)
                j.setTemperatura(temperatura)
                j.setPressao(pressao)
                j.calcularVolumeMolar()
                print()
        elif opc2==5:
            print('=-'*30)
            print('{:^55}'.format('Soave-Redlich-Kwong'))
            print('=-'*30)
            print('''
              1 - Pressão
              2 - Volume Molar
              qualquer tecla para voltar para o menu''')
            opc3 = int(input('Opção: '))
            k = EquacaoDeEstado.SRK()
            if opc3 == 1:
                print('=-'*30)
                print('{:^55}'.format('Equação de Estado - Soave-Redlich Kwong - Pressão'))
                print('=-'*30)
                composto = str(input('Composto: ')).strip().lower()
                temperatura = float(input('Temperatura (K): '))
                volumemolar = float(input('Volume molar (m³/mol): '))
                k.buscarPuras(composto)
                k.setTemperatura(temperatura)
                k.setVolumeMolar(volumemolar)
                k.calcularPressao()
                print(f'Pressão: {k.getPressao():.3f} Pa')
                print()
            elif opc3 == 2:
                print('=-'*30)
                print('{:^55}'.format('Equação de Estado - Soave-Redlich-Kwong - Volume Molar'))
                print('=-'*30)
                composto = str(input('Composto: ')).strip().lower()
                temperatura = float(input('Temperatura (K): '))
                pressao = float(input('Pressão (Pa): '))
                k.buscarPuras(composto)
                k.setTemperatura(temperatura)
                k.setPressao(pressao)
                k.calcularVolumeMolar()
                print()
        elif opc2==6:
            print('=-'*30)
            print('{:^55}'.format('Peng-Robinson'))
            print('=-'*30)
            print('''
              1 - Pressão
              2 - Volume Molar
              qualquer tecla para voltar para o menu''')
            opc3 = int(input('Opção: '))
            l = EquacaoDeEstado.PR()
            if opc3 == 1:
                print('=-'*30)
                print('{:^55}'.format('Equação de Estado - Peng-Robinson - Pressão'))
                print('=-'*30)
                composto = str(input('Composto: ')).strip().lower()
                temperatura = float(input('Temperatura (K): '))
                volumemolar = float(input('Volume molar (m³/mol): '))
                l.buscarPuras(composto)
                l.setTemperatura(temperatura)
                l.setVolumeMolar(volumemolar)
                l.calcularPressao()
                print(f'Pressão: {l.getPressao():.3f} Pa')
                print()
            elif opc3 == 2:
                print('=-'*30)
                print('{:^55}'.format('Equação de Estado - Peng-Robinson - Volume Molar'))
                print('=-'*30)
                composto = str(input('Composto: ')).strip().lower()
                temperatura = float(input('Temperatura (K): '))
                pressao = float(input('Pressão (Pa): '))
                l.buscarPuras(composto)
                l.setTemperatura(temperatura)
                l.setPressao(pressao)
                l.calcularVolumeMolar()
                print()
        resp = str(input('\033[mDeseja continuar? [S/N] ')).upper()
    elif opc==3:
        print('=-'*30)
        print('{:^55}'.format('Aplicação em equipamentos'))
        print('=-'*30)
        m = PropriedadesResiduais.PropriedadesResiduais()
        mm = EquacaoDeEstado.EquacaoDeEstado()
        print('''Equipamentos disponíveis para cálculo de trabalho
              1 - Compressor
              2 - Turbina''')
        equipamento = int(input('Escolha o equipamento: '))
        composto = str(input('Composto: ')).strip().lower()
        pressaoi = float(input('Pressão da entrada (Pa): '))
        temperaturai = float(input('Temperatura da entrada (K): '))
        pressaof = float(input('Pressão da saída (Pa): '))
        temperaturaf = float(input('Temperatura da saída (K): '))
        m.setEquipamento(equipamento)
        m.setComposto(composto)
        mm.buscarPuras(composto)
        m.setPressaoInicial(pressaoi)
        m.setPressaoFinal(pressaof)
        m.setTemperaturaFinal(temperaturaf)
        m.setTemperaturaInicial(temperaturai)
        m.calcularResidual()
        print()
        resp = str(input('\033[mDeseja continuar? [S/N] ')).upper()
    elif opc==4:
        print('=-'*30)
        print('{:^55}'.format('Coefiente de Fugacidade'))
        print('=-'*30)
        print('''
              1 - Pura
              2 - Misturas
              qualquer tecla para voltar para o menu''')
        opc2 = int(input('Opção: '))
        if opc2==1:
            c = CoeficienteDeFugacidade.CoefFugacidadePuras()
            print('=-'*30)
            print('{:^55}'.format('Coefiente de Fugacidade - Espécie Pura'))
            print('=-'*30)
            composto = str(input('Composto: ')).strip().lower()
            temperatura = float(input('Temperatura (K): '))
            pressao = float(input('Pressão (Pa): '))
            c.setComposto(composto)
            c.setTemperatura(temperatura)
            c.setPressao(pressao)
            c.calcularFugacidade()
            print()
        elif opc2==2:
            print('=-'*30)
            print('{:^55}'.format('Coefiente de Fugacidade - Misturas'))
            print('=-'*30)
            d = CoeficienteDeFugacidade.CoefFugacidadeMisturas()
            dd = EquacaoDeEstado.EquacaoDeEstado()
            composto1 = str(input('Composto (1): ')).strip().lower()
            dd.buscarPuras(composto1)
            b1 = dd.getSim()
            composto2 = str(input('Composto (2): ')).strip().lower()
            dd.buscarPuras(composto2)
            b2 = dd.getSim()
            temperatura = float(input('Temperatura (K): '))
            pressao = float(input('Pressão (Pa): '))
            frac1 = float(input('Fração molar (1): '))
            frac2 = float(input('Fração molar (2): '))
            d.setComposto1(composto1)
            d.setComposto2(composto2)
            d.setTemperatura(temperatura)
            d.setPressao(pressao)
            d.setFracaoMolar1(frac1)
            d.setFracaoMolar2(frac2)
            d.calcularFugacidade()
            print()
        resp = str(input('\033[mDeseja continuar? [S/N] ')).upper()
    elif opc==5:
        print('=-'*30)
        print('{:^55}'.format('Equilíbrio Líquido-Vapor'))
        print('=-'*30)
        print('''
              1 - Margules
              2 - Wilson
              qualquer tecla para voltar para o menu''')
        opc2 = int(input('Opção: '))
        if opc2==1:
            print('=-'*30)
            print('{:^55}'.format('Equilíbrio Líquido-Vapor - Margules'))
            print('=-'*30)
            e = ELV.Margules()
            ee = EquacaoDeEstado.EquacaoDeEstado()
            composto1 = str(input('Composto (1): ')).strip().lower()
            ee.buscarPuras(composto1)
            b1 = ee.getSim()
            composto2 = str(input('Composto (2): ')).strip().lower()
            ee.buscarPuras(composto2)
            b2 = ee.getSim()
            temperatura = float(input('Temperatura (ºC): '))
            variacao = float(input('Variação: '))
            a12 = float(input('A12: '))
            a21 = float(input('A21: '))
            e.setComposto1(composto1)
            e.setComposto2(composto2)
            e.setTemperatura(temperatura)
            e.setvariacao(variacao)
            e.setA12(a12)
            e.setA21(a21)
            e.grafico()
        elif opc2==2:
            print('=-'*30)
            print('{:^55}'.format('Equilíbrio Líquido-Vapor - Wilson'))
            print('=-'*30)
            f = ELV.Wilson()
            ff = EquacaoDeEstado.EquacaoDeEstado()
            composto1 = str(input('Composto (1): ')).strip().lower()
            ff.buscarPuras(composto1)
            b1 = ff.getSim()
            composto2 = str(input('Composto (2): ')).strip().lower()
            ff.buscarPuras(composto2)
            b2 = ff.getSim()
            temperatura = float(input('Temperatura (ºC): '))
            variacao = float(input('Variação: '))
            lambda12 = float(input('Lambda12: '))
            lambda21 = float(input('Lambda21: '))
            f.setComposto1(composto1)
            f.setComposto2(composto2)
            f.setTemperatura(temperatura)
            f.setvariacao(variacao)
            f.setLambda12(lambda12)
            f.setLambda21(lambda21)
            f.grafico()
        resp = str(input('\033[mDeseja continuar? [S/N] ')).upper()
    elif opc==0:
        break
    if resp=='N':
        break
    print('=-'*30)