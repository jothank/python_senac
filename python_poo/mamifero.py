from animal import Animal


class Mamifero(Animal):

    def __init__(self, tamanho: float, peso: float, raca: str, especie: str) -> None:
        super().__init__(tamanho, peso, raca, especie)

    def amamentar(self):
        print("Este mamifero está amamentando.")
