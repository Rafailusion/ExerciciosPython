class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def envelhecer(self):
        self.idade += 1
    def engordar(self):
        self.peso += 1
    def emagrecer(self):
        self.peso -= 1
    def crescer(self):
        if self.idade < 21:
            self.altura += 0.5

Rafael = Pessoa(nome = 'Rafael', idade = 10, peso = 70.0, altura = 1.78)
print(f'Nome: {Rafael.nome}, Idade: {Rafael.idade}, Peso: {Rafael.peso}, Altura: {Rafael.altura}')
while Rafael.idade < 80:
    Rafael.envelhecer()
    Rafael.engordar()
    Rafael.emagrecer()
    Rafael.crescer()
    print(f'Nome: {Rafael.nome}, Idade: {Rafael.idade}, Peso: {Rafael.peso}, Altura: {round(Rafael.altura,2)}')


