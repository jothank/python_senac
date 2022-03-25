class Animal():

    def __init__(self, tamanho: float, peso: float, raca: str, especie: str) -> None:
        self.tamanho = tamanho
        self.peso = peso
        self.raca = raca
        self.especie = especie
        self.sexo = None

    def mover(self):
        print(f"O animal {self.raca} está se movendo.")

    def comer(self):
        print(f"O animal {self.raca} está comendo.")

    def dormir(self):
        print(f"O animal {self.raca} está dormindo.")

    def reproduzir(self):
        print(f"O animal {self.raca} está dose reproduzindo.")
