class Carro():
    def __init__(self,marca,cor,ano,modelo):
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.modelo = modelo


# MÉTODOS

    def Ligar(self):
        print('estou ligado')

    def Desligar(self):
        print('Estou desligado')

    def InformacoesCarro(self):
        print(self.marca, self.cor, self.ano, self.modelo)

carro1 = Carro('Fiat','branco','2020','cronos')
carro1.Ligar()
carro1.Desligar()
carro1.InformacoesCarro()
        