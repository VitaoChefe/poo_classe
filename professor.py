class Pessoa:
    def __init__(self, nome, idade,cpf, salario, trabalhando=True, estudando=False):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.salario = salario
        self.trabalhando = trabalhando
        self.estudando = estudando



    def apresentar(self):
        print(f'bom dia a todos e todas, sou professor {self.nome}\n'
              f'minha idade é {self.idade}\n'
              f'meu CPF é {self.cpf}\n'
              f'meu salario é {self.salario}\n'
              )

        if self.estudando:
            print(' estou estudando')
        else:
            print(f"não esta estudando")

        if self.trabalhando:
            print('estou trabalhando')
        else:
            print(f"não estou trabalhando")

        print("-" * 50)

    def receber(self):
        if self.trabalhando:
            print('estou trabalhando')
            self.salario = self.salario + 100
        else:
            print(f"não estou trabalhando")


class Professor(Pessoa): # herda da classe do professor
    def __init__(self, nome, idade,cpf, salario,materia,local,turma,trabalho=True):
        super().__init__( nome, idade,cpf,salario, materia)
        self.nome = nome
        self.idade = idade
        self.local = local
        self.salario = salario
        self.quantidade_aula = turma
        self.quantidade = 10
        self.trabalho = trabalho
        self.materia = materia

    def apresentar(self):
        print(f"meu nome é {self.nome}"
        f" minha idade é{self.idade} "
        f"a escola que eu trabalho é{self.local} "
        f" meu salario é{self.salario} "
        f" quantidades de aula que eu dou{self.quantidade_turma} "
        f" eu trabalho {self.trabalho}  "
        f" a matéria que eu dou aula é{self.materia}  "
        )
    def quantidade_de_aulas(self):
        if self.local:
            aumento = (self.quantidade_aula + self.quantidade_aula)
            print(f"Eu dava {self.quantidade_aula} de aulas,agora dou {aumento} aulas")
        elif self.local:
            print(f"Eu dou aulas")
        else:
            print(f"Eu não dou aulas")

    def receber(self):
        if self.salario:
            print(f"ele não recebe, pois ele não trabalha!!")
        else:
            print('estou trabalhando')

    def passar_materia(self):
        if self.materia:
            print(f'Eu dou aula de {self.materia}')
        else:
            print(f'Eu não dou aula')




p1 = Pessoa("vitor", "21 anos", "2200 reais,")
p1.apresentar()
