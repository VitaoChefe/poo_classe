class Pessoa:
    def __init__(self, nome, idade,cpf, salario, trabalhando=True, estudando=False):
        self.__nome = nome
        self._idade = idade
        self.__cpf = cpf
        self._salario = salario
        self._trabalhando = trabalhando
        self._estudando = estudando

    def get_nome(self):
        return self.__nome
    def get_idade(self):
        return self._idade
    def get_cpf(self):
        return self.__cpf
    def get_salario(self):
        return self._salario
    def get_trabalhando(self):
        return self._trabalhando
    def get_estudando(self):
        return self._estudando

    def set_salario(self, valor):
        if valor >= 0:
            self._salario = valor
        else:
            print("salario invalido")

    def apresentar(self):
        print(f'bom dia a todos e todas, sou professor {self.__nome}\n'
              f'minha idade é {self._idade}\n'
              f'meu CPF é {self.__cpf}\n'
              f'meu salario é {self._salario}\n'
              )

        if self._estudando:
            print(' estou estudando')
        else:
            print(f"não esta estudando")

        if self._trabalhando:
            print('estou trabalhando')
        else:
            print(f"não estou trabalhando")

        print("-" * 50)

    def receber(self):
        if self._trabalhando:
            print('estou trabalhando')
            self._salario = self._salario + 100
        else:
            print(f"não estou trabalhando")


class Professor(Pessoa): # herda da classe do professor
    def __init__(self, nome, idade, cpf, salario,materia,local,turma, quantidade_aula,trabalho=True):
        super().__init__(nome, idade, cpf, salario)
        self.__materia = materia
        self.__local = local
        self.__quantidade_aula = quantidade_aula
        self._trabalho = trabalho
        self._turma = turma


    def get_turma(self):
        return self._turma
    def get_local(self):
        return self.__local
    def get_quantidade_aula(self):
        return self.__quantidade_aula
    def get_trabalho(self):
        return self._trabalho
    def get_materia(self):
        return self.__materia


    def apresentar(self):
        print(f"meu nome é {self.get_nome()}\n"
        f" minha idade é {self.get_idade()}\n "
        f" a escola que eu trabalho é { self.get_local() } \n"
        f" meu salario é {self.get_salario()}\n "
        f" a quantidades de aulas que eu dou são {self.get_quantidade_aula()} \n"
        f" Trabalhando: {"Sim" if self._trabalhando else "Não"} \n"
        f" a matéria que eu dou aula é {self.get_materia()} \n "
        )
    def quantidade_de_aulas(self):
        if self.__local:
            aumento = (self.get_quantidade_aula() + self.get_quantidade_aula())
            print(f"Eu dava {self.get_quantidade_aula()} de aulas,agora dou {aumento} aulas")
        elif self.__local:
            print(f"Eu dou aulas")
        else:
            print(f"Eu não dou aulas")

    def receber(self):
        if self._salario:
            print(f"ele não recebe, pois ele não trabalha!!")
        else:
            print('estou trabalhando')

    def passar_materia(self):
        if self.__materia:
            print(f'Eu dou aula de {self.get_materia()} aula')
        else:
            print(f'Eu não dou aula')


p1 = Pessoa("vitor", "23 anos", "30149503865", 1560,True,True)
p1.apresentar()
# prof1 = Professor('vitor', '21 anos', '45821408822', "20000",'matenatica', 'Sesi', '3', 2)
# prof1.apresentar()
# prof1.quantidade_de_aulas()
# prof1.receber()
# nome, idade, cpf, salario,materia,local,turma,trabalho=True
#
# p1 = Pessoa ('Vini', '16','6543456789', '2000')
# p1.apresentar()
# p1.receber()


