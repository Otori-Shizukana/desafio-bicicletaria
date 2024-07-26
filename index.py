from time import sleep
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    def buzinar(self):
        print("Plim Plim")
    def parar(self):
        print("Parando Bicicleta...")
        sleep(2)
        print("Bicicleta Parada")
    def correr(self):
        print("Vrummmm...")
    #def __str__(self):
    #   return f"Bicicleta: Cor={self.cor}, Modelo={self.modelo}, Ano={self.ano}, Valor={self.valor}"
    #def __str__(self):
    #    return f"{self.__class__.__name__}: Cor= {self.cor}, Modelo= {self.modelo}, Ano= {self.ano}, Valor= {self.valor}"
    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

bike1 = Bicicleta("Preto com verde","Titan aro 29", 2023, 1200)
bike2= Bicicleta("Laranja", "Colli bike", 2024, 755.92)

bike1.correr()
bike1.buzinar()
bike1.parar()
print(bike1)

bike2.correr()
bike2.buzinar()
bike2.parar()
print(bike2)