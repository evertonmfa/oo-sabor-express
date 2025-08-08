class Pessoa:

    pessoas = []

    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profisao = profissao
        Pessoa.pessoas.append(self)
        
    def __str__(self):
        return f'{self.nome} | {self.profisao}'
    
    @classmethod
    def aniversario(cls):
        
        print(f'{'  Nome'.ljust(10)} | {'idade'} ')
        for pessoa in cls.pessoas:
            print(f'{pessoa.nome.ljust(10)} | {pessoa.idade + 1} anos')  
   

    @property
    
    def saudacao(self):
        return  print(f'Olá {self.nome} vejo que trabalha com {self.profisao}')

pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=22, profissao='Desenvolvedor')

Pessoa.aniversario()


