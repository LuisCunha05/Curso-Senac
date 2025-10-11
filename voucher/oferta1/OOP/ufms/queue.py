
from typing import Any

class Fila:
    def __init__(self, quantidade: int = 5) -> None:
        self._capacidade: int = quantidade
        self._inicio: int = 0
        self._fim: int = 0
        self._tamanho: int = 0
        self._lista: list = [None] * quantidade

    def inicio(self) -> int:
        return self._inicio
    
    def fim(self) -> int:
        return self._fim

    def capacidade(self) -> int:
        return self._capacidade
    
    def contar(self) -> int:
        return self._tamanho
    
    def estaVazio(self) -> bool:
        return self.inicio() == self.fim()
    
    def imprimir(self) -> list:
        print(self._lista)

    def consultar(self) -> Any | None:
        if(self.estaVazio()):
            print('Fila vazia')
            return
        return self._lista[self.inicio()]

    def enfileirar(self, valor: Any):
        if(self.fim() == self.capacidade()):
            print('Fila está cheia')
            return
        
        self._lista[self.fim()] = valor
        self._tamanho += 1
        self._fim += 1

    def desenfileirar(self) -> Any:
        if(self.estaVazio()):
            print('Fila vazia')
            return

        temp = self._lista[self.inicio()]
        self._lista[self.inicio()] = None
        self._tamanho -= 1
        self._inicio += 1

        if(self.estaVazio()):
            self._tamanho = 0
            self._inicio = 0
            self._fim = 0
        return temp

class Interface:
    _OPTIONS = {
    "1": "Consultar",
    "2": "Enfileirar",
    "3": "Desenfileirar",
    "4": "Contar",
    "5": "Imprimir",
    "6": "Esta vazio?",
    "7": "Capacidade da fila",
    "8": "Inicio da fila",
    "9": "Fim da fila",
    "0": "Sair"
    }
    
    @staticmethod
    def exibirOpcoes():
        print("\nDigite a opção desejada:")
        for chave, valor in Interface._OPTIONS.items():
            print(f"{chave}: {valor}")

    @staticmethod
    def pegarOpcao() -> str | None:
        while True:
            Interface.exibirOpcoes()
            opt = input('')

            if(Interface._OPTIONS.get(opt)):
                return opt
            
            print("Opção inválida!")

    @staticmethod
    def app():
        fila = Fila()
        while True:
            opcao = Interface.pegarOpcao()

            match(opcao):
                case "1":
                    val = fila.consultar()
                    if(not val):continue

                    print(f"Primeiro valor: {val}")
                    continue
                case "2":
                    fila.enfileirar(input("Digite um valor para inserir na fila: "))
                    continue
                case "3":
                    print(f"Valor desenfileirado: {fila.desenfileirar()}")
                    continue
                case "4":
                    print(f"Quantidade de elementos: {fila.contar()}")
                    continue
                case "5":
                    fila.imprimir()
                    continue
                case "6":
                    if(fila.estaVazio()):
                        print("Fila está vazia")
                        continue
                    print("Fila não está vazia")
                    continue
                case "7":
                    print(f"Capacidade da fila: {fila.capacidade()}")
                    continue
                case "8":
                    print(f"Index do início da fila: {fila.inicio()}")
                    continue
                case "9":
                    print(f"Index do fim da fila: {fila.fim()}")
                    continue
                case "0":
                    print("Fim da execução!")
                    quit()

Interface.app()
