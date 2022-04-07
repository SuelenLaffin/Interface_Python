
#CLASSES
class Computador:
    def __init__(self,marca,memoria_ram,placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    
# computador1 = Computador('Asus','9gb','nvidia')
# print(computador1.marca,computador1.memoria_ram,computador1.placa_de_video)
# computador2 = Computador('acer','2gb','intel')
# print(computador2.marca,computador2.memoria_ram,computador2.placa_de_video)
# computador3 = Computador('hp','5gb','ryzen')
# print(computador3.marca,computador3.memoria_ram,computador3.placa_de_video)

#MÉTODOS: ligar, desligar, exibir configurações
    def Ligar(self):
        print('estou ligando')

    def Desligar(self):
        print('estou desligando')

    def ExibirInformacoesDesteComputador(self):
        print(self.marca, self.memoria_ram,self.placa_de_video)


computador1 = Computador('Acer','16gb','Nvidia')
computador1.Ligar()
computador1.Desligar()
computador1.ExibirInformacoesDesteComputador()